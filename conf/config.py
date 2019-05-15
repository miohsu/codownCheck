import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SVN_ADDRESS = 'https://corp.youdao.com/svn/soft/codown/xue/course-app/apk'

CODOWN_ADDRESS = 'http://codown.youdao.com/xue/course-app/apk'

SVN_PATH = os.path.join(BASEDIR, 'files', 'svn')
CODOWN_PATH = os.path.join(BASEDIR, 'files', 'codown')

VERSION = '3.2.0'

DOWNLOAD_PATH = [VERSION, 'market']

DOWNLOAD_FILE = ['youdao_course_official', 'banner-course-xuewap']
