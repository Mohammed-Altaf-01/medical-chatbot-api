import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pydantic import BaseModel
from fastapi import HTTPException

class UserQuery(BaseModel):
    user_query: str


class ChatBot:
    def __init__(self):
        self.tokenizer = None 
        self.model = None 
    
    def load_from_hub(self,model_id: str):
        self.tokenizer =  AutoTokenizer.from_pretrained(model_id,
                                          device_map = 'auto')
        self.model = AutoModelForCausalLM.from_pretrained(model_id,
                                             device_map='auto')
        
    def get_response(self,text: UserQuery) -> str:
        if not self.model or not self.tokenizer:
            raise HTTPException(status_code=400, detail="Model is not loaded")
            
        inputs = self.tokenizer(text,return_tensors='pt')
        outputs = self.model.generate(**inputs,
                                 max_new_tokens = 100,
                                )
        response = self.tokenizer.decode(outputs[0],skip_special_tokens=True)
        response = self.get_clean_response(response) 
        return response

    def get_clean_response(self,response:list[str] | str) -> str:
        if type(response) == list:
            response = response[0].split("\n")
        else:
            response = response.split("\n")

        ans = ''
        cnt = 0 # to verify if we have seen Human before 
        for answer in response:
            if answer.startswith("[|Human|]"): cnt += 1

            elif answer.startswith('[|AI|]'):
                answer = answer.split(' ')
                ans += ' '.join(char for char in answer[1:])
                ans += '\n'

            elif cnt:
                ans += answer + '\n'
        return ans