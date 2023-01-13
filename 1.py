import requests
response = requests.get("https://google.com")
print(response.text)

gitscript = requests.get("https://raw.githubusercontent.com/FNov10/CMPUT401Lab1/main/1.py")
print(gitscript.text)