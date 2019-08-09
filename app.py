from __future__ import print_function

import logging
log = logging.getLogger('main')

import os
import sys
import time
import string
import struct
import binascii

sys.path.insert(1, os.path.split(sys.path[0])[0])
from cli import CommandLineInterface

import nfc
import nfc.ndef
import nfc.clf

from nfc_super_mario_real_life import db_util, sound_util, led_util

### Configs ###
COIN_SOUND = 'coin'
BRICK_SOUND = 'brick'
db = db_util.db


def main():
    while True:
        poll()
        time.sleep(1)


def poll():
    
    clf = nfc.ContactlessFrontend('tty:AMA0:pn532')
    print("Please touch a tag to get a new coin")

    led_util.prepare_led_gpio()

    tag = clf.connect(rdwr={'on-connect': connected})
    uid_tag = binascii.hexlify(tag.identifier)
    coin_tag = getCoin(tag)
    print(int(coin_tag))

    new_coin = connect_mysql(uid_tag, coin_tag)

    for record in tag.ndef.message:
        new_txt = nfc.ndef.TextRecord(text=new_coin)
        new_msg = nfc.ndef.Message(new_txt)
        tag.ndef.message = str(new_msg)

    finalCoin(tag.ndef.message)

    led_util.flash_led()

    return True


def intTest(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


def finalCoin(message):	
    for record in message:
        print("You have " + record.data[3:] + " coin(s)")


def connected(tag):
    pass


def getCoin(tag):
    for record in tag.ndef.message:
        if intTest(record.data[3:]) is False:
            test_txt2 = nfc.ndef.TextRecord(text="0")
            test_msg2 = nfc.ndef.Message(test_txt2)
            tag.ndef.message = str(test_msg2)
            return "0"
        elif intTest(record.data[3:]) is True:
            return str(record.data[3:])


def connect_mysql(uid_tag, coin_tag):
    # you must create a Cursor object. It will let
    # you execute all the queries you need
    with db:
        cur = db.cursor()
        cur.execute("SELECT * FROM test1;")
        rows = cur.fetchall()
        uid_list = []
    for row in rows:
        uid_list.append(row[0])
    if str(uid_tag) not in str(uid_list):
        new_coin_tag = int(coin_tag) + 1
        cur.execute("INSERT INTO test1(UID, COIN, BRICK) VALUES\
            (%s, %s, %s)", (str(uid_tag), str(new_coin_tag), "1"))
        print ("You got a new coin!")
        sound_util.play_sound(COIN_SOUND)
        return str(new_coin_tag)
    else:
        new_coin_tag = coin_tag
        print ("You have already collected the coin.")
        sound_util.play_sound(BRICK_SOUND)
        return str(new_coin_tag)


if __name__ == '__main__':
    main()