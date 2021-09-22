from pyrogram import Client,filters
import os
import time
import random
import re
import requests
from google_translate_py import Translator

app_id=int(os.environ.get("APP_ID"))
api_hash=os.environ.get("API_HASH")
mid= int(os.environ.get("USER_ID"))
string_session = os.environ.get("STRING_SESSION")
bid = os.environ.get("BID")
key = os.environ.get("KEY")
uid = os.environ.get("UID")
st = ("😀","😃","😄","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🤩","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","☹️","🙁","😕","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","😫","🤤","😴","😪","🌛","🌜","🌚","🌝","🌞","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","🤠","🤑","😎","🤓","🤥","🤡","👻","💩","👽","🤖","🎃","👿","👹","👺","☠️","🔥","✨","💪","👍","👎","👏","🙌","🤲","🤝","🤜","🤛","✊","👊","🖐️","✋","🤚","👋","👌","✌️","🤘","🤟","🤙","🤞","🖖")

app = Client(string_session,app_id,api_hash)

with app:
  un=app.get_me().first_name
  try:
    app.join_chat("YTAllInOneChannel")
  except:
    print ("done")
try:
  wm=os.environ.get("WELCOME_MESSAGE")
except:
  wm=("Hello! how are you? . I am %s's assistant . I can help you as %s through chat . I am happy to help you ." %(un,un))


@app.on_message(filters.private & ~filters.bot & ~filters.user(users="me"))
def echo(client, message):
  message.reply_chat_action("typing")
  c=str(message["media"])
  if c=="True":
    b=random.choice(st)
    message.reply_text(b,quote=True)
  else:
    text = message.text

    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    ntext = regrex_pattern.sub(r'',text)
    if ntext:
      t= Translator().translate(ntext, "", "en")
      url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
      querystring = {"bid":bid,"key":key,"uid":uid,"msg":t}
      headers = {'x-rapidapi-key': "1b658cfec5mshad10a4f71536534p1117e4jsn1a431058d5f6",'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com"}
      response = requests.request("GET", url, headers=headers, params=querystring)
      rp=response.text[8:-2]
      b= Translator().translate(rp, "", "si")
      message.reply_text(b,quote=True)
    else:
      b=random.choice(st)
      message.reply_text(b,quote=True)

app.run()
