from pyrogram import Client,filters
import os
from google_trans_new import google_translator  
from coffeehouse.lydia import LydiaAI
api_key = "2126a19291cc677696b3e5cde16cc5d54986c64a7c2ef596e593a8d22679383cef91d521d1a82864ab48086f3f8c6a0e9849cf08581c2e5f7e377b518dc68573"
lydia = LydiaAI(api_key)
translator = google_translator()  

app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
id=869979136
session_string ="BQBNf_r3IA5tLXdceJAc6qgbx5dKVyuismn8RMdqvbCo0wEr87lNw5ORvxSocM9MbOv2sXN8c6DNioL52-l1rW8TI9HXxP8M-DtkElj-j2R-1T04IhLGuf2pa3i73rJFjkt5cGSWP9hGX1NVx9G73lMWHKPpIbWyqb0z48t7_T5ji2VgIR3nuoSepV46klmNiz516--0K_wUEqAP0X1PaKQ-ke30HgpUi3b6uKIeNr27kibZphqBGT8cnQPgrps4WAuuf476l7blTYJM2lgqaQF0YXtOKA-vv2H0ZDiHeJYJl1sc2MurYMfPiCGmSahCIIkV-tIyH20BIJQ-Y_0sALE8U-lWcgA"
app = Client(session_string,app_id,api_hash)
@app.on_message(filters.text & filters.private & ~filters.bot & ~filters.user(users=[id,1407800946]))
def echo(client, message):
  message.reply_chat_action("typing")
  d=open("uid.txt","r")
  uid=d.read()
  if message.from_user["id"]==uid:
    e = open("uid.txt","r")
    sid = e.read()
    b = lydia.get_session(sid)
    if b.available=="True":
      output = b.think_thought(message.text)
      b= translator.translate(output,lang_tgt='si')
      message.reply_text(b)
    else:
      session = lydia.create_session()
      output = session.think_thought(message.text)
      b= translator.translate(output,lang_tgt='si')
      message.reply_text(b)
      g = open("sid.txt", "w")
      g.write(str(session.id))
      g.close()
  else:
    session = lydia.create_session()
    output = session.think_thought(message.text)
    b= translator.translate(output,lang_tgt='si')
    message.reply_text(b)
    h = open("sid.txt", "w")
    h.write(str(session.id))
    h.close()
    y = open("uid.txt","w")
    y.write(str(message.from_user["id"]))
    y.close()
app.run()
