import time
import json
import base64
from Crypto.Cipher import AES
import requests
from pathlib import Path

from conf import comments_root
from toplist import get_toplist_ids


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Cookie': 'JSESSIONID-WYYY=vDeNaw5OspW8kcNaX%5CsngVIwR3Z%2FigZ0HHGIb2duQgPm%2FFhGpQs6c26bKN3xf9tOatRbKk1JlTpJCiNsrZCsACk%2BN296WbpNc%2Fn96i8Ih6NYvHkjqXRR165SZAxv9YkkSAzfH9WTgCnyJUV6PEB9mm%2BJsduyy0B%5Cf2S7zXIdbls2hHY7%3A1519467798967; _iuqxldmzr_=32; _ntes_nnid=fc7bf97086aab1c7e5ea7559945fc3fe,1519465998987; _ntes_nuid=fc7bf97086aab1c7e5ea7559945fc3fe; __utma=94650624.1089055467.1519466000.1519466000.1519466000.1; __utmz=94650624.1519466000.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ngd_tid=izuEtMCQO5AHgNjd7VBI%2FItSs427hfCz',
}


def get_params(page_num, count):
    page_num = (page_num - 1) * 100

    first_param = {
        "rid":          "R_SO_4_418603077",
        "offset":       page_num,
        "total":        False,
        "limit":        count,
        "csrf_token":   ""
    }

    first_param = json.dumps(first_param)
    first_key  = "0CoJUm6Qyw8W8jud"
    second_key = "nienienienienien"
    h_encText = AES_encrypt(first_key, first_param).decode('utf-8')
    h_encText = AES_encrypt(second_key, h_encText).decode('utf-8')
    return h_encText


def AES_encrypt(key, text):
    iv = '0102030405060708'
    pad = 16 - len(text) % 16
    text +=  pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_encSecKey():
    encSrcKey = "6469da86a183fc2fc9df65ac98f67138c8d3048d0626714fe646ecb564d4f8cd386a9c9618bb8a4f2929e50ba32e8991266aba783975e39cc7cf8a61cc3ba76c81c64a3414f38d604ca1bf9f4647c29cd92d5b362eff15cf7bb1e3a52df798a52aafac2f09420a68af9686e2c1a294ccf426b5aac64899486011fc7eca8e79b8"
    return encSrcKey


def get_comments(music_id, page_num):
    music_path = Path(comments_root) / str(music_id)
    music_path.mkdir(parents=True, exist_ok=True)

    count = 100
    # for page_index in range(page_num, 0, -1):b
    for page_index in range(1, page_num + 1):
        data = {
            'params': get_params(page_index, count),
            'encSecKey': get_encSecKey()
        }
        url = f"http://music.163.com/weapi/v1/resource/comments/R_SO_4_{music_id}?csrf_token="
        resp = requests.post(url, headers=headers, data=data).content
        resp_json = json.loads(resp)
        json.dump(resp_json, open(music_path / f'{page_index}.json', 'w'))


if __name__=='__main__':
    toplist_ids = get_toplist_ids()
    toplist_ids = toplist_ids[90:100]
    print(toplist_ids)

    for c, music_id in enumerate(toplist_ids):
        print(f"{c}/{len(toplist_ids)}:", music_id)
        time.sleep(5)
        get_comments(music_id=music_id, page_num=10)

