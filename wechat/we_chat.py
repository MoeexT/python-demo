# -*- coding: utf-8 -*-

import json
import requests
from wxpy import *

def auto_reply(text):
	url = "http://www.tuling123.com/openapi/api"
	api_key = "ab8463da3f324b5d89a37351f3917f82"
	payload = {
		"key": api_key,
		"info": text,
		"userid": "223093"
	}
	req = requests.post(url, data=json.dumps(payload))
	result = json.load(req.content)
	return result["text"]

bot = Bot(console_qr=True, cache_path=True)

@bot.register(mp)
def send_message(msg):
	return auto_replay(msg.text)
	
embed()

bot.file_helper.send("")
bot.friends()
bot.friends().stats()
bot.logout()
