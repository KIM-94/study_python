from datetime import datetime

from notion.client import NotionClient
from notion.block import PageBlock, TextBlock, TodoBlock, BookmarkBlock, get_embed_link, BasicBlock

token_v2 = 'c876bd10bc2c600d076e0e998a0891c63f28eeaef24136d1ac20050effc2318e3394a0fb5a94c3a1bc142a69db3f081fb91e21357259176d364befd4ef0e606b6a4e5de903ef195622268b8f2545' # 준비물의 token_v2
client = NotionClient(token_v2=token_v2)

url = "https://www.notion.so/ksw2102/crowling-4992fd7197eb4d36954efed609689246"
page = client.get_block(url)

print("Page 제목은  :", page.title)

import os

files = os.listdir('playlist_txt/')

list = []
link = []
name = []

Lurl = []
# print(files)
for filename in files:
    if ".txt" not in filename:
        continue
    file = open('playlist_txt/' + filename, 'r', encoding='utf-8')
    new_page = page.children.add_new(PageBlock)
    new_page.title = '{}'.format(filename.split('.txt')[0])

    for i in file:
        title = i.split(' LINK ')[0]
        link = i.split(' LINK ')[1].strip()

        book1 = new_page.children.add_new(BookmarkBlock)
        book1.title = title
        book1.link = link
    file.close()


