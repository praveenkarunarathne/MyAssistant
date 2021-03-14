from pyrogram import Client,filters
import os
from google_trans_new import google_translator  

translator = google_translator()  

app_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
id=869979136
session_string ="BQCWP5HKSDNyjA5NpQRDgHZ92v4PRQBnWdxY07py9UkmMljHsmx_QTKlAm4AIjCh5O01rszuU4MV4uiPeunkuSe4hPQttLa6792-VnHdSv1K0uAaUntEGDkJj_2DSFMCyw5UAH5LtPJK1uw8zX71fIzDXqHeX_jxJXEl9zoGA70LxOUCbMhr_OY-oIMAiKwgulK3jh4w5nmxlxgm9lrAbRcelAQQRyOh53BLlF7q68jV0t3PyBy6kTXEC8j2IlQ_F9KHnUT51p6Jt0aCIiZ1r0AP8c_qzSBLLR-0q_xW5zdJaBjkgJLgMHzk0bi5fYfPcoHKY9YTjmEsNkdi1nyW1Wc0U-lWcgA"
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
