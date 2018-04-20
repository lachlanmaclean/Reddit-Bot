import time
import random
subreddits = ['gaming', 'test', 'aww', 'jokes', 'funny', 'pcgaming', 'pcmasterrace', 'teenagers']


def run():
	print "Random Subreddit: " + random.choice(subreddits)
	time.sleep(3)

while True:
	run()
