#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/19 22:03
import requests
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
resp = requests.get('http://127.0.0.1:8000',headers=headers)
print(resp.text)