<div align="center">
    <h2>Code Vipassana - Project Saadhna 2024</h2>
    Team Members: <i> <a href="mailto:atharvamundke22@gmail.com">Atharva Mundke</a>, <a href="mailto:shwetanagapure1024@gmail.com">Shweta Nagapure</a> 
</div>

---
### Team Name: TechX

## Financial Advisory Bot using RAG with GenAI

---

### 1. Objective
Transform financial advisory services through generative AI, delivering customized financial advice based on individualized data analysis. This approach utilizes advanced algorithms to interpret customer data and market trends, ensuring tailored recommendations that adapt to changing financial landscapes, ultimately enhancing client outcomes and satisfaction.

---

### 2. Challenges
1. Analyze customer financial data and market trends to generate tailored investment strategies.
2. Offer real-time advisory services that adapt to changing financial conditions and customer goals.
3. Ensure transparency and explainability in the AI-driven advisory process to build customer trust and confidence.

---

### 3. Problem Statement
In today's complex financial landscape, individuals struggle to access personalized, timely, and data-driven financial advice. Traditional advisory services are often expensive, not readily available 24/7, and may not always incorporate real-time market trends. There's a pressing need for an innovative solution that democratizes access to high-quality financial advice, adapts to changing market conditions, and aligns with individual financial goals.

---

### 4. Solution Overview
The Financial Advisory Assistant Bot aims to address this gap by delivering swift, precise, and context-aware financial advice using advanced AI technologies. Leveraging Retrieval-Augmented Generation (RAG) and Generative AI, this bot integrates real-time data from financial news and banking websites, stored in a MySQL relational database, to ensure up-to-date and accurate responses.

---

# Financial Advice Chatbot

This project implements a financial advice chatbot using Vertex AI's Gemini Pro model. It integrates with Google Colab and provides a user-friendly interface through ipywidgets.

## Features

- **User Input:** Collects relevant financial information from the user through a form.
- **Prompt Generation:** Constructs a detailed prompt incorporating user data and the query.
- **AI-Powered Advice:** Leverages Gemini Pro to generate personalized financial advice.
- **Safety Measures:** Implements safety settings to filter out harmful content.

## Requirements

- **Google Colab:** The code is designed to run within a Google Colab environment.
- **Vertex AI:** Requires access to Vertex AI and the Gemini Pro model.
- **Libraries:** Install necessary libraries using `!pip install ipywidgets google-cloud-aiplatform`.

## Usage

1. **Upload PDF:** Upload your financial document (e.g., bank statement, loan agreement) to Colab.
2. **Authenticate:** Authenticate your Google account to access Vertex AI.
3. **Fill the Form:** Provide your financial details and specify your query in the interactive form.
4. **Get Advice:** Click the "Get Advice" button to generate personalized financial advice.

## Code Structure

- **`app.py`:** Flask application for web deployment (not used in Colab).
- **Colab Notebook:**
    - Imports necessary libraries.
    - Handles PDF upload and authentication.
    - Defines prompt template, generation config, and safety settings.
    - Creates input widgets and a button to trigger advice generation.
    - Displays the interactive form and output area.
