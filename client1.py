import requests

def access_server():
    url = "http://localhost:8000/"
    prompt = "What is the weather like in Abu Dhabi?"
    sample_input = {"prompt": prompt, "stream": True, "temperature": 0.7}
    response = requests.post(url, json=sample_input)
    for line in response.iter_lines():
        print(line.decode("utf-8"))

if __name__ == "__main__":
    access_server()
