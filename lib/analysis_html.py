from bs4 import BeautifulSoup


class Analysis(object):
    def __init__(self, html):
        self.html = html

    def get_a_href(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        return [link.get('href') for link in soup.find_all('a') if link.get('href') not in ['../', './']]
