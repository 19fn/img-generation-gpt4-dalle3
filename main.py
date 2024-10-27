import re
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.AzureOpenAiService import AzureOpenAiService

# Configure logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Create a Jinja2Templates object and point it to the "templates" directory
templates = Jinja2Templates(directory="templates")

@app.get("/prompter", response_class=HTMLResponse)
async def main_page(request: Request):
    # Render the "index.html" template and pass any context (e.g., request)
    logger.info("Main page accessed.")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-prompt")
async def generate_prompt(request: Request):
    llm = AzureOpenAiService()

    messages = [
        {"role": "system", "content": """When crafting a prompt to generate stunning and meaningful images, focus on creating realistic representations that reflect human creativity and interaction with the environment. Consider the following elements:

            1. Theme and Setting:

                - Choose a specific environment or scene that embodies realism, such as bustling cityscapes, serene rural landscapes, or historical settings.
                - Incorporate elements that showcase human activity and creativity, such as architecture, vehicles (cars, boats, planes), and everyday life scenarios. Include people engaging in various activities to bring the scene to life.
            
            2. Imagery and Details:

                - Enhance your prompt with layers of realistic imagery that evoke emotion and depth, such as natural phenomena (sunsets, storms, wildlife) or detailed city scenes (busy streets, market places).
                - Think about scale: do you want to depict vast urban panoramas or intimate moments between individuals? Consider how lighting and perspective can influence the mood of the scene.
            
            3. Follow the Format:

                - Responses must adhere to the format: Prompt: "MY_RESPONSE_GO_HERE"
                    """},
        {"role": "user", "content": "Give a random prompt:"}
    ]

    try:
        response = llm.get_chat_completion(messages)
        logger.info("Chat completion successfully retrieved.")
    except Exception as e:
        logger.error(f"Error retrieving chat completion: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # Use regex to extract the clean response from the returned content
    match = re.search(r'"(.*?)"', response)
    if match:
        logger.info(response)
        clean_response = match.group(1)
        try:
            response_img = llm.get_image_generation(clean_response)
            if response_img:
                logger.info(f"Image URL: {response_img.data[0].url}")
                image_url = response_img.data[0].url
            else:
                logger.error("No image URL returned.")
                image_url = None
        except Exception as e:
            logger.error(f"Error generating image: {e}")
            image_url = None
    else:
        logger.error(f"Could not extract prompt from response: {response}")
        clean_response = "Could not extract prompt."
        image_url = None

    return {"message": clean_response, "image_url": image_url}
