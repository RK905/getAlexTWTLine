from twitter import *

config = {}
execfile("config.py", config)

twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

user = "alexiskold"
results = twitter.statuses.user_timeline(screen_name = user)

for status in results:
	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))