from transformers import AutoTokenizer
from transformers import pipeline
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model, token="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")

llama_pipeline = pipeline(
    "text-generation",  # LLM task
    model=model,
    torch_dtype=torch.float32,
    device_map="auto",
)