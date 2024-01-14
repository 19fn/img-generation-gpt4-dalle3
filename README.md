# Azure OpenAI Playground

An interactive sandbox providing a hands-on experience with the most recent OpenAI models.

## Features

- GPT-4
- GPT-4 TURBO
- DALLE-3

## Getting Started

### Prerequisites

- Python (version 3.9.6)
- Flask (version 3.0.0)
- Azure OpenAI Key and endpoint

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/19fn/openai-playground.git
    ```

2. Navigate to the project directory:

    ```bash
    cd openai-playground
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up environment variables.
     ```bash
      # Azure OpenAI key
      export AZURE_OPENAI_KEY="replace-with-openai-key"
     
      # Azure OpenAI endpoint
      export AZURE_OPENAI_ENDPOINT="replace-with-openai-endpoint"

      # Flask secret key
      export FLASK_SECRET_KEY="replace-with-random-secret-key"
     ```

2. Run the Flask app:

    ```bash
    flask run
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000` to view the app.
