from bs4 import BeautifulSoup
from flask_api import FlaskAPI
import json
import requests


app = FlaskAPI(__name__)


@app.route('/<path:site>')
def linkcheck(site):
    # page = ''.join(sys.argv[1:])

    # add formatter to add http:// if needed?
    page = 'http://' + site

    r = requests.get(page)

    data = r.text

    soup = BeautifulSoup(data, 'lxml')

    urls = []

    for a in soup.find_all('a'):
        urls.append(a.get('href'))

    url_responses = {}

    for url in urls:
        if url[0] == '/':
            print(url)
        if url[0] not in ('/', '#', 'm', 'j'):
            temp_r = requests.get(url)
            url_responses[url] = temp_r.status_code

    return url_responses


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
