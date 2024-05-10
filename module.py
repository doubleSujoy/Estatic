import os
import requests
import base64

from gradio_client import Client
hf_tok = os.environ.get('hf_key', None)
ChatGptClient = Client(os.environ.get('infiChatModel', None), hf_token = hf_tok)
tool_sphere_code_model = Client("crystal99/tool-sphere-code-gen", hf_token = hf_tok)
imageGen = Client("crystal99/stabilityai-stable-diffusion-xl-base-1.0", hf_token = hf_tok)
pixleImageGen = Client("crystal99/B2BMGMT_sWizad-pokemon-trainer-sprite-pixelart", hf_token = hf_tok)
imageGenVone = Client("crystal99/runwayml-stable-diffusion-v1-5", hf_token = hf_tok);

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

def bosohwf84kv(q):
      result2 = tool_sphere_code_model.predict(
		message=f"{q}",
		request="You are a friendly Chatbot.",
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
    response = requests.get(f"https://crystal99-runwayml-stable-diffusion-v1-5.hf.space/file=${result3}")
    if response.status_code == 200:
	    base64_image = base64.b64encode(response.content)
	    base64_image_str = base64_image.decode('utf-8')
	    return f"data:image/jpeg;base64,{base64_image_str}"
    else:
	return "Failed to fetch Image"



def imgGenDetai(q):
	result = "some"
	return result

def imageGenPix(q):
	result = "some"
	return result

