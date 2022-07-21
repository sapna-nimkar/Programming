import requests
from pprint import pprint
import json
import os

try:
    base_url = os.environ['BASE_URL']
    
except KeyError as err:
    # base_url = 'https://reqres.in'
    print(f"Key error for {err}")
except ZeroDivisionError as err:
    print("Can't divide by 0")
except Exception as err:
    print(err)

def get_environ_settings(env):
    filename = ""
    if env == 'prd':
        filename = "prod.json"
    elif env == 'dev':
        filename = "dev.json"
    else:
        filename = "local.json"
    
    with open(f"settings/{filename}") as f:
        data = json.load(f)
        
    return data



def get_users():
    uri = 'api/users'
    query_params = "page=2"
    headers = {}
    url = "{}/{}?{}".format(base_url, uri, query_params)
    response = requests.get(url, headers= headers)
    pprint(response.status_code)
    # pprint(response.headers)
    # pprint(response.cookies)
    # pprint(response.json())
    # pprint(response.text)
    # pprint(response.elapsed)

def post_user(name, job):
    url = 'https://reqres.in/api/users'
    body = {
        "name": name,
        "job": job
    }
    headers = {
       "xapi-key": "sadsaD"
    }
    response = requests.post(url=url, data=body, headers=headers)
    pprint(response.status_code)
    pprint(response.headers)
    pprint(response.cookies)
    pprint(response.json())
    pprint(response.text)
    pprint(response.elapsed)


if __name__ == "__main__":
    # get_users()
    # post_user("Supratim", "IT")
    # d = {
    #     "name": 'name',
    #     "job": 'job'
    # }
    # s = json.dumps(d)
    # print(type(s), s)
    # print(s[1])
    # j = json.loads(s)
    # print(type(j), j)
    #env = 'username=sapna;name=Sapna;age=30'
    setting = get_environ_settings(os.environ['env'])
    print(setting)