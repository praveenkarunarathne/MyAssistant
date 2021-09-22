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
st = ("CAACAgIAAxkBAAECH15gYoq6kC0pUnq9j9HUoHRaFrXxdQACKwwAAhU6cEiad-2FxM2fPx4E","CAACAgIAAxkBAAECH2BgYoq-CweohIQfzsTnP8eInM4eVwAC0wgAAmxpeEhutjKphXzGUB4E","CAACAgIAAxkBAAECH2JgYorBptX1rk0gSgU9n5j-MAmg9wACFwkAAobXeEjwOpl9qSewaR4E","CAACAgIAAxkBAAECH2RgYorF_8RdGrUerLdorg3Yw8YNFQACtAkAAoK1eUjLqezXdkUPwB4E","CAACAgIAAxkBAAECH2ZgYorHjUSTPcHJq0gzBnZ1QrPpdQACTQkAAnYreUgDJEKDRPfmCB4E","CAACAgIAAxkBAAECH2hgYorKvZzd2OS6W7F53w5VglAAAWsAAkAKAAOIeEg3YPSpfkagah4E","CAACAgIAAxkBAAECH2pgYorOFPX-En9TA75v25HorLffBgACgAoAAn-IeUgQj9SZDgzuSR4E","CAACAgIAAxkBAAECH2xgYorR-AwW3lz7YF1ktKh5AmBObQACPgoAAkRoeEjk3oI22WsWQR4E","CAACAgIAAxkBAAECH25gYorUW-MK_bIaF6sYxo-SliNRHQACGAwAAvE8eUikdLCSqv4MHh4E","CAACAgIAAxkBAAECH3BgYorYoE62xxblk73dUvCKuMmy8AACcAkAAuE_eEjcEjg-jnAElB4E","CAACAgIAAxkBAAECH3JgYorb-Jkwg2TYtgh499ltBsnMNgACGgcAAnT3eUhYeUB74HivvB4E","CAACAgIAAxkBAAECH3RgYorfgIe2MA2jebauk7nBsLu-EgACowkAAmgQeUiWfKD49y8GxR4E","CAACAgIAAxkBAAECH3ZgYoriUKQvezKX1Z0Ook0FRtcO7QAC2gcAAriHeEg4uUrgNPGoJh4E","CAACAgIAAxkBAAECH3hgYorlaKx4-HK93qTVrkRo5xmgtwACGAwAAvE8eUikdLCSqv4MHh4E","CAACAgIAAxkBAAECH3pgYorn1P8E0meDQxOzxsGcpElNIQACcAkAAuE_eEjcEjg-jnAElB4E","CAACAgIAAxkBAAECH3xgYorrnpTBwQxgO3YJ9i0_-Z7z1AACGgcAAnT3eUhYeUB74HivvB4E","CAACAgIAAxkBAAECH35gYorvamWJTSGrSGLP6c9hIMTkdQACowkAAmgQeUiWfKD49y8GxR4E","CAACAgIAAxkBAAECH4BgYorzmTHtYhPDMsTxU3JJgkFlvAAC2gcAAriHeEg4uUrgNPGoJh4E","CAACAgIAAxkBAAECH4JgYor2QBjlIfhf6a3DKM0Q5vjxvgAC1gkAAqn5eEgjb457lafMmh4E","CAACAgIAAxkBAAECH4RgYosazPXhEKL4LUxqHdKOlSIsVQAC5wgAAjWteUjzhCyplSfyoR4E","CAACAgIAAxkBAAECH4ZgYosfrBPCrFP9gICVchXOSjhMDgACNwgAArkCeEhCxj4n7m3ZwR4E","CAACAgIAAxkBAAECH4hgYosuaOoVnq9aAjMgGFAqWFNV4QACNggAAmb_cUgh7s4KinEBKx4E","CAACAgIAAxkBAAECH4pgYosyZs-2kLBfMIPSdUmVDAAByXMAAncJAAKHTXhIIWD5LTtxLYQeBA","CAACAgIAAxkBAAECH4xgYos3e7MoHODoXtHEiYL579oHQwACpgcAAqrieUgN453uUkDlRB4E","CAACAgIAAxkBAAECH45gYos6H4ASAiosvhqx0PABsZ6RhAACiwgAAub8cUh80WZ4Zf8Uuh4E","CAACAgIAAxkBAAECH5BgYos-ObDHsXugMxM3slPzS90FqAACpQoAAn9_eUhAQIpxKMcmYx4E","CAACAgIAAxkBAAECH5JgYotBUGr54x2dp2JXow1ebsJkmgACLQkAAun1eUi3I1Hy_V3Aox4E","CAACAgIAAxkBAAECH5RgYotDhPlDeXBfhkk1m9DpFelAkAACWwgAApI_cEgUry3ru4NTyh4E","CAACAgIAAxkBAAECH5ZgYotGcuszW0EdZ802q22fYJN8GAACHAkAAjvxcUjTeWFVzhg5oh4E","CAACAgIAAxkBAAECH5hgYotJQWmfAoLgFTdmxEVt1GuDqAACoQkAAkkNcUheM47INJdZyh4E","CAACAgIAAxkBAAECH5pgYotLR2R4FzTAlMXWDDA-fweAFAACLQ4AAquAeEjArMoE-DufUR4E","CAACAgIAAxkBAAECH5xgYotOyySjfhrQaFs3a_KZpOgPtgACwgcAAnpyeEi8v9ltM005Kx4E","CAACAgIAAxkBAAECH55gYotR4IeyUYEVGmCC2UR7p2cVVAACTAkAAoF-eUhnynutT6b_1B4E","CAACAgIAAxkBAAECH6BgYotTUAdE0WcX9PfrLuhRrK6YCgACmwgAAuEyeEg4UJH3qXOHzR4E","CAACAgIAAxkBAAECH6JgYotWIq8AAc_1fAABmoppWwsAAabUMgACKQkAArZCeEgyGp9fixDGCB4E","CAACAgIAAxkBAAECH6RgYotZEYyaEmmMW7hOwMmAjgIchAACPAkAAt2zeEjuGlH9wT6mxR4E","CAACAgIAAxkBAAECH6ZgYotepdBsaMcElaRG70ypvy1icwACyggAAu5ucEjQXx5jbxdZHh4E","CAACAgIAAxkBAAECH6hgYothOxPAjhKIvLWhT5l7YjHkMAACUQsAAuyPeEgmAAEJlOjDHmceBA","CAACAgIAAxkBAAECH6pgYotj66aIU09CZjEU9YV9FqIskQAC8AkAAjD9eUjS4GGREiyUTh4E","CAACAgIAAxkBAAECH6xgYotmH20vjAGzNtJO4gOPg9_YRAACSAkAAm6KeEg4rnrJvCSNgB4E","CAACAgIAAxkBAAECH65gYotpXzwcTcXt6hrFZIBepQQUlgACBAkAAhKSeEhOOmLuXnXygB4E","CAACAgIAAxkBAAECH7BgYots1dnQU7v4jhMGzeHyBiWQaAAC1woAAkaxeUg-JD75XC0gbx4E","CAACAgIAAxkBAAECH7JgYotuxChvs9URlpbTxVVRq4DZowACQQkAApzGeUjCxJbPUqXv8R4E","CAACAgIAAxkBAAECH7RgYotxdf45n3Svbz_8M9IEJXmOIwACzggAAsG1cEif81ur4gUQAh4E","CAACAgIAAxkBAAECH7ZgYot0nvpPSNyCJPv3jzG4eaL2ywACTQcAAvwNeUhlG5Suple4Hh4E","CAACAgIAAxkBAAECH7hgYot3S71WrVgbKTJzHIWL1RKRTwACOgkAAlIeeEh7hsNm9iMYhB4E","CAACAgIAAxkBAAECH7pgYot6aZW449FS-gSNynjqkRZz2QACswkAAnBRcEiaF32n1_7M_R4E","CAACAgIAAxkBAAECH7xgYot9F_ecBNzHGOM8nwevddrpYQACFAoAAjPpeEiAd-iAzJYOVB4E","CAACAgIAAxkBAAECH75gYouAEstrYqDlrAABIto5PF4it50AAmAJAAKySnFIIZpMOnh5gqIeBA","CAACAgIAAxkBAAECH8BgYouDa1mHtANs_t-cuxd43FVk4wACNggAAg0ZeEg0_oqvGyMPKx4E","CAACAgIAAxkBAAECH8JgYouGRdcRQapbiujgD8VHXFoYhQACQQoAAuSZyUjOZGJlV_8t6x4E")

app = Client(string_session,app_id,api_hash)

with app:
    un=app.get_me().first_name
try:
  wm=os.environ.get("WELCOME_MESSAGE")
except:
  wm=("!" %(un,un))


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
