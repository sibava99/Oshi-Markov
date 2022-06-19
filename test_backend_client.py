import requests
import json

BASE_URL = "http://localhost:5000/"
# BASE_URL = "https://markov-backend.herokuapp.com/"

def generate_test():
    with open("data/output.txt", "r", encoding="utf-8") as f:
        text = f.read()
    data = {"text":text}      
    response = requests.post(BASE_URL + "generate_text/", data=data)
    print(response.content.decode('utf-8'))
    
def save_model_test():
    with open("data/output.txt", "r", encoding="utf-8") as f:
        text = f.read()
    data = {"text":text}   
    response = requests.post(BASE_URL + "save_model/", data=data)
    print(response.content.decode('utf-8'))
    
def get_model_test():
    response = requests.get(BASE_URL + "generate_text/" + "LC3enAjT1kN7HuFUOq3AuhNk")
    print(response.content.decode('utf-8'))
    
def generate_twitter_test():
    data = {"twitter_id": "@1000000lome"}   
    response = requests.post(BASE_URL + "generate_text_twitter/", data=data)
    # print(vars(response))
    print(json.loads(response.content))

if __name__ == "__main__":
    # generate_test()
    # save_model_test()
    generate_twitter_test()