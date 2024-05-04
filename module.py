import os
from gradio_client import Client
hf_tok = os.environ.get('hf_key', None)
ChatGptClient = Client(os.environ.get('infiChatModel', None), hf_token = hf_tok)
tool-sphere-code-model = Client("crystal99/tool-sphere-code-gen", hf_token = hf_tok)

def giiyel7hosx(q):
  result = ChatGptClient.predict(
		message=f"{q}",
		request="You are a friendly Chatbot.",
		param_3=512,
		param_4=0.7,
		param_5=0.95,
		api_name="/chat"
)
  return result

def bosohwf84kv(q):
  result = client.predict(
		message=f"{q}",
		request="You are a friendly Chatbot.",
		param_3=2100,
		param_4=0.7,
		param_5=0.95,
		api_name="/chat"
)
return result

