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
        {"role": "system", "content": """When crafting a prompt to generate motivational and inspiring images, focus on creating visuals that resonate emotionally, encourage people to overcome challenges, and foster a sense of strength, love, focus, and perseverance. Consider the following elements:
            1. Theme and Message:
            Core Message: Choose a theme that reflects motivation, such as overcoming adversity, personal growth, resilience, or the pursuit of dreams. The image should inspire action and positive emotions like hope, love, and courage.
            Contextual Setting: Place the scene in environments that evoke determination and self-improvement. This can include a gym setting symbolizing physical endurance, a serene natural landscape symbolizing peace and reflection, or moments of victory and success.
            2. Visuals and Symbolism:
            Powerful Imagery: Use visual elements that reinforce the message. For example, hands reaching for the sky to symbolize hope, runners crossing a finish line to depict achievement, or a sunrise to represent new beginnings.
            Colors and Emotion: Opt for bold, energizing colors like red and orange to convey passion and intensity, or calming blues and greens for themes of peace, healing, and perseverance. Consider the emotional impact of the colors on the viewer.
            Symbolic Elements: Include powerful symbols such as weights (for overcoming challenges), hearts (for love and empathy), arrows (for progress), or light (for hope and clarity).
            3. Follow the Format:
            Responses must adhere to the format: Prompt: "MY_RESPONSE_GO_HERE"
            """},
        {"role": "user", "content": "Give a random prompt:"}
    ]

    try:
        # Generate the prompt
        response = llm.get_chat_completion(messages)
        logger.info("Chat completion successfully retrieved.")
    except Exception as e:
        logger.error(f"Error retrieving chat completion: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # Use regex to extract the clean response from the returned content
    match = re.search(r'"(.*?)"', response)
    if match:
        logger.info("Clean prompt - done")
        clean_response = match.group(1)
        return {"prompt": clean_response}
    else:
        logger.error(f"Could not extract prompt from response: {response}")
        return {"prompt": "Could not extract prompt."}

@app.post("/generate-image")
async def generate_image(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt")
        
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        llm = AzureOpenAiService()
        
        # Generate the image using the provided prompt
        response_img = llm.get_image_generation(prompt)
        
        if response_img:
            logger.info(f"Image URL - done")
            image_url = response_img.data[0].b64_json
            return {"image_url": image_url}
        else:
            logger.error("No image URL returned.")
            return {"image_url": None}
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

