#! /usr/local/bin/python3
# coding=utf-8
import requests
import random
import datetime


class zaima:

    # url
    # room
    # __res
    # error
    # __roomData
    # __quinName
    # __quinLanguage
    def __init__(self, url, room):
        self.url = url
        self.room = room
        try:
            self.__res = requests.get(self.url + self.roomNum).json()
            self.error = self.__res.get('error')
            self.__roomData = self.__res.get('data')
        except requests.RequestException as e:
            print("网络出错了！怕不是没联网？\nError: %s" % e.message)
            exit()

    # 计算播的时间数据，存入 dict 中
    def __bo_time(self):
        self.__boData = {}
        self.__boData['nonB'] = datetime.datetime.now() - \
            datetime.datetime.strptime(
                self.roomData.get('start_time'), '%Y-%m-%d %H:%M')
        self.__boData['days'] = self.__boData['nonB'].days
        self.__boData['hours'] = self.__boData['nonB'].seconds / (3600)
        self.__boData['min'] = (self.__boData['hours'] -
                                int(self.__boData['hours'])) * 60
        self.__boData['sec'] = (self.__boData['min'] -
                                int(self.__boData['min'])) * 60
        # return __boData

    def message_output(self):
        self.__quinLanguage = random.choice(
            open("./langs/quinLangs.dat", "r").readlines())
        self.__quinName = random.choice(
            open("./langs/quinName.dat", "r").readlines())
        # quinName = random.choice(quinName)
        if self.__roomData['room_status'] == '2':
            # if 1:
            self.__bo_time()
            # print(bo)
            if not self.__boData['days']:
                print("刚刚勃完，让%s歇一歇吧，不要猝死在直播间。" % quinName)
            else:
                print("%s已经摸了%s天%s个小时%s分钟%s秒了。" % (quinName, self.__boData[
                      'days'], self.__boData['hours'], self.__boData['min'], self.__boData['sec']))
                print(quinLanguage)
        elif self.__roomData['room_status'] == '1':
            print("惊了！")
            print(quinName, "居然播了，不敢信。")
            print("而且有", roomData.get('online'), "个猛男在看直播，整个房间都gay gay的。")


if __name__ == '__main__':
    # douyu API adderss
    url = 'http://open.douyucdn.cn/api/RoomApi/room/'
    roomNum = '3614'
    zaima = new zaima(url, room)
    if !zaima.error:
        zaima.message_output()
    else:
        print("好神秘啊，怕不是进错房间了？")

# get API return
# deal with the return data
# try:
#     r = requests.get(url + roomNum)
#     r = r.json()
# except requests.RequestException as e:
#     print("网络出错了！怕不是没联网？\nError: %s" % e.message)
#     exit()
#
# # roomError == 0 then catch the right data
# if r.get('error') == 0:
#     # catch the room data in returned JSON data
#     quinLanguage = open("./langs/quinLangs.dat", "r").readlines()
#     quinName = open("./langs/quinName.dat", "r").readlines()
#     quinName = random.choice(quinName)
#     roomData = r.get('data')
#
#     print("%s说：%s" % (quinName, roomData.get('room_name')))
#     print()
#
#     # not in play
#     if roomData.get('room_status') == '2':
#         # if 1:
#         bo = bo_time(roomData)
#         # print(bo)
#
#         if not bo['days']:
#             print("刚刚勃完，让%s歇一歇吧，不要猝死在直播间。" % quinName)
#         else:
#             print(quinName, "已经摸了", bo['days'], " 天", int(bo['hours']),
#                   "个小时", int(bo['min']), "分钟", int(bo['sec']), "秒了。")
#             print(random.choice(quinLanguage))
#     elif roomData.get('room_status') == '1':
#         print("惊了！")
#         print(quinName, "居然播了，不敢信。")
#         print("而且有", roomData.get('online'), "个猛男在看直播，整个房间都gay gay的。")
# else:
#     print("好神秘啊，怕不是进错房间了？")
