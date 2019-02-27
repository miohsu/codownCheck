import os, shutil
from src import download, calculateMD5
from conf.config import SVN_ADDRESS, DOWNLOAD_PATH, DOWNLOAD_FILE, SVN_PATH, CODOWN_ADDRESS, CODOWN_PATH


def down(base_url, suffix_urls, storge_path, type):
    if type in ['path_down', 'file_down']:
        downloader = getattr(download, type)
    else:
        print("Error: Type not in ['file', 'path']!")
        return
    urls = download.get_urls(base_url, suffix_urls)
    downloader(urls, storge_path)


def clear(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def main():
    clear(SVN_PATH)
    clear(CODOWN_PATH)

    down(base_url=SVN_ADDRESS, suffix_urls=DOWNLOAD_FILE, storge_path=SVN_PATH, type='file_down')
    down(base_url=SVN_ADDRESS, suffix_urls=DOWNLOAD_PATH, storge_path=SVN_PATH, type='path_down')
    down(base_url=CODOWN_ADDRESS, suffix_urls=DOWNLOAD_FILE, storge_path=CODOWN_PATH, type='file_down')
    down(base_url=CODOWN_ADDRESS, suffix_urls=DOWNLOAD_PATH, storge_path=CODOWN_PATH, type='path_down')

    calculateMD5.calculate(SVN_PATH, CODOWN_PATH)


if __name__ == '__main__':
    main()
