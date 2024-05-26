import transformers
import torch

from auth_token import hf_access_token

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
access_token = hf_access_token

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    token = access_token,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a good assistant who writes mail based on user's question!"},
    {"role": "user", "content": "Write me a mail for my customer based on the following information"},
]

if __name__ == "__main__":
    while True:
        user_input = input("Enter your question: ")
        if user_input == "exit":
            break
        messages.extend([{"role":"user","content":user_input}])

        prompt = pipeline.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
        )

        terminators = [
            pipeline.tokenizer.eos_token_id,
            pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = pipeline(
            prompt,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        print(outputs[0]["generated_text"][len(prompt):])