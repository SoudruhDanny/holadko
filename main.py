import socket
import oauthy
import logging
from time import sleep
import pyautogui
import keyboard
import re
from operator import methodcaller
from pynput.keyboard import Key, Controller

KEYBOARD = Controller()


#
#Getting your credentials
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'jimyslave'
token = oauthy.oauth #test oauth
channel = '#jimysak'

board_map = {
    1: (549, 446),
    2: (681, 446),
    3: (792, 446),
    4: (908, 446),
    5: (1020, 446),
    6: (1142, 446),
    7: (1255, 446),
    8: (598, 520),
    9: (718, 520),
    10: (838, 520),
    11: (972, 520),
    12: (1074, 520),
    13: (1214, 520),
    14: (1324, 520),
    15: (547, 593),
    16: (662, 593),
    17: (782, 593),
    18: (897, 593),
    19: (1026, 593),
    20: (1153, 593),
    21: (1273, 593),
    22: (587, 676),
    23: (683, 676),
    24: (823, 676),
    25: (961, 676),
    26: (1084, 676),
    27: (1222, 676),
    28: (1337, 676)
}

deck_map = {
    1: (433, 787),
    2: (546, 787),
    3: (655, 787),
    4: (771, 787),
    5: (889, 787),
    6: (1012, 787),
    7: (1129, 787),
    8: (1254, 787),
    9: (1356, 787)
}

item_map = {
    1: (253, 809),
    2: (295, 771),
    3: (278, 741),
    4: (312, 720),
    5: (294, 673),
    6: (304, 646),
    7: (372, 656),
    8: (356, 684),
    9: (366, 715),
    10: (414, 683)
}


def augment(value):
    if value == 1:
        pyautogui.moveTo(603, 519)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 2:
        pyautogui.moveTo(940, 505)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 3:
        pyautogui.moveTo(1332, 531)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)


def move_champion_to(deck, board):
    pyautogui.moveTo(deck_map[int(deck)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(board_map[int(board)])
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def lock_shop():
    pyautogui.moveTo(1450, 904)
    sleep(0.05)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def move_champion_from(deck, board):
    pyautogui.moveTo(board_map[int(board)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(deck_map[int(deck)])
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def buy_xp():
    pyautogui.moveTo()
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def roll_shop():
    pyautogui.moveTo()
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def shop(value: int):
    if value == 1:
        pyautogui.moveTo(586, 1009)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 2:
        pyautogui.moveTo(779, 995)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 3:
        pyautogui.moveTo(959, 993)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 4:
        pyautogui.moveTo(1188, 1005)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

    if value == 5:
        pyautogui.moveTo(1357, 999)
        sleep(.06)
        pyautogui.mouseDown(button='left')
        sleep(.02)
        pyautogui.mouseUp(button='left')
        sleep(0.06)

def sell(deck):
    pyautogui.moveTo(board_map[int(deck)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(1332, 531)
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')

def move(board1, board2):
    pyautogui.moveTo(board_map[int(board1)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(deck_map[int(board2)])
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')

def main():
    try:
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

                if "!aug" in resp:
                    raw_value = re.search(r'\s\d', resp)
                    value = raw_value.group()
                    if int(value) in range(1, 4):
                        augment(int(value))

                if "!lock" in resp:
                    lock_shop()

                if "!XP" in resp:
                    buy_xp()

                if "!rollShop" in resp:
                    roll_shop()

                if "!buy" in resp:
                    raw_value = re.search(r'\s\d', resp)
                    value = raw_value.group()
                    if int(value) in range(1, 6):
                        shop(int(value))

                if "!toBoard" in resp:
                    raw_value = re.findall(r'\s\d{1,2}', resp)
                    deck = raw_value[0]
                    board = raw_value[1]
                    move_champion_to(int(deck), int(board))

                if '!toDeck' in resp:
                    raw_value = re.findall(r'\s\d{1,2}', resp)
                    deck = raw_value[1]
                    board = raw_value[0]
                    move_champion_from(int(deck), int(board))

                if '!sell' in resp:
                    raw_value = re.search(r'\s\d', resp)
                    value = raw_value.group()
                    if int(value) in range(1, 10):
                        sell(int(value))

                if '!move' in resp:
                    raw_value = re.findall(r'\s\d{1,2}', resp)
                    board1 = raw_value[0]
                    board2 = raw_value[1]
                    move(board1, board2)

    except Exception as exception:
        print(exception)
        main()


if __name__ == '__main__':
    main()
