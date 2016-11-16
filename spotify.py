import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import json
import os
import random
import requests as req
import json, os
from time import sleep
import sys
import re
import urllib
reload(sys)
sys.setdefaultencoding("utf-8")

Token = ''
owner = '184018132'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Developer", url="https://telegram.me/Electrovirus")
    c = types.InlineKeyboardButton("Our channel", url="https://telegram.me/Ev_official")
    markup.add(a, c)
    ret_msg = bot.send_message(cid, "Hello I'm Spotify bot \n\nCommands : \n/spotify  [songname]-[artist] \n/id \n/feedback [text]", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id

@bot.message_handler(commands=['spotify'])
def m(m):
        try:
            url = urllib.urlopen("https://api.spotify.com/v1/search?limit=1&type=track&q={}".format(m.text.replace('/spotify','')))
            data = url.read()
            js = json.loads(data)
            files = js['tracks']['items'][0]['preview_url']
            name = js['tracks']['items'][0]['name']
            pic = js['tracks']['items'][0]['album']['images'][1]['url']
            art = js['tracks']['items'][0]['artists'][0]['name']
            bot.send_message(m.chat.id, '<b>Name</b> : {}\n<b>Artist : </b>{}'.format(name,art),parse_mode='HTML')
            bot.send_chat_action(m.chat.id, 'record_audio')
            urllib.urlretrieve(files,'spotify.mp3')
            urllib.urlretrieve(pic,'spotify.png')
            bot.send_audio(m.chat.id, open('spotify.mp3'), title=name)
            bot.send_sticker(m.chat.id, open('spotify.png'))
            hash = 'spotify'
            os.remove('spotify.mp3')
            os.remove('spotify.png')
            print ' send /spotify'
        except KeyError:
            bot.send_message(m.chat.id, 'Error')
        except IndexError:
            bot.send_message(m.chat.id, 'Error')
        except IOError:
            bot.send_message(m.chat.id, 'Error')

@bot.message_handler(commands=['id', 'ids', 'info', 'me'])
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    t = m.chat.type
    d = m.date
    text = m.text
    p = m.pinned_message
    fromm = m.forward_from
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Spotify Bot", url="https://telegram.me/Ev_official"))
#info text
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(commands=['feedback'])
def feedback(m):
    senderid = m.chat.id
    first = m.from_user.first_name
    usr = m.from_user.username
    str = m.text
    txt = str.replace('/feedback', '')
    bot.send_message(senderid, "_Thank Your feedback sent_", parse_mode="Markdown")
    bot.send_message(owner, "msg : {}\nid : {}\nname : {}\nUsername : @{}".format(txt,senderid,first,usr))

bot.polling(True)
