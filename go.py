#coding:utf-8

import uiautomator2 as u2
from time import sleep
import itchat
import importlib,sys
importlib.reload(sys)


# connect to device by wifi
d = u2.connect('192.168.2.104')


# 手机解锁
def unlock():
    # 滑动ing
    d.swipe_ext("up", 1.0)
    # d.swipe(0.412, 0.926, 0.412, 0.226)
    # 输入解锁密码
    d(text='4').click()
    d(text='4').click()
    d(text='4').click()
    d(text='4').click()


# 打卡操作
def goWork():
    # 启动企业微信 （adb shell -> pm list package -f | grep 'tencent'）
    d.app_start("com.tencent.wework")
    # d.click(0.824, 0.386)
    print('启动企业微信')
    # 沉睡ing
    sleep(4)
    # 进入工作台
    d.click(0.626, 0.962)
    print('进入工作台')
    # 沉睡ing
    sleep(1)
    # 滑动ing
    d.swipe_ext("up", 0.9)
    # d.swipe(0.504, 0.786, 0.504, 0.358)
    # 沉睡ing
    sleep(1)
    # 进入打卡页面
    d(text='打卡').click()
    print('进入打卡页面')
    # 沉睡ing
    sleep(1.5)
    # 拍照打卡
    d(text='拍照打卡').click()
    print('拍照打卡')
    # 沉睡ing
    sleep(1.5)
    # 拍照
    d.click(0.506, 0.938)
    # 沉睡ing
    sleep(1.5)
    # 打卡
    d.click(0.484, 0.95)
    print('打卡成功')
    # 关闭企业微信
    # d.app_clear("com.tencent.wework")


# 发送群聊消息
def SendChatRoomsMsg(gname,context):
    # 获取群组所有的相关信息（注意最好群聊保存到通讯录）
    myroom = itchat.get_chatrooms(update=True)
    # 传入指定群名进行搜索，之所以搜索，是因为群员的名称信息也在里面
    myroom = itchat.search_chatrooms(name=gname)
    for room in myroom:
        # 遍历所有NickName为键值的信息进行匹配群名
        if room['NickName'] == gname:
            username = room['UserName']
            # 得到群名的唯一标识，进行信息发送
            itchat.send_msg(context,username)
        else:
            print('No groups found')


# 主函数
if __name__ == '__main__':
    screen = d.info
    if(screen["screenOn"] == True):
        goWork()
    else:
        d.screen_on()
        print('手机亮屏')
        unlock()
        goWork()