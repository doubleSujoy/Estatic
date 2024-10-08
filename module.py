import os
import requests
import base64
import json

from gradio_client import Client
hf_tok = os.environ.get('hf_key', None)
ChatGptClient = Client("crystal99/test-gpt", hf_token = hf_tok)
tool_sphere_code_model = Client("crystal99/tool-sphere-code-gen", hf_token = hf_tok)  # crystal99/new-code-llama, crystal99/tool-sphere-code-gen
imageGen = Client("crystal99/stabilityai-stable-diffusion-xl-base-1.0", hf_token = hf_tok)
pixleImageGen = Client("crystal99/B2BMGMT_sWizad-pokemon-trainer-sprite-pixelart", hf_token = hf_tok)
#imageGenVone = Client("crystal99/runwayml-stable-diffusion-v1-5", hf_token = hf_tok);
llama3chat = Client("crystal99/chat-llama-3", hf_token = hf_tok);

hostAi = Client("ultrabotbot/Meta-Llama-3-8B-Instruct-chat", hf_token = "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")

headers = {
        "Authorization": f"Bearer {hf_tok}"
}

def giiyel7hosx(q, sm="You are a friendly Chatbot."):
      result = ChatGptClient.predict(
		message=f"{q}",
		system_message=f"{sm}",
		max_tokens=2000,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
      )
      return result


def llama3_chat(q, sm="You are a friendly Chatbot."):
      result = llama3chat.predict(
		message=f"{q}",
		system_message=f"{sm}",
		max_tokens=2000,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
      )
      return result


def bosohwf84kv(q):
      result2 = tool_sphere_code_model.predict(
		message=f"{q}",
		system_message="you are a friendly chat bot named tool-sphere assistant created by tool-sphere team, your purpose is to help people with their code problem and generate code link: https://tool-sphere.github.io/",
	        max_tokens=2100,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
      )
      return result2
	

def imgGenv1(q):
    """result3 = imageGenVone.predict(
		param_0=f"{q}",
		api_name="/predict"
    )
    response = requests.get(f"https://crystal99-runwayml-stable-diffusion-v1-5.hf.space/file={result3}", headers=headers)
    if response.status_code == 200:
	    base64_image = base64.b64encode(response.content)
	    base64_image_str = base64_image.decode('utf-8')
	    return f"data:image/jpeg;base64,{base64_image_str}"
    else:"""
    return "Failed to fetch Image"



def imgGenDetai(q):
    result4 = imageGen.predict(
		param_0=f"{q}",
		api_name="/predict"
    )
    print(f"=> {result4}")
    response = requests.get(f"https://crystal99-stabilityai-stable-diffusion-xl-base-1-0.hf.space/file={result4}", headers=headers)
    if response.status_code == 200:
	    base64_image = base64.b64encode(response.content)
	    base64_image_str = base64_image.decode('utf-8')
	    return f"data:image/jpeg;base64,{base64_image_str}"
    else:
	    return "Failed to fetch Image"


def imageGenPix(q):
    result5 = pixleImageGen.predict(
		param_0=f"{q}",
		api_name="/predict"
    )
    response = requests.get(f"https://crystal99-b2bmgmt-swizad-pokemon-trainer-sprite-pixelart.hf.space/file={result5}", headers=headers)
    if response.status_code == 200:
	    base64_image = base64.b64encode(response.content)
	    base64_image_str = base64_image.decode('utf-8')
	    return f"data:image/jpeg;base64,{base64_image_str}"
    else:
	    return "Failed to fetch Image"
	    
