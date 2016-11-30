#! /usr/bin/env python
# -*- coding: utf-8 -*-
import optparse, json, requests, time, random, yaml
url = 'http://open.douyucdn.cn/api/RoomApi/room/'
roomNum = '3614'

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
"Q酱"
]

r = requests.get(url+roomNum)
r = r.json()
r = json.dumps(r)
r = yaml.safe_load(r)

roomError = r.get('error')
ntime = time.strftime('%Y%m%d',time.localtime(time.time()))
ntimeS = time.strftime('%H',time.localtime(time.time()))

if roomError == 0:
    roomData = r.get('data')
    quinName = random.choice(quinName)

    print "%s说：%s" % (quinName, roomData.get('room_name').encode('utf-8'))
    print
    if roomData.get('room_status') == '2':
        nonB = int(ntime)-int(roomData.get('start_time').encode('utf-8')[0:10].replace('-', ''))
        nonBS = 24-int(roomData.get('start_time').encode('utf-8')[11:13])+int(ntimeS)
        if nonB == 1 and nonBS <= 24:
            print "让秦先生歇一歇吧，不要猝死在直播间。"
        else:
            print quinName, "已经摸了", nonB, " 天了。"
            print random.choice(quinLanguage)
    elif roomData.get('room_status') == '1':
        print "惊了！"
        print quinName, "居然播了，不敢信。"
        print "而且有", roomData.get('online'), "个猛男在看直播，整个房间都gay gay的。"
else:
    print("好神秘啊，怕不是进错房间了？")
