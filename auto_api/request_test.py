#:coding:utf-8
import requests

# 请求百度网页
re = requests.get('http://www.baidu.com', data=None, timeout=10)
print(re.headers)
