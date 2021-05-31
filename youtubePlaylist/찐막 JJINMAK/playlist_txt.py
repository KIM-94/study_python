from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re

files = os.listdir('playlist_html/')
list = []
link = []
name = []

Lurl = []
print(files)
for filename in files:
    if ".html" not in filename:
        continue
    url = 'file:///C:/Users/KIM/PycharmProjects/crawlingNotion/creatPlaylist/찐막 JJINMAK/playlist_html/'+filename
    print(url)
    txtname = filename
    txtname = txtname.split('.html')[0]
    txtfile = open('playlist_txt2/'+txtname+'.txt', 'w', encoding='utf-8')
    response = urlopen(url)
    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')
    # print(soup.find('yt-formatted-string', class_='content style-scope ytd-video-secondary-info-renderer'))
    title = []
    link = []
    # print(soup.select('ytd-comment-thread-renderer > ytd-comment-renderer > div > div > ytd-expander > div > yt-formatted-string')[1])
    for i in soup.select('ytd-comment-thread-renderer > ytd-comment-renderer > div > div > ytd-expander > div > yt-formatted-string')[1].find_all('span'):
        if str(i.text).strip() == '':
            continue
        print(str(i.text).strip())
        parse = re.sub('[l|]', '', str(i.text).strip())
        title.append(str(parse).lstrip())
    print('------------')
    for i in soup.select('ytd-comment-thread-renderer > ytd-comment-renderer > div > div > ytd-expander > div > yt-formatted-string')[1].find_all('a'):
        if str(i.text).strip() == '':
            continue
        if str(i.attrs["href"]).strip()[0:4] == '/wat':
            print(str(i.attrs["href"]).strip())
            link.append(str(i.attrs["href"]).strip())

    writedata = []
    for i in range(0, len(link)):
        # print(title[i+4], link[i+1])
        writedata.append(title[i+4]+' LINK '+'https://www.youtube.com'+link[i])
    print('//////////////////')
    for i in range(1, len(writedata)):
        print(writedata[i])
        txtfile.write(writedata[i]+'\n')
    print('//////////////////')
    txtfile.close()
    # for i in soup.find('yt-formatted-string', class_='style-scope ytd-comment-renderer').find_all('a', class_='yt-simple-endpoint style-scope yt-formatted-string'):
    #     if str(i.attrs["href"]) == '':
    #         continue
    #     if str(i.attrs["href"])[0:4] == '/wat':
    #         print(str(i.attrs["href"]).strip())
    #         link.append('https://www.youtube.com'+str(i.attrs["href"]).strip())
    # print(len(title), len(link))
    #
    # for i in range(0, len(title)):
    #     try:
    #         print(title[i]+' LINK '+link[i])
    #         txtfile.write(title[i]+' LINK '+link[i]+'\n')
    #     except IndexError:
    #         print('list index out of range')
    # txtfile.close()
