import socket
import oauthy
import logging
from time import sleep
import pyautogui
import keyboard
import re

#
#Getting your credentials
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'jimyslave'
token = oauthy.oauth #test oauth
channel = '#jimysak'

hex_map = {
    1: "x=549, y=446",
    2: "x=681, y=444",
    3: "x=792, y=448",
    4: "x=908, y=445",
    5: "x=1020, y=446",
    6: "x=1142, y=445",
    7: "x=1255, y=448",
    8: "x=598, y=520",
    9: "x=718, y=519",
    10: "x=838, y=512",
    11: "x=972, y=513",
    12: "x=1074, y=522",
    13: "x=1214, y=520",
    14: "x=1324, y=520",
    15: "x=547, y=593",
    16: "x=662, y=595",
    17: "x=782, y=588",
    18: "x=897, y=585",
    19: "x=1026, y=593",
    20: "x=1153, y=593",
    21: "x=1273, y=598",
    22: "x=587, y=676",
    23: "x=683, y=670",
    24: "x=823, y=675",
    25: "x=961, y=683",
    26: "x=1084, y=672",
    27: "x=1222, y=678",
    28: "x=1337, y=678"
}

board_map = {
    1: "x=433, y=787",
    2: "x=546, y=784",
    3: "x=655, y=789",
    4: "x=771, y=788",
    5: "x=889, y=787",
    6: "x=1012, y=782",
    7: "x=1129, y=785",
    8: "x=1254, y=784",
    9: "x=1356, y=780"
}

item_map = {
    1: "x=253, y=809",
    2: "x=295, y=771",
    3: "x=278, y=741",
    4: "x=312, y=720",
    5: "x=294, y=673",
    6: "x=304, y=646",
    7: "x=372, y=656",
    8: "x=356, y=684",
    9: "x=366, y=715",
    10: "x=414, y=683"
}

def buy_xp():
    pyautogui.press('F')
    sleep(0.06)


def roll_shop():
    pyautogui.press('D')
    sleep(0.06)


def shop(value: int):
    print(value)

    if value == 1:
        pyautogui.moveTo(586, 1009)
        pyautogui.leftClick()
        sleep(0.06)

    if value == 2:
        pyautogui.moveTo(779, 995)
        pyautogui.leftClick()
        sleep(0.06)

    if value == 3:
        pyautogui.moveTo(959, 993)
        pyautogui.leftClick()
        sleep(0.06)

    if value == 4:
        pyautogui.moveTo(1188, 1005)
        pyautogui.leftClick()
        sleep(0.06)

    if value == 5:
        pyautogui.moveTo(1357, 999)
        pyautogui.leftClick()
        sleep(0.06)


def main():
    # Connecting to Twitch with sockets
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    # Receiving channel messages
    resp = sock.recv(2048).decode('utf-8')
    logging.info(resp)

    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            print(resp)
            if "!buyXP" in resp:
                buy_xp()

            if "!rollShop" in resp:
                roll_shop()

            if "!buy" in resp:
                raw_value = re.search(r'\d', resp)
                value = raw_value.group()
                if int(value) in range(1, 6):
                    shop(int(value))

            if "!moveChamp" in resp:
                raw_value = re.search(r'\d{1,2}', resp)
                value = raw_value.groups()
                print(value)




if __name__ == '__main__':
    main()
