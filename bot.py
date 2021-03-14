from pyrogram import Client,filters
import os
from google_trans_new import google_translator  

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
translator = google_translator()  

app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
id=869979136
session_string ="BQBNf_r3IA5tLXdceJAc6qgbx5dKVyuismn8RMdqvbCo0wEr87lNw5ORvxSocM9MbOv2sXN8c6DNioL52-l1rW8TI9HXxP8M-DtkElj-j2R-1T04IhLGuf2pa3i73rJFjkt5cGSWP9hGX1NVx9G73lMWHKPpIbWyqb0z48t7_T5ji2VgIR3nuoSepV46klmNiz516--0K_wUEqAP0X1PaKQ-ke30HgpUi3b6uKIeNr27kibZphqBGT8cnQPgrps4WAuuf476l7blTYJM2lgqaQF0YXtOKA-vv2H0ZDiHeJYJl1sc2MurYMfPiCGmSahCIIkV-tIyH20BIJQ-Y_0sALE8U-lWcgA"
app = Client(session_string,app_id,api_hash)
@app.on_message(filters.text & filters.private & ~filters.bot & ~filters.user(users=[id,1407800946]))
def echo(client, message):
  f = open("uid.txt", "w")
  f.write(str(message.from_user["id"]))
  f.close()
  message.forward(id)
@app.on_message(filters.text & filters.user(users=id))
def bot(client,message):
  d=open("uid.txt","r")
  uid=d.read()
  b= translator.translate(message.text,lang_tgt='si')  
  app.send_message(int(uid), b)
app.run()
