import requests
import pprint
import json

'''
-> Do a GET requests on Reqres LIST USERS API
-> Print the Status Code and Status Message
-> Assert Page ID in path parameter and Page Id in Response is Equal
-> Assert Size of Data List in response json to be Equal to per_page value
-> Print the Status Code and Error Message when invalid input is passed

->Hit this api "n" number of times 
  and extract the response time for all the hits 
  and display the least response time taken value and hit count

'''
base_url = 'https://reqres.in/api/users'
query_params = 'page=2'
headers = {'Connection': 'keep-alive'}
url = "{}?{}".format(base_url, query_params)

def get_users():
    
    response = requests.get(url, headers = headers)
    pprint.pprint(response.status_code)
    pprint.pprint(response.reason)
    print(response.json()['page'])

def assert_get_users():
    response = requests.get(url, headers = headers)
    expected_value = query_params.split('=')
    assert int(expected_value[1]) == response.json()['page'] , 'Page ID in path parameter is not equal to page id in response'
    assert response.json()['per_page'] == len(response.json()['data']) , 'per_page value in response is not equal to length of data array'

#hit this API "n" number of times
def get_min_responsetime(n):
    response_times = []
    for i in range(n):
        response = requests.get(url, headers = headers)
        response_times.append(response.elapsed)
    response_times.sort()
    
    return response_times[0].total_seconds()

def create_users():
    body = {
        "name" : 'sapna',
        "job" : 'create'
    }
    response = requests.post(url, headers = headers, data = body)
    print(response.status_code)
    print(response.reason)
    print(response.elapsed.total_seconds())

if __name__ == '__main__':
    get_users()
    assert_get_users()
    print(get_min_responsetime(10))
    create_users()
