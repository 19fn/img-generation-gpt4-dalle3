# Prompter2iMG

Use GPT-4 to create prompts for generating unique images using DALL-E 3.

## OpenAI's Models

- GPT-4o-mini
- DALL-E 3

## Getting Started

### Prerequisites

- Python (version 3.9.6 or above)
- Azure OpenAI key and endpoint

### How to Run It Locally

1. **Set Up Python Virtual Environment**  
   First, create a Python 3 virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   With the virtual environment activated, install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Check Dependencies (Optional)**  
   You can check the installed dependencies using:

   ```bash
   pip freeze  
   ```

### Configure Azure OpenAI

5. **Set Azure OpenAI Environment Variables**  
   You need to export the Azure OpenAI environment variables:

   - Set the base API endpoint for Azure OpenAI:

     ```bash
     export AZURE_OPENAI_ENDPOINT=https://RESOURCE_NAME.openai.azure.com/
     ```

   - Set the Azure OpenAI API key:

     ```bash
     export AZURE_OPENAI_API_KEY=REPLACE_WITH_API_KEY
     ```

### Run the Project

6. **Run the Project with Uvicorn**  
   To run the FastAPI application:

   ```bash
   uvicorn main:app
   ```

7. **Run on a Specific Host**  
   To specify the host:

   ```bash
   uvicorn main:app --host 127.0.0.1
   ```

8. **Run on a Specific Port**  
   To specify the port:

   ```bash
   uvicorn main:app --port 5000
   ```

9. **Run on Both Custom Host and Port**

   ```bash
   uvicorn main:app --host=0.0.0.0 --port=5000
   ```

### Default Behavior

By default, FastAPI runs on `localhost` with port `8000`.

Open the app in your browser:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)
