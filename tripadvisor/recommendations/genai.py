# Generative AI results based on imput prompts
from transformers import AutoModelForCausalLM, AutoTokenizer

class generativeAI():
    def __init__(self, prompt):
        self.prompt = prompt
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.generateResponse()
    
    def generateResponse(self):
        input_ids = self.tokenizer.encode(self.prompt, return_tensors="pt", max_length=512, truncation=True)
        attention_mask = input_ids.ne(1).long()
        
        output = self.model.generate(
            input_ids, 
            attention_mask=attention_mask, 
            pad_token_id=self.model.config.eos_token_id, 
            max_length=500, 
            num_return_sequences=1, 
            temperature=0.7, 
            top_k=5,
            do_sample=True
        )
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text

