"""
Here, download the models from huggingface
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"

print(f"torch.cuda.is_available(): {torch.cuda.is_available()}")
print(f"torch.cuda.device_count(): {torch.cuda.device_count()}")
print(f"torch.cuda.get_device_name(0): {torch.cuda.get_device_name(0)}")
print(f"torch.cuda.get_device_name(1): {torch.cuda.get_device_name(1)}")

model_name = "cais/HarmBench-Llama-2-13b-cls"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")