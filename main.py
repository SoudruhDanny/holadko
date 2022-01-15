import socket
import oauthy
import logging
from time import sleep
import pyautogui
import keyboard
#asd
#Getting your credentials
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'jimyslave'
token = oauthy.oauth #test oauth
channel = '#jimysak'


def buyXP():
    pyautogui.press('F')
    sleep(0.06)


def rollShop():
    pyautogui.press('D')
    sleep(0.06)


def Shop():

    pyautogui.moveTo(586, 1009)
    pyautogui.leftClick()
    sleep(0.06)

    pyautogui.moveTo(779, 995)
    pyautogui.leftClick()
    sleep(0.06)

    pyautogui.moveTo(959, 993)
    pyautogui.leftClick()
    sleep(0.06)

    pyautogui.moveTo(1188, 1005)
    pyautogui.leftClick()
    sleep(0.06)

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
                buyXP()
            if "!rollShop" in resp:
                rollShop()
            if f"!buy {x}" in resp:
                Shop()


if __name__ == '__main__':
    main()
