from bs4 import BeautifulSoup
from flask.json import jsonify
import requests
import json
import urllib.parse
from random import randint


class Scraper:
    def get_movie_by_id(self, id):
        pass

    def get_movie_id_by_title(self, title):

        query = urllib.parse.quote_plus(title)

        response = {
            'Error': "Something went wrong! Please make sure the movie name is correct."}

        headers = {
            'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }

        html = requests.get(
            f'https://www.google.com/search?q=imdb+{query}', headers=headers).text

        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='tF2Cxc')

        title = container.find('h3', class_='LC20lb DKV0Md').text
        # article_summary = container.find('span', class_='aCOpRe').text
        link = container.find('a')['href']

        if 'imdb.com/title/tt' in link:
            response = {
                'title': title,
                # 'Article Summary': article_summary,
                'link': link,
            }

        return json.dumps(response, indent=2, ensure_ascii=False)

    def pick_random(self):
        return jsonify({'id': f"tt{randint(int('00000001'), 99999999)}"})


if __name__ == '__main__':
    scraper = Scraper()
    scraper.get_movie_id_by_title(title='something')
