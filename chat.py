import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

parser = argparse.ArgumentParser()
parser.add_argument("model_name", type=str, help="Name or path of the model to use for dialogue")
parser.add_argument("user_input", type=str, help="The first user input to start the dialogue")
args = parser.parse_args()

model_name = args.model_name
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

while True:
    user_input = input("User: ") if not args.user_input else args.user_input
    if user_input == "exit":
        break
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=1000, do_sample=True)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Bot: " + output_text)
    args.user_input = None
