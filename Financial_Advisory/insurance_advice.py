from flask import Flask, render_template, request, jsonify
import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig, HarmCategory, HarmBlockThreshold
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bob-rg7-gcp-1215eb0055c9.json'
app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="bob-rg7-gcp", location="us-central1")

prompt_template = """You are an AI assistant that helps people with financial advice. Provide a detailed and comprehensive response.

- Age: {age}
- Occupation: {occupation}
- Monthly Income: ₹{monthly_income}
- Monthly Expenses: ₹{monthly_expenses}
- Current Savings: ₹{current_saving}
- Investment Goals: {investment_goals}
- Risk Tolerance: {risk_tolerance}
- Type of Financial Advice Needed: {advice_type}
- Current Financial Products (if any): {current_financial_products}
- Any Debts or Loans: {debts_loans}
- If yes, provide details: ₹{debts_loans_details}
- Please provide me with advice on {query}.
"""

# Generation configuration
generation_config = GenerationConfig(
    max_output_tokens=2192,
    temperature=0.95,
    top_p=0.75,
)

# Safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@app.route('/')
def index():
    return render_template('insurance_advice.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    user_data = request.form.to_dict()
    prompt = create_prompt(user_data)
    advice = generate(prompt)
    return jsonify({'advice': advice})

def create_prompt(user_data):
    return prompt_template.format(**user_data)

def generate(prompt):
    model = GenerativeModel("gemini-1.5-pro-001")
    responses = model.generate_content(
        [prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    full_response = ""
    for response in responses:
        full_response += response.text

    return full_response

if __name__ == '__main__':
    app.run(debug=True)