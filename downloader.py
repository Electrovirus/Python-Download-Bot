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
    ret_msg = bot.send_message(cid, "Hello I'm Downloader bot \n\nCommands : \n/dl [Link] \n/id \n/feedback [text]", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id

    @bot.message_handler(regexp='^(/dl) (.*)')
def all(m):
    text = m.text.split()[1]
    id = m.from_user.id
      try:
         if m.chat.type == 'private':
             if re.match('(http|https)://.*.(png)$',text):
                 msg = bot.send_message(m.chat.id, '*Downloading.....*',parse_mode='Markdown')
                 dw(text,'file.png')
                 bot.send_photo(m.chat.id, open('file.png'),caption='Here is your file')
                 os.remove('file.png')
             if re.match('(http|https)://.*.(apk)$',text):
                 msg = bot.send_message(m.chat.id, '*Downloading .....*',parse_mode='Markdown')
                 dw(text,'app.apk')
                 bot.send_document(m.chat.id, open('app.apk'),caption='Here is your file')
                 os.remove('app.apk')
             if re.match('(http|https)://.*.(html|htm)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.html')
                 bot.send_document(m.chat.id, open('file.html'),caption='Here is your file')
                 os.remove('file.html')
             if re.match('(http|https)://.*.(jpg)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'s.jpg')
                 bot.send_photo(m.chat.id, open('s.jpg') ,caption='Here is your file')
                 os.remove('s.jpg')
             if re.match('(http|https)://.*.(gif)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'s.gif')
                 bot.send_photo(m.chat.id, open('s.gif'),caption='Here is your file')
                 os.remove('s.gif')
             if re.match('(http|https)://.*.(zip|rar)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.zip')
                 bot.send_document(m.chat.id, open('file.zip'),caption='Here is your file')
                 os.remove('file.zip')
             if re.match('(http|https)://.*.(webp)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.webp')
                 bot.send_sticker(m.chat.id, open('file.webp'))
                 os.remove('file.webp')
      except IndexError:
                 bot.send_message(m.chat.id, '*Error!\nURL Or Format Is Invalid!*',parse_mode='Markdown')

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
    markup.add(types.InlineKeyboardButton("Downloader Bot", url="https://telegram.me/Ev_official"))
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
