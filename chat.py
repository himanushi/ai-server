import argparse
from transformers import AutoModelForSeq2SeqLM, AutoModelForCausalLM, AutoTokenizer

parser = argparse.ArgumentParser()
parser.add_argument("model_name", type=str, help="Name or path of the model to use for dialogue")
parser.add_argument("user_input", type=str, help="The first user input to start the dialogue")
args = parser.parse_args()

model_name = args.model_name

if "t5" in model_name:
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
elif "m2m100" in model_name:
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
else:
    model = AutoModelForCausalLM.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

while True:
    user_input = input("User: ") if not args.user_input else args.user_input
    if user_input == "exit":
        break
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    if "t5" in model_name or "m2m100" in model_name:
        output = model.generate(input_ids, max_length=1000, do_sample=True)
    else:
        output = model.generate(input_ids, max_length=1000, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Bot: " + output_text)
    args.user_input = None
