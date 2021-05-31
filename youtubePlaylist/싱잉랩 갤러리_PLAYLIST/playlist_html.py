from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

f = open('getvideosLINK.txt', 'r', encoding='utf-8')
list = []
for i in f:
    list.append(i)
f.close()


delay = 3
browser = Chrome()
browser.implicitly_wait(delay)
browser.maximize_window()

# for i in range(0, 2):
for i in range(3, len(list)):
    # time.sleep(5)
    title = list[i].split(' LINK ')[0]
    link = list[i].split(' LINK ')[1].strip()
    print(title, link)

    url = link
    browser.get(url)

    body = browser.find_element_by_tag_name('body')  # 스크롤하기 위해 소스 추출
    num_of_pagedowns = 1
    # 1번 밑으로 내리는 것
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        num_of_pagedowns -= 1
    # browser.find_element_by_css_selector('.more-button.style-scope.ytd-comment-renderer').click()
    browser.find_element_by_xpath(r'//paper-button[@id="more"]').click()
    # // *[ @ id = "more"] / span
    # // *[ @ id = "more"]
    # / html / body / ytd - app / div / ytd - page - manager / ytd - watch - flexy / div[4] / div[
    #     1] / div / ytd - comments / ytd - item - section - renderer / div[3] / ytd - comment - thread - renderer[
    #       1] / ytd - comment - renderer / div[1] / div[2] / ytd - expander / paper - button[2]
    html0 = browser.page_source
    soup = BeautifulSoup(html0, 'html.parser')
    f2 = open('playlist_html/'+title+'.html', 'w', encoding='utf-8')
    content = soup.find('ytd-page-manager', id='page-manager')
    f2.write(str(content))
    f2.close()
    # response = urlopen(url)
    # plain_text = response.read()
    # soup = BeautifulSoup(plain_text, 'html.parser')
    # print(soup.find('yt-formatted-string', class_='content style-scope ytd-video-secondary-info-renderer'))

    # for j in soup.find_all('span', class_='style-scope yt-formatted-string'):
    #     print(j)