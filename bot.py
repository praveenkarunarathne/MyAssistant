from pyrogram import Client,filters
import os
os.system("pip install coffeehouse")
from google_trans_new import google_translator  
from coffeehouse.lydia import LydiaAI
api_key = os.env.get("lydia_api_key")
lydia = LydiaAI(api_key)
translator = google_translator()  

app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
session_string = os.env.get("session_string")
app = Client(session_string,app_id,api_hash)
@app.on_message(filters.text & filters.private & ~filters.bot & ~filters.user(users=1407800946))
def echo(client, message):
  message.reply_chat_action("typing")
  r = open("uid.txt", "a")
  r.close()
  d=open("uid.txt","r")
  uid=str(d.read())
  c=str(message.from_user["id"])
  if c==uid:
    x = open("sid.txt", "a")
    x.close()
    e = open("sid.txt","r")
    sid = e.read()
    b = lydia.get_session(sid)
    m=str(b.available)
    if m=="True":
      output = b.think_thought(message.text)
      b= translator.translate(output,lang_tgt='si')
      message.reply_text(b)
    else:
      session = lydia.create_session()
      output = session.think_thought(message.text)
      b= translator.translate(output,lang_tgt='si')
      g = open("sid.txt", "w")
      g.write(str(session.id))
      g.close()
      message.reply_text("ආයුබෝවන් ඔබට කොහොම ද? . මම භානුකගේ සහායිකාව වෙමි. මට ඔබට භානුක ලෙස චැට් හරහා උදව් කළ හැකිය. මට කෙටි පණිවිඩ පමණක් කියවිය හැකි අතර කරුණාකර ඉංග්‍රීසි භාෂාව පමණක් ටයිප් කරන්න. මන්ද මට එම භාෂාව පමණක් තේරුම් ගත හැකි අතර, ඔබට වහාම උදව් කිරීමට මම සතුටු වෙමි!")
      message.reply_text(b)
  else:
    session = lydia.create_session()
    output = session.think_thought(message.text)
    b= translator.translate(output,lang_tgt='si')
    h = open("sid.txt", "w")
    h.write(str(session.id))
    h.close()
    y = open("uid.txt","w")
    y.write(str(message.from_user["id"]))
    y.close()
    message.reply_text("ආයුබෝවන් ඔබට කොහොම ද? . මම භානුකගේ සහායිකාව වෙමි. මට ඔබට භානුක ලෙස චැට් හරහා උදව් කළ හැකිය. මට කෙටි පණිවිඩ පමණක් කියවිය හැකි අතර කරුණාකර ඉංග්‍රීසි භාෂාව පමණක් ටයිප් කරන්න. මන්ද මට එම භාෂාව පමණක් තේරුම් ගත හැකි අතර, ඔබට වහාම උදව් කිරීමට මම සතුටු වෙමි!")
    message.reply_text(b)
@app.on_message(~filters.text & filters.private & ~filters.bot & ~filters.user(users=1407800946))
def stk(client, message):
  message.reply_chat_action("typing")
  message.reply_text("මට කෙටි පණිවිඩ පමණක් කියවිය හැකිය. කරුණාකර මට කෙටි පණිවිඩ පමණක් එවන්න.")
app.run()
