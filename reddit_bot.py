#!/usr/local/bin/python
import praw
import config
import time
import os
import random

subreddits = ['gaming', 'test', 'aww', 'jokes', 'funny', 'pcgaming', 'pcmasterrace', 'teenagers']

def bot_login():											#sets login credentials from config file
	print "Logging in"
	r = praw.Reddit(username = config.username,				#Login using credentials
			password = config.password,						#password of bot
			client_id = config.client_id,					#client id found on reddit bot api panel
			client_secret = config.client_secret,			#secret key found on reddit bot api panel
			user_agent = "DadBotJokes_ 0.3" )				#user agent so reddit knows who we are
	print "Logged in"										#displays when we sucessfully log in
	return r 												#returns r as a variable for us to login

def delete_bad_posts():
	print "Attempting to delete"
	user = r.redditor('DadJokesBot_')							#Scans through my own posts
	for comments in user.comments.new(limit = 25):				#for loop
		if comments.score <= 0:									#if my comments are negative karma or 0 they get deleted
			comments.delete()
			print "A comment was deleted!"



def run_bot(r, comment_id_list):

	print "Scanning r/" + selected_sub
	for comment in r.subreddit(selected_sub).comments(limit=25): #Chooses the subreddit the bot will scan

		if comment.body.split(' ',2)[0] == "I'm" and comment.id not in comment_id_list and comment.author.name != r.user.me(): #sets parameters for which we find comments

			print "Trying to find comment..."
			if len(comment.body.split(' ', 3)[1]) > 3: #Only find words with more than 3 letters
				print "Comment found by user " + comment.author.name	#prints out author
				print comment.body	#prints their comment
				following_word = comment.body.split(' ',2)[1]	#sets a local variable with the following word after "I'm"
				reply = "Hi " + following_word + ", I'm Dad" "\n\n ------------- \n ^(I'm a silly bot | Downvote to remove)" #assigns var reply with our message

				####################################

				#comment.reply(reply)  					#submits our message to reddit as a comment reply

				###################################

				print reply #prints to console our message. Useful for debug
				comment_id_list.append(comment.id)		#appends the list so we dont comment twice on the same message
				with open ("comments.txt", "a") as f: 	#opens the text file holding the ids of the comments already messaged
					f.write(comment.id + "\n")			#adds to the list
				print "Comment posted!"
						#Sleep only if comment posted re RATELIMIT

def get_saved_comments():
	if not os.path.isfile("comments.txt"):				#if the txt file doesn't exist, just use local list
		comment_id_list = []
	else:
		with open("comments.txt", "r") as f:			#otherwise open the text file and read
			comment_id_list = f.read()							#adds all the text in our text file to local list
			comment_id_list = comment_id_list.split("\n")
			comment_id_list =filter(None, comment_id_list)		#filter out NULL data
	return comment_id_list										#returns list for later use

r = bot_login()													#bot login
comment_id_list = get_saved_comments()							#sets a list from our text file

while True: #forever loop
	selected_sub = random.choice(subreddits)	#Each loop, picks a new subreddit
	run_bot(r, comment_id_list)					#runs bot through sub
	delete_bad_posts()
	print "Will try again in fifteen minutes"
	time.sleep(900)

												#goes through past posts and deleted
												#negative karma
