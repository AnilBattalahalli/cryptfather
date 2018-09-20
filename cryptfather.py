#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, binascii, argparse, itertools

key='%^*%#^#^#^#^%$&*$&$^$^$^$^#%#$%#@#!#$%@$#^%#&$^*$*%%*&%(%(*^(111111kbdsbvkjsadvbsvbsbadojvbjsbdjbvojsbdbvjbasdojbvjobajsdbvbojsdbvjobsadojbvjobsjodbvbabsojvbojbsovbpouasbvpuobaspuobvpusdbvpiubaspiduvbpiusadbvpiubsdapviubsadpuobbpiupggyggyh8707t07bt08t0bb008tb7tbt9bt0t0780r0v79[t79v7p9rv68ro86odoo5o6coe68v6vr8bbogoyfonyffbffnfnfftftftfttbtbtdtvrrvr6rrvdd5995d5d57d975d5d97d97d795d9dd9dd9ddd4'




# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
"""def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def echo(bot, update):
	print update.message.chat.id
	update.message.reply_text(update.message.text)"""

################################################################################

def start(bot, update):
    u=update.message.text
    if u[0]=='~':
        m=decrypt(u,key)
    else:
        m=encrypt(u,key)
    bot.sendMessage(chat_id=update.message.chat.id, text=m)

def encrypt(msg, key):
    '''Return cipher text'''
    msg= (binascii.hexlify(msg.encode('utf-8'))).decode('utf-8')
    msg= xor_str(msg, key)

    # ascii armor the cipher text
    cipher= (binascii.hexlify(msg.encode())).decode()

    cipher="~%s" %cipher
    return cipher

def decrypt(cipher, key):
    '''Return plain text message'''
    # get back the string from ascii armored cipher
    cipher=cipher[1:]
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    msg = xor_str(cipher, key)
    msg = (binascii.unhexlify(msg.encode('utf-8'))).decode('utf-8')
    return msg

def xor_str(a, b):
    '''Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.'''
    xorred = ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xorred



#def error(bot, update, error):
    #logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("205606239:AAFxxEbu5diVOTzhirS36W01UMJwWL0Wk7M")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], start))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
