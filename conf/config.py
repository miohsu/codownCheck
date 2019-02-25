import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SVN_ADDRESS = 'https://corp.youdao.com/svn/soft/codown/xue/course-app/apk'
SVN_ADDRESS = 'http://192.168.1.72/repo'

CODOWN_ADDRESS = 'http://codown.youdao.com/xue/course-app/apk'

SVN_PATH = os.path.join(BASEDIR, 'files', 'svn')

VERSION = '3.2.0'

# DOWNLOAD_PATH = [VERSION, 'market']
DOWNLOAD_PATH = ['images', 'repodata']

# DOWNLOAD_FILE = ['youdao_course_official', 'banner-course-xuewap']
DOWNLOAD_FILE = ['EULA', 'GPL']
