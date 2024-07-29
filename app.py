# app.py
from flask import Flask, render_template, request, jsonify
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
from threading import Thread
app = Flask(__name__)
from flask import Flask, render_template, request, jsonify
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="bob-rg7-gcp", location="us-central1")

# Load the PDF document
with open('/content/carloan.pdf', 'rb') as file:
    pdf_content = file.read()
document1 = Part.from_data(
    mime_type="application/pdf",
    data=base64.b64encode(pdf_content).decode()
)

prompt_template = """You are an AI assistant that helps people with financial advice. The answer should be descriptive.
I am of age: {age}
occupation: {occupation}
monthly income: {monthly_income}
monthly expenses: {monthly_expenses}
current saving: {current_saving}
investment goals: {investment_goals}
risk tolerance: {risk_tolerance}
car price is {car_price}
loan term: {loan_term}
on floating interest rate

What is the interest rate being offered on the loan? {interest_rate}
Do you have any other outstanding loans? {outstanding_loans}
What is your credit score? {credit_score}

Please provide me with {query} advice."""

generation_config = {
    "max_output_tokens": 2192,
    "temperature": 0.95,
    "top_p": 0.75,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    user_data = request.json
    prompt = prompt_template.format(**user_data)

    model = GenerativeModel("gemini-1.5-pro-001")
    response = model.generate_content(
        [prompt, document1],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    return jsonify({"advice": response.text})

# Initialize Vertex AI
vertexai.init(project="bob-rg7-gcp", location="us-central1")

# Load the PDF document
with open('/content/carloan.pdf', 'rb') as file:
    pdf_content = file.read()
document1 = Part.from_data(
    mime_type="application/pdf",
    data=base64.b64encode(pdf_content).decode()
)

prompt_template = """You are an AI assistant that helps people with financial advice. The answer should be descriptive.
I am of age: {age}
occupation: {occupation}
monthly income: {monthly_income}
monthly expenses: {monthly_expenses}
current saving: {current_saving}
investment goals: {investment_goals}
risk tolerance: {risk_tolerance}
car price is {car_price}
loan term: {loan_term}
on floating interest rate

What is the interest rate being offered on the loan? {interest_rate}
Do you have any other outstanding loans? {outstanding_loans}
What is your credit score? {credit_score}

Please provide me with {query} advice."""

generation_config = {
    "max_output_tokens": 2192,
    "temperature": 0.95,
    "top_p": 0.75,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice1():
    user_data = request.json
    prompt = prompt_template.format(**user_data)

    model = GenerativeModel("gemini-1.5-pro-001")
    response = model.generate_content(
        [prompt, document1],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    return jsonify({"advice": response.text})

def run_flask(port):
    app.run(port=port, debug=True, use_reloader=False)

# Start the Flask app in a separate thread
flask_thread = Thread(target=run_flask, args=(8001,))
flask_thread.start()

# Use ngrok to create a public URL
from google.colab.output import eval_js
print(eval_js("google.colab.kernel.proxyPort(8001)"))