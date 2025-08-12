from elevenlabs.conversational_ai.conversation import ClientTools
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os
import requests
import openai
import uuid

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

client_tools = ClientTools()

def searchWeb(parameters):
    query = parameters.get("query") or ""
    ddg = DuckDuckGoSearchRun()
    try:
        return ddg.run(query)
    except Exception as e:
        return {"error": str(e)}

def save_to_txt(parameters):
    filename = parameters.get("filename") or f"output_{uuid.uuid4()}.txt"
    data = parameters.get("data", "")
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{data}\n")
    return {"saved_to": filename}

def create_html_file(parameters):
    filename = parameters.get("filename") or f"page_{uuid.uuid4()}.html"
    title = parameters.get("title", "")
    data = parameters.get("data", "")
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title></head><body><h1>{title}</h1><div>{data}</div></body></html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return {"created": filename}

def generate_image(parameters):
    prompt = parameters.get("prompt", "")
    size = parameters.get("size", "1024x1024")
    save_directory = parameters.get("save_directory", "generated_images")
    filename = parameters.get("filename") or f"image_{uuid.uuid4()}.png"
    os.makedirs(save_directory, exist_ok=True)
    if not filename.lower().endswith(".png"):
        filename = filename + ".png"
    path = os.path.join(save_directory, filename)
    response = openai.Image.create(prompt=prompt, n=1, size=size)
    image_url = response.data[0].url
    resp = requests.get(image_url, timeout=30)
    resp.raise_for_status()
    with open(path, "wb") as f:
        f.write(resp.content)
    return {"image_path": path}

client_tools.register("searchWeb", searchWeb)
client_tools.register("saveToTxt", save_to_txt)
client_tools.register("createHtmlFile", create_html_file)
client_tools.register("generateImage", generate_image)

TOOL_FUNCTIONS = {
    "searchWeb": searchWeb,
    "saveToTxt": save_to_txt,
    "createHtmlFile": create_html_file,
    "generateImage": generate_image,
}
