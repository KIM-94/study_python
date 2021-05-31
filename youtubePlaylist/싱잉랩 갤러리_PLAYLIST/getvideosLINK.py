from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'file:///C:/Users/KIM/PycharmProjects/crawlingNotion/creatPlaylist/싱잉랩 갤러리_PLAYLIST/videosLINK.html'
response = urlopen(url)
plain_text = response.read()
soup = BeautifulSoup(plain_text, 'html.parser')
# print(soup)
f = open('getvideosLINK.txt', 'w', encoding='utf-8')
for i in soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer'):
    print(i.attrs['title']+' LINK '+'https://www.youtube.com'+i.attrs['href'])
    f.write(i.attrs['title']+' LINK '+'https://www.youtube.com'+i.attrs['href']+'\n')
f.close()