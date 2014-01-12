import json
import os
import urllib
from urllib.request import urlopen

# GET JSON file and convert to Unicode
response = urlopen('https://s3.amazonaws.com/Minecraft.Download/indexes/legacy.json')
encoding = response.info().get_param('charset', 'utf-8')

# Convert output to dictionary
data = json.loads(response.read().decode(encoding))

os.mkdir('assets')
os.chdir('assets')
'''
os.mkdir('icons')
os.mkdir('lang')
os.mkdir('music')
os.mkdir('records')
os.mkdir('sound\ambient\cave')
os.mkdir('sound\ambient\weather')
os.mkdir('sound\damage')
os.mkdir('sound\dig')
os.mkdir('sound\fire')
os.mkdir('sound\fireworks')
os.mkdir('sound\liquid')
os.mkdir('sound\minecart')
os.mkdir('sound\note')
os.mkdir('sound\portal')
os.mkdir('sound\random')
os.mkdir('sound\step')
os.mkdir('sound\tile\piston')
'''


for name, info in data['objects'].items():
    filehash = info['hash']
    limithash = filehash[:2]

    url = 'http://resources.download.minecraft.net/' + limithash + '/' + filehash

    folder = os.path.dirname(name)
    if not os.path.isdir(folder):
        os.makedirs(folder)

    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Perspective/0.1')  

    download = urllib.request.urlopen(request)
    with open(name, 'b+w') as f:
        f.write(download.read())

    print(name + ' has been downloaded')
    