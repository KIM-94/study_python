import pandas as pd
import os

# path = 'C:/Users/KIM/PycharmProjects/crawlingNotion/portfolio/youtubePlaylist/channel2/'
# filepath = 'C:/Users/KIM/PycharmProjects/crawlingNotion/portfolio/youtubePlaylist/channel/channelList2.xlsx'

# /Users/sungwookim/PycharmProjects/crawlingNotion/portfolio/youtubePlaylist

path = '/Users/sungwookim/PycharmProjects/crawlingNotion/portfolio/youtubePlaylist/channel2/'
filepath = '/Users/sungwookim/PycharmProjects/crawlingNotion/portfolio/youtubePlaylist/channel/channelList2.xlsx'


def showList():
    # path = 'C:/Users/KIM/PycharmProjects/crawlingNotion/stock'
    # path_xlsx = 'C:/Users/KIM/Desktop/공공데이터 취업박랍회/xlsx/'
    list = []
    files = os.listdir(path)
    count = 0
    for index, filename in enumerate(files):
        if ".xlsx" not in filename:
            continue
        print(count, filename)
        count = count+1
        list.append(filename)
    return list

def readFile(FILN):
    # search = input('파일을 선택하세요')
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    # FILN = path+file[int(search)]
    # FILN = filepath

    print(FILN)
    xlsx = pd.read_excel(path+FILN)
    # print(xlsx)

    플레이리스트명 = xlsx['플레이리스트명'].values
    영상주소 = xlsx['영상주소'].values
    영상길이 = xlsx['영상길이'].values
    try:
        조회수 = xlsx['조회수'].values
        등록일 = xlsx['등록일'].values
    except KeyError:
        조회수 = "-"
        등록일 = "-"
    데이터기준일자 = xlsx['데이터기준일자'].values

    for i in 조회수:
        print(i)

    # # print(채널명)
    # 조회수1 = []
    # for i in 조회수:
    #     # print(str(i))
    #     if str(i) == "nan":
    #         temp = "0"
    #     else:
    #         try:
    #             temp = str(i).split("구독자 ")[1].split("만명")[0]
    #             temp = int(float(temp) * 10000)
    #         except ValueError:
    #             try:
    #                 temp = str(i).split("구독자 ")[1].split("천명")[0]
    #                 temp = int(float(temp) * 1000)
    #             except ValueError:
    #                 temp = str(i).split("구독자 ")[1].split("명")[0]
    #                 temp = int(float(temp))
    #         # temp2 = str(i).split("구독자 ")[1].split("천명")[0]
    #         # temp2 = temp2 * 1000
    #         # temp = str(i).split("구독자 ")[1].split("명")[0]
    #         # temp = temp.split("만명")[0]
    #         # temp = temp * 10000
    #         # try:
    #         #     temp = temp.split("만명")[0]
    #         #     temp = temp * 10000
    #         # except:
    #         #     temp
    #     구독자1.append(temp)
    #     # print(temp)
    # # for i in 구독자1:
    # #     print(i)
    # sql = "INSERT INTO `channel` (`ch_name`, `sub_num`, `video_num`, `ch_url`, `datetime`) VALUES"
    # print(sql)
    # for i in range(0, len(채널명)):
    #     # print(채널명[i], 구독자1[i], 영상개수[i], 채널주소[i], 데이터기준일자[i])
    #     if i < len(채널명)-1:
    #         print("("+"'"+채널명[i].replace("\'", "\\'")+"',"+str(구독자1[i])+","+str(영상개수[i])+","+"'"+채널주소[i]+"',"+"'"+str(데이터기준일자[i])+"'"+"),")
    #     else:
    #         print("(" + "'" + 채널명[i] + "'," + str(구독자1[i]) + "," + str(영상개수[i]) + "," + "'" + 채널주소[i] + "'," + "'" + str(데이터기준일자[i]) + "'" + ");")

    # contents = xlsx['신문사'].values, xlsx['link'].values, xlsx['제목'].values, xlsx['데이터기준일자'].values
    #
    # row = []
    # title_list = []
    # for i in contents[2]:  
    #     data_set = str(i).split(' ')
    #     # print(str(i).split(' '))
    #     for j in data_set:
    #         # print(j) 
    #         data_set_level2 = str(re.sub('[\]\[.?\"\'·-‘-↑↓`“…]', ' ', j)).split(' ')
    #         for k in data_set_level2:
    #             title_list.append(k)
    #         row.append(j)
    #     for j in data_set:
    #         # print(j)
    #         row.append(j)
    #
    # # 기업별 공고 개수
    # result = Counter(title_list)
    # COMPANNY_SET = set(title_list)
    # # print(result)
    #
    # y = OrderedDict(result.most_common())
    # # print(y)
    # for i in y:
    #     print(i, result[i])
    # print(len(result))

filelist = showList()
for i in range(0, len(filelist)):
    readFile(filelist[i])