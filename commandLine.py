import praw

reddit = praw.Reddit(client_id='0rDPWpdN0p5rnA',
	client_secret='FIKkxfmqKdlst2etbot6pjaLtf8',
	password='XemogDev',
	user_agent='test scripts',
	username='Xemog_Dev')
chosenSubreddit = input("Enter a subreddit")

for submission in reddit.subreddit(chosenSubreddit).hot(limit=10):
	print(submission.title)