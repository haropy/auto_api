import requests
import json

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])  # 主要作用是拼接接口请求地址


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)  # json格式化输出


def request_method():
    response = requests.post(build_uri('user/emails'), auth=('haropy', '01TAL0Anet'), json=['740404472@qq.com'])
    print(better_output(response.text))  # 调用json格式化输出
    print(response.request.headers)
    print(response.request.body)


if __name__ == '__main__':
    request_method()
