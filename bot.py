from pyrogram import Client,filters
import os
import time
import random
import re
import requests
from google_translate_py import Translator

app_id=int(os.environ.get("APP_ID"))
api_hash=os.environ.get("API_HASH")
string_session = os.environ.get("STRING_SESSION")
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
      Kuki =   requests.get(f"https://kukiapi.xyz/api/botname/owner/message={t}").json()
      rp = Kuki['reply']
      b= Translator().translate(rp, "", "si")
      message.reply_text(b,quote=True)
    else:
      b=random.choice(st)
      message.reply_text(b,quote=True)

app.run()
