import requests

url_upload = 'http://127.0.0.1:5000/upload'

url_analyze = 'http://127.0.0.1:5000/analyze'

files = {'file': open('test.png','rb')}

r = requests.post(url, files=files)

r = requests.post(url, json={"method": "glcm", "classifyer": "mlp"})

print(r.json())