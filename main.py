import hashlib
from os import walk

files = []
results = []
for (dirpath, dirnames, filenames) in walk("data"):
    files.extend(filenames)
    break


for file in files:
    with open("data/" + files[0], "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha3_256(bytes).hexdigest()
        result = readable_hash
        results.append(result)

results.sort()

print("nomonsalakhiddinov2002@gmail.com \n" + "".join(results))


