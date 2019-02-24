import os


SVN_ADDRESS = 'https://corp.youdao.com/svn/soft/codown/xue/course-app/apk'

CODOWN_ADDRESS = 'http://codown.youdao.com/xue/course-app/apk'

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVN_CHECKOUT_PATH = os.path.join(BASEDIR, 'files', 'svn')

VERSION = '3.2.0'

DOWNLOAD_PATH = [VERSION, 'market']

ALLWAYS_DOWNLOAD = ['youdao_course_official', 'banner-course-xuewap']
