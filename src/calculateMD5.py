import hashlib
import os

from conf.config import SVN_PATH

files = []
for hierarchy in os.walk(SVN_PATH):
    if hierarchy[-1]:
        for file in hierarchy[-1]:
            files.append(os.path.join(hierarchy[0], file))
print(len(files), files)

results = {}
for file in files:
    m = hashlib.md5()
    with open(file, 'rb') as fp:
        while True:
            data = fp.read(1024)
            if not data:
                break
            m.update(data)
    results[file] = m.hexdigest()
print(results)

results_set = set([i for i in results.items()])

print(results_set)
