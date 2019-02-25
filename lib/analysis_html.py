from bs4 import BeautifulSoup


class Analysis(object):
    def __init__(self, html):
        self.html = html

    def get_a_href(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        result = [link.get('href') for link in soup.find_all('a') if not link.get('href').endswith('/')]
        result = [i for i in result if not i.startswith('?')]
        return result
