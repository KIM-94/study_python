from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

files = os.listdir('playlist_html/')
list = []
link = []
name = []

Lurl = []
print(files)
for filename in files:
    if ".html" not in filename:
        continue
    url = 'file:///C:/Users/KIM/PycharmProjects/crawlingNotion/creatPlaylist/싱잉랩 갤러리_PLAYLIST/playlist_html/'+filename
    txtname = filename.split('.html')[0]
    txtfile = open('playlist_txt/'+txtname+'.txt', 'w', encoding='utf-8')
    response = urlopen(url)
    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')
    # print(soup.find('yt-formatted-string', class_='content style-scope ytd-video-secondary-info-renderer'))
    title = []
    link = []
    for i in soup.find('yt-formatted-string', class_='content style-scope ytd-video-secondary-info-renderer').find_all('span', class_='style-scope yt-formatted-string'):
        if str(i.text).strip() == '':
            continue
        print(str(i.text).strip())
        title.append(str(i.text).strip())
    for i in soup.find('yt-formatted-string', class_='content style-scope ytd-video-secondary-info-renderer').find_all('a', class_='yt-simple-endpoint style-scope yt-formatted-string'):
        if str(i.attrs["href"]) == '':
            continue
        if str(i.attrs["href"])[0:4] == '/wat':
            print(str(i.attrs["href"]).strip())
            link.append('https://www.youtube.com'+str(i.attrs["href"]).strip())
    print(len(title), len(link))

    for i in range(0, len(title)):
        try:
            print(title[i]+' LINK '+link[i])
            txtfile.write(title[i]+' LINK '+link[i]+'\n')
        except IndexError:
            print('list index out of range')
    txtfile.close()
