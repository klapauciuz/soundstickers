# -*- coding: utf-8 -*-
import sys
import telepot
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultAudio
import requests
from bs4 import BeautifulSoup
from config import *
import datetime

def on_inline_query(msg):
	query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
	print(datetime.datetime.now())
	print('Inline Query:', query_id, from_id, query_string)
	if query_string:
		articles = []
		r = requests.get('https://www.freesound.org/search/?q='+query_string+'&f=type%3Amp3+duration%3A%5B2+TO+10%5D&s=score+desc&advanced=1&g=')
		print(r.status_code)
		mp3s = BeautifulSoup(r.text, "lxml").find_all('a', class_='mp3_file')
		for mp3 in mp3s:
			print(mp3['href'])
		counter = -1
		for mp3 in mp3s:
			counter += 1
			print(mp3['href'])
			articles.append(
			InlineQueryResultAudio(
				id=str(counter),
				type='audio',
				title=mp3.text.split(' - ')[0],
				audio_url='https://www.freesound.org' + mp3['href'],
			   ))
		bot.answerInlineQuery(query_id, articles, 0)
	else:
		articles = []
		articles = [InlineQueryResultAudio(
						 id='0',
						 type='audio',
						 title='Laugh',
						 audio_url='https://www.freesound.org/data/previews/150/150968_1339744-lq.mp3',
					), InlineQueryResultAudio(
						 id='1',
						 type='audio',
						 title='Fail',
						 audio_url='https://www.freesound.org/data/previews/172/172949_3226163-lq.mp3',
					), InlineQueryResultAudio(
						 id='2',
						 type='audio',
						 title='Woohoo!',
						 audio_url='https://www.freesound.org/data/previews/220/220691_4108287-lq.mp3',
					), InlineQueryResultAudio(
						 id='3',
						 type='audio',
						 title='Applause',
						 audio_url='https://www.freesound.org/data/previews/60/60788_199526-lq.mp3',
					), InlineQueryResultAudio(
						 id='4',
						 type='audio',
						 title='Hi there!',
						 audio_url='https://0.s3.envato.com/files/173687654/preview.mp3',
					), InlineQueryResultAudio(
						 id='5',
						 type='audio',
						 title='Bye bye!',
						 audio_url='https://www.freesound.org/data/previews/323/323361_4347097-lq.mp3',
					), InlineQueryResultAudio(
						 id='6',
						 type='audio',
						 title='Chicken',
						 audio_url='https://www.freesound.org/data/previews/188/188390_3466604-lq.mp3',
					), InlineQueryResultAudio(
						 id='7',
						 type='audio',
						 title='Happy huming',
						 audio_url='https://www.freesound.org/data/previews/361/361077_6590186-lq.mp3',
					), InlineQueryResultAudio(
						 id='8',
						 type='audio',
						 title='Laughing hard',
						 audio_url='https://www.freesound.org/data/previews/41/41141_428749-lq.mp3',
					), InlineQueryResultAudio(
						 id='9',
						 type='audio',
						 title='Evil laugh',
						 audio_url='https://www.freesound.org/data/previews/319/319766_3341540-lq.mp3',
					), InlineQueryResultAudio(
						 id='10',
						 type='audio',
						 title='Deep evil laugh',
						 audio_url='https://www.freesound.org/data/previews/350/350679_5106192-lq.mp3',
					), InlineQueryResultAudio(
						 id='11',
						 type='audio',
						 title='Robot laugh',
						 audio_url='https://www.freesound.org/data/previews/255/255937_4062622-lq.mp3',
					), InlineQueryResultAudio(
						 id='12',
						 type='audio',
						 title='Caugh',
						 audio_url='https://www.freesound.org/data/previews/353/353669_6552793-lq.mp3',
					), InlineQueryResultAudio(
						 id='13',
						 type='audio',
						 title='Funky',
						 audio_url='https://www.freesound.org/data/previews/187/187096_586-lq.mp3',
					), InlineQueryResultAudio(
						 id='14',
						 type='audio',
						 title='Snoring',
						 audio_url='https://www.freesound.org/data/previews/371/371299_5302340-lq.mp3',
					), InlineQueryResultAudio(
						 id='15',
						 type='audio',
						 title='Oh yeah!',
						 audio_url='https://www.freesound.org/data/previews/172/172005_764147-lq.mp3',
					)]

		bot.answerInlineQuery(query_id, articles, 0)

def on_chosen_inline_result(msg):
	result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
	print('Chosen Inline Result:', result_id, from_id, query_string)

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(datetime.datetime.now())
	print('someone wants to chat and wrote this...:')
	print(msg['text'])
	if msg['text'] == '/help' or msg['text'] == '/start':
		bot.sendMessage(chat_id, 'Hey. Call me from your chats by typing `@soundstickers_bot` in the message field. You will see a list of default sound stickers that you can send to chat.\n\nAlso you can just type name of any other sound, like `@soundstickers_bot meow` or `@soundstickers_bot bird` to upload and send sounds from freesound.org.\n\nHave fun!', parse_mode='Markdown')


bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
				  'inline_query': on_inline_query,
				  'chosen_inline_result': on_chosen_inline_result},
				 run_forever='Listening ...')