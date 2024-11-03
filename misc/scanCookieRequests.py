# for the cookies CTF challenge. iterate making request with a different cookie name (number) to get all the responses
import requests
for i in range(100):
    cookie = 'name={}'.format(i) # define cookie to go in header
    headers = {'Cookie':cookie}
    
    request = requests.get('http://mercury.picoctf.net:21485/check', headers=headers)

    print(request.text)
