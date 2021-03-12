"""
ref

curl
https://soyoung-new-challenge.tistory.com/92

BeautifulSoup
https://velog.io/@neulhan/%EC%B4%88%EB%B3%B4%EB%8F%84-%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-python%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84%EC%97%90%EC%84%9C-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EA%B2%80%EC%83%89%EC%96%B4-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-2-BeautifulSoup-1uk4asqet0
"""
import requests
from bs4 import BeautifulSoup as bs
import os
from common import tuple_number, tuple_pattern, tuple0_imageFileDir


def get_card_url(number, pattern):
    home_url = 'https://commons.wikimedia.org/wiki/File:' + str(number) + str(pattern) + '.svg'
    html_text = requests.get(home_url).text
    soup_obj = bs(html_text, 'html.parser')
    tag = soup_obj.select_one('#file > div > span > a:nth-of-type(1)')
    url = tag['href'].replace('171', '2000')
    return url


def curl_url_fileName(url, fileName):
    """

    :rtype: None
    """
    os.system('curl ' + url + ' > ' + fileName)
    return


if __name__ == '__main__':
    os.system('mkdir ' + tuple0_imageFileDir[0])
    for pattern in tuple_pattern:
        for number in tuple_number:
            url = get_card_url(number, pattern)
            fileName = './' + str(tuple0_imageFileDir[0]) + '/' + str(number) + str(pattern) + '.png'
            curl_url_fileName(url, fileName)
