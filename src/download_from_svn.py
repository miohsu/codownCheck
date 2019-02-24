import svn.remote, os

from conf.config import SVN_ADDRESS, DOWNLOAD_PATH, SVN_CHECKOUT_PATH, ALLWAYS_DOWNLOAD

r = svn.remote.RemoteClient('/'.join([SVN_ADDRESS, DOWNLOAD_PATH[0]]))
r.checkout(SVN_CHECKOUT_PATH)

c = svn.remote.RemoteClient(SVN_ADDRESS)
content = c.cat(ALLWAYS_DOWNLOAD[0])
with open(os.path.join(SVN_CHECKOUT_PATH, ALLWAYS_DOWNLOAD[0]), 'wb') as f:
    f.write(content)
