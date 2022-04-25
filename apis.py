from urllib import response
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get
header = {"Accept": "applications/vnd.github.v3+json"}
print("Status Code:" + str(r.status_code))
response_dict = r.json()
repository_dicts = response_dict("items")
repo_dict = repository_dicts[0]
for key in sorted (repo_dict.keys()):
    print(key)
