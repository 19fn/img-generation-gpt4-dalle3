import os
from openai import AzureOpenAI

class AzureOpenAiService:
    def __init__(self):
        # Load environment variables for Azure OpenAI service
        self.azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

        # Check if the environment variables are set
        if not self.azure_openai_endpoint or not self.azure_openai_api_key:
            raise ValueError("Azure OpenAI endpoint and API key must be set in environment variables")

        # Initialize the OpenAI client
        self.client = AzureOpenAI(
            azure_endpoint=self.azure_openai_endpoint,
            api_key=self.azure_openai_api_key,
            api_version="2024-02-01"
        )

    def get_chat_completion(self, messages):
        """Send chat messages to Azure OpenAI and get a response."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Set model to your deployment name
                messages=messages,
                temperature=0.4
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Error occurred while fetching chat completion: {str(e)}") from e

    def get_image_generation(self, prompt):
        """Send a prompt to Azure OpenAI to generate an image."""
        try:
            response = self.client.images.generate(
                model="dall-e-3",  # Set model to your deployment name
                prompt=prompt,
                n=1,
                style="natural",
                response_format="b64_json"
            )
            return response
        except Exception as e:
            raise RuntimeError(f"Error occurred while generating image: {str(e)}") from e