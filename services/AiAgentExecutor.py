import os
import tempfile

from autogen import ConversableAgent
import autogen
from autogen.coding import DockerCommandLineCodeExecutor


# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    image="python:3.12-slim",  # Execute code using the given docker image name.
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration that uses docker.
code_executor_agent = ConversableAgent(
    "code_executor_agent_docker",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the docker command line code executor.
    human_input_mode="NEVER",  # Always take human input for this agent for safety.
)

code_writer_system_message = """When crafting a prompt to generate stunning and meaningful images, consider the following elements:

            1. Theme and Setting:
            - Focus on a specific environment or scene, such as a natural landscape (forests, oceans, deserts) or an abstract space setting (nebulae, alien worlds).
            - Describe the atmosphere vividly, using sensory details. For example, mention the type of light (soft, golden, glowing), temperature (warm, chilly), and textures (smooth, rugged, misty).

            2. Emotional Tone:
            - Convey the emotional depth of the image. Should the scene feel serene, mysterious, awe-inspiring, or melancholic? Use words like 'calm,' 'haunting,' 'joyful,' or 'introspective' to evoke the desired feeling.

            3. Color Palette:
            - Mention a specific set of colors or mood-based hues. Are the colors vibrant and bold, or muted and subtle? Do they create a sense of peace (pastel blues, greens) or energy (bright reds, oranges)?

            4. Imagery and Details:
            - Add layers of detailed imagery that enhance the feeling, like celestial bodies (stars, moons, galaxies), elements of nature (trees, waterfalls, sand dunes), or abstract patterns (fractals, floating shapes).
            - Think about scale: do you want vast, epic spaces or close, intimate scenes?

            5. Surreal/Conceptual Touch:
            - Add an element of the fantastical or surreal. Blend unexpected ideas together, like 'a forest made of glowing crystal trees,' or 'an ocean of liquid stardust.' This gives the image a dream-like quality.
            
            6. Follow the format:
            - Response must follow the format ' Prompt: "MY_RESPONSE_GO_HERE" '
            - Reply 'TERMINATE' in the end when everything is done.

            Example Prompt:
            'A vast, glowing nebula stretches across the night sky, casting soft purple and blue light over a tranquil forest below. The trees shimmer with silver leaves, swaying gently in a cool breeze. The atmosphere feels both serene and mysterious, as if the stars themselves are alive with quiet energy. The scene is bathed in a mix of deep indigos and subtle pinks, creating a cosmic, otherworldly feeling. TERMINATE'
            """

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
)

code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=code_writer_system_message,
    llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution for this agent.
)

chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message="Write a random prompt.",
)

# When the code executor is no longer used, stop it to release the resources.
# executor.stop()