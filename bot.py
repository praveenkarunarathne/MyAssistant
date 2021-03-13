from pyrogram import Client,filters
import os
app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
id=869979136
app = Client(
    "my",app_id,api_hash)
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
  app.send_message(int(uid), message.text)
app.run()
