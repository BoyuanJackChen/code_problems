import requests

def access_server():
    url = "http://localhost:8000/"
    prompts = ["The future of AI is"]
    sampling_params = {"temperature": 0.8, "top_p": 0.95}
    sample_input = {"prompts": prompts, "sampling_params": sampling_params}
    response = requests.post(url, json=sample_input)
    print(response.json())

if __name__ == "__main__":
    access_server()
