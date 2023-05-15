from transformers import OpenAiAgent
from transformers import HfAgent

from huggingface_hub import login

agent = OpenAiAgent()

login()

agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")