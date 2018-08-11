#!/usr/bin/python3.3
import errno
import os
import urllib.request

try:
    os.mkdir('artwork')
    os.mkdir('logo-mono')
    os.mkdir('logo-color')
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

artwork = open('artwork.txt', 'r')
for link in artwork:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join('artwork', name)

    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')
artwork.close()

logos = open('logo-mono.txt', 'r')
for link in logos:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join('logo-mono', name)
    filename2 = os.path.join('logo-color', name.replace("-mono-", "-"))
	
    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')


    if not os.path.isfile(filename2):
        print('Downloading: ' + filename2)
        try:
            urllib.request.urlretrieve(link.replace("-mono-", "-"), filename2)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')
            
logos.close();
