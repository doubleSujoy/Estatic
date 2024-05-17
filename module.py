import os
import requests
import base64
import json

from gradio_client import Client
hf_tok = os.environ.get('hf_key', None)
ChatGptClient = Client(os.environ.get('infiChatModel', None), hf_token = hf_tok)
tool_sphere_code_model = Client("crystal99/tool-sphere-code-gen", hf_token = hf_tok)  # crystal99/new-code-llama, crystal99/tool-sphere-code-gen
imageGen = Client("crystal99/stabilityai-stable-diffusion-xl-base-1.0", hf_token = hf_tok)
pixleImageGen = Client("crystal99/B2BMGMT_sWizad-pokemon-trainer-sprite-pixelart", hf_token = hf_tok)
imageGenVone = Client("crystal99/runwayml-stable-diffusion-v1-5", hf_token = hf_tok);
llama3chat = Client("crystal99/chat-llama-3", hf_token = hf_tok);

headers = {
        "Authorization": f"Bearer {hf_tok}"
}

def giiyel7hosx(q, sm="You are a friendly Chatbot."):
      result = ChatGptClient.predict(
		message=f"{q}",
		request=f"{sm}",
		param_3=512,
		param_4=0.7,
		param_5=0.95,
		api_name="/chat"
      )
      return result


def llama3_chat(q, sm="You are a friendly Chatbot."):
      result = llama3chat.predict(
		message=f"{q}",
		request=f"{sm}",
		param_3=2000,
		param_4=0.7,
		param_5=0.95,
		api_name="/chat"
      )
      return result


def bosohwf84kv(q):
      result2 = tool_sphere_code_model.predict(
		message=f"{q}",
		request="you are a generative ai large language model, your name is infinite gpt you are created by yourself, users can use you into there project by an api endpoint which documentation is provided https://infinite.gpt in this site but you dont have an official website, currently you are working as a code assistant in tool-sphere website but you are a full chat large language model, tool-sphere is a website where a lots of free online tools available tool-sphere website link: https://tool-sphere.github.io/  in this site many tools are provided such as email sender -> anyone can send email using this tool qithout having a mail account both html and text emails are supported, ai code generator -> where user can generate code from natural language, temp-mail-generator -> using this tool users can create temporary disposable email address to use to login or keep their original email spam free, no other tools, you dont send too much lengthy response from",
		param_3=2100,
		param_4=0.7,
		param_5=0.95,
		api_name="/chat"
      )
      return result2
	

def imgGenv1(q):
    result3 = imageGenVone.predict(
		param_0=f"{q}",
		api_name="/predict"
    )
    response = requests.get(f"https://crystal99-runwayml-stable-diffusion-v1-5.hf.space/file={result3}", headers=headers)
    if response.status_code == 200:
	    base64_image = base64.b64encode(response.content)
	    base64_image_str = base64_image.decode('utf-8')
	    return f"data:image/jpeg;base64,{base64_image_str}"
    else:
	    return "Failed to fetch Image"



def imgGenDetai(q):
    result4 = imageGen.predict(
		param_0=f"{q}",
		api_name="/predict"
    )
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
	    
