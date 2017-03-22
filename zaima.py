#! /usr/local/bin/python3
# coding=utf-8
import requests
import time
import random
import datetime

# douyu API adderss
url = 'http://open.douyucdn.cn/api/RoomApi/room/'
roomNum = '3614'

# Quin luanguage
quinLanguage = [
    "摸了。",
    "秦先森已经歇了。",
    "什么？已经八点了？",
    "靠妖啊，秦先森又在吃香香鸡了。",
    "秦喵喵再不播我就要死了。",
    "zaima",
    "不在，cnm",
    "戳木娘啊，秦川又去哪里摸鱼了。",
    "你能表演一下那个吗？",
    "每天都在那里直播。",
    "狗才摸鱼。",
    "别问了，秦川这种生物不存在的。",
    "zaima？男娼堇业代表。",
    "怕不是要摸爆一切。",
    "怕不是要摸到时间的尽头。",
    "秦川什么时候来舞动青春啊。",
    "说不出话。"
]

# Quin name
quinName = [
    "秦川",
    "秦先森",
    "秦喵喵",
    "秦智障",
    "川川子",
    "鸡盒摸鱼王奎恩",
    "Quin",
    "缺",
    "缺哥哥",
    "缺神",
    "Q酱",
    "二五仔"
]

# get API return
# deal with the return data
try:
    r = requests.get(url + roomNum)
    r = r.json()
except requests.RequestException as e:
    print("网络出错了！怕不是没联网？\nError: %s" % e.message)
    exit()

roomError = r.get('error')

# now time
ntime = time.strftime('%Y%m%d', time.localtime(time.time()))
ntimeS = time.strftime('%H', time.localtime(time.time()))

# roomError == 0 then catch the right data
if roomError == 0:
    # catch the room data in returned JSON data
    roomData = r.get('data')
    quinName = random.choice(quinName)
    nonBS = 0

    # get the last play time
    btime = datetime.datetime.strptime(
        roomData.get('start_time'), '%Y-%m-%d %H:%M')
    # print(type(bitime))

    print("%s说：%s" % (quinName, roomData.get('room_name')))
    print()

    # not in play
    if roomData.get('room_status') == '2':
        # if 1:
        nonB = (datetime.datetime.now() - btime)
        bDays = nonB.days
        bHours = nonB.seconds / (3600)
        bMin = (bHours - int(bHours)) * 60
        bSec = (bMin - int(bMin)) * 60

        if not bDays:
            print("刚刚勃完，让%s歇一歇吧，不要猝死在直播间。" % quinName)
        else:
            print(quinName, "已经摸了", bDays, " 天", int(bHours),
                  "个小时", int(bMin), "分钟", int(bSec), "秒了。")
            print(random.choice(quinLanguage))
    elif roomData.get('room_status') == '1':
        print("惊了！")
        print(quinName, "居然播了，不敢信。")
        print("而且有", roomData.get('online'), "个猛男在看直播，整个房间都gay gay的。")
else:
    print("好神秘啊，怕不是进错房间了？")
