import requests

url_upload = 'http://127.0.0.1:5000/upload'

url_analyze = 'http://127.0.0.1:5000/analyze'

files = {'file': open('test.png','rb')}

r_upload = requests.post(url_upload, files=files)

r_analyze = requests.post(url_analyze, json={"method": "glcm", "classifyer": "mlp"})

print(r.json())
