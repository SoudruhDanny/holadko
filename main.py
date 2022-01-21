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
    1: (335, 597),
    2: (391, 599),
    3: (326, 640),
    4: (382, 638),
    5: (438, 638),
    6: (347, 668),
    7: (403, 666),
    8: (308, 695),
    9: (331, 729),
    10: (290, 757)
}

item_move = {
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
    28: (1337, 676),
    29: (433, 787),
    30: (546, 787),
    31: (655, 787),
    32: (771, 787),
    33: (889, 787),
    34: (1012, 787),
    35: (1129, 787),
    36: (1254, 787),
    37: (1356, 787)
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
    pyautogui.moveTo(365, 970)
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')


def roll_shop():
    pyautogui.moveTo(365, 1031)
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
    pyautogui.moveTo(deck_map[int(deck)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(959, 993)
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')

def move(board1, board2):
    pyautogui.moveTo(board_map[int(board1)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(board_map[int(board2)])
    sleep(.050)
    pyautogui.mouseUp(button='left')
    print('Done')

def moveItem(item, number):
    pyautogui.moveTo(item_map[int(item)])
    sleep(.050)
    pyautogui.mouseDown(button='left')
    sleep(.050)
    pyautogui.moveTo(item_move[int(number)])
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

                if '!item' in resp:
                    raw_value = re.findall(r'\s\d{1,2}', resp)
                    item = raw_value[0]
                    position = raw_value[1]
                    moveItem(item, position)

    except Exception as exception:
        print(exception)
        main()


if __name__ == '__main__':
    main()
