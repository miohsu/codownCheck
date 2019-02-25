from lib.downloader import FileDownloader, PathDownloader


def file_down(urls, path):
    print("Start down {}".format(urls))
    for url in urls:
        fdl = FileDownloader(url, path)
        fdl.download()


def path_down(urls, path):
    print("Start down from {}".format(urls))
    for url in urls:
        pdl = PathDownloader(url, path)
        pdl.download()


def get_urls(base_url, suffix_urls):
    return ['/'.join([base_url.rstrip('/'), suffix]) for suffix in suffix_urls]
