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


def download_card_image(whether_overwrite=False):
    if not os.path.isdir(tuple0_imageFileDir[0]):
        os.system('mkdir ' + tuple0_imageFileDir[0])

    for pattern in tuple_pattern:
        for number in tuple_number:
            file_name = './' + str(tuple0_imageFileDir[0]) + '/' + str(number) + str(pattern) + '.png'
            if os.path.isfile(file_name):
                if not whether_overwrite:
                    continue
            url = get_card_url(number, pattern)
            os.system('curl ' + url + ' > ' + file_name)


if __name__ == '__main__':
    download_card_image()

"""
ref

curl
https://soyoung-new-challenge.tistory.com/92

BeautifulSoup, requests
https://velog.io/@neulhan/%EC%B4%88%EB%B3%B4%EB%8F%84-%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-python%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84%EC%97%90%EC%84%9C-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EA%B2%80%EC%83%89%EC%96%B4-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-2-BeautifulSoup-1uk4asqet0
get href
https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
css selector // tr:nth ->nth-of-type
https://mjdeeplearning.tistory.com/46

check a file exists
https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
"""
