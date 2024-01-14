import os
from openai import AzureOpenAI
import requests
import json

def chatCompletions(model, content):
    client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_KEY"),
                api_version='2023-05-15', 
                azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            )


    response = client.chat.completions.create(
        model=f"{model}",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{content}"}
        ]
    )

    return response.choices[0].message.content

def imgGeneration(model,content):
    client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_KEY"),
                api_version='2023-12-01-preview', 
                azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            )

    result = client.images.generate(
        model=model,
        prompt=content,
        n=1
    )

    json_response = json.loads(result.model_dump_json())

    # Retrieve the generated image
    image_url = json_response["data"][0]["url"]
    generated_image = requests.get(image_url).content

    return generated_image

