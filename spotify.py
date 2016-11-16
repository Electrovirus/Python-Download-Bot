import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import json
import os
import config
import random
import requests as req

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Taylor Team \xE2\x9C\x8C", url="https://telegram.me/taylor_team")
    c = types.InlineKeyboardButton("Add group \xE2\x9C\x8C", url="https://telegram.me/ID_bot_robot?startgroup=test")
    markup.add(a, c)
    b = types.InlineKeyboardButton("Developer ID bot \xE2\x9C\x8C", url="https://telegram.me/negative_officiall")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
    markup.add(nn)
    ret_msg = bot.send_message(cid, "Hello I'm ID bot \n\n Send : \n  /id or /me or /info   \n\n\n get your id : \n /idme (just pv) \nsend Your feedback : /feedback [msg]\n\n\n list inline mod : \ntype @ID_bot_robot\n\nBot version 3", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id

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
    markup.add(types.InlineKeyboardButton("\xF0\x9F\x98\x8A Taylor Team \xF0\x9F\x98\x8A", url="https://telegram.me/taylor_team"))
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
    bot.send_message(senderid, "_Thank Your Msg Posted admin_", parse_mode="Markdown")
    bot.send_message(config.owner, "msg : {}\nid : {}\nname : {}\nUsername : @{}".format(txt,senderid,first,usr))

bot.polling(True)
