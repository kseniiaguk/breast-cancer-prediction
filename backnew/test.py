import requests

url_upload = 'http://127.0.0.1:5000/upload'

url_analyze = 'http://127.0.0.1:5000/analyze'

files = {'file': open('2.png', 'rb')}
#r = requests.post(url_upload, files=files)

r = requests.post(url_analyze, json={"method": "glcm", "classifyer": "rf"})

print(r.json())
