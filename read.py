#!/usr/local/bin/python
import praw
import config
import time
import os
from urllib import quote_plus


STATEMENT = ["I'm"]
REPLY = ["Hi {}, I'm Dad"]

def bot_login():
	print "Logging in"
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "DadBotJokes_ comment test" )
	print "Logged in"
	return r


def run_bot(r):

	submission = r.subreddit('test').comments(limit=5)
	current_comment = "var"

	for comment in submission:
		#print comment.body
		if "I'm" in comment.body and not comment.author == r.user.me():

			current_comment = comment.body.split(' ',2)[1]
			print "Hi " + current_comment + ", I'm Dad"


	print "\n" + "Sleeping for 10 Seconds"
	time.sleep(10)


r = bot_login()



while True:
	run_bot(r)



