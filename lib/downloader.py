import requests, os

from conf import config
from lib.analysis_html import Analysis


class Downloader(object):
    def __init__(self, url, storge_path):
        self.url = url
        self.storge_path = storge_path

    def download(self):
        # download the file
        pass


class FileDownloader(Downloader):
    def download(self):
        # download the file
        response = requests.get(self.url, stream=True)
        storge_file = os.path.join(self.storge_path, self.url.split('/')[-1])
        with open(storge_file, 'wb') as fp:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    fp.write(chunk)


class PathDownloader(Downloader):
    def __init__(self, *args):
        super().__init__(*args)
        self.storge_path = os.path.join(self.storge_path, self.url.rstrip('/').split('/')[-1])
        if not self.url.endswith('/'):
            self.url = self.url + '/'

    def download(self):
        # download from path
        html = requests.get(self.url).content.decode('utf8')
        analysis = Analysis(html)
        filenames = analysis.get_a_href()
        print("{} contain {}".format(self.url, filenames))

        try:
            if not os.path.exists(self.storge_path):
                os.mkdir(self.storge_path)
            elif not os.path.isdir(self.storge_path):
                raise NameError("Error: '{}' is exists, but is not a dir.".format(self.storge_path))
        except NameError as e:
            print(e)
            return

        for file in filenames:
            url_file = '/'.join([self.url.rstrip('/'), file])
            print('Start Download {}'.format(url_file))
            fd = FileDownloader(url_file, self.storge_path)
            fd.download()


if __name__ == '__main__':
    BASEDIR = config.BASEDIR
    # url = 'https://cdn.staticfile.org/vue/2.2.2/vue.min.js'
    storge_path = os.path.join(BASEDIR, 'files', 'svn')
    # fdl = FileDownloader(url, storge_path)
    # fdl.download()

    url_path = 'https://mirrors.aliyun.com/centos/dostools'

    pdl = PathDownloader(url_path, storge_path)
    pdl.download()
