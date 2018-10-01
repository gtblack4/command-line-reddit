import praw
from praw.models import MoreComments
#Session Information -- Please Don't steal my account
reddit = praw.Reddit(client_id='0rDPWpdN0p5rnA',
	client_secret='FIKkxfmqKdlst2etbot6pjaLtf8',
	password='XemogDev',
	user_agent='test scripts',
	username='Xemog_Dev')
#viewSubmission displays the top 20 comments using the user selection
#This function needs work, but I'm not sure the direction to take it in yet
def viewSubmission(subId,chosenSubreddit):
	submission = reddit.submission(id=subId)
	commentCount = 0
	print('{0:4}|{1:6}|{2:150.150}'.format("Rank","Score","Comment"))
	lineCount = 0
	while True:
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment,MoreComments):
				continue
		
			print('{0:4}|{1:6}|{2:150.150}'.format(commentCount,top_level_comment.score,top_level_comment.body))
			commentCount = commentCount + 1
			print('{0:4}|{1:6}|{2:150.150}'.format('____','______','____________________________________________________________________________________________________'))
			lineCount = lineCount + 1
			if lineCount%20==0:
				userNext = input("Enter 'Next' to view the next 20 comments or 'menu' to return to the Subreddit homepage:")
				if userNext == 'menu':
					break


	print(" ")
	while True:
		chosenComment = input('{0}{1}{2}'.format("Select a parent comment to view children, or enter 'Back' to return to the ",chosenSubreddit," homepage :"))
		commentCounter = 1
		if chosenComment == 'Back':
			break
		for top_level_comment in submission.comments:
			if chosenComment == commentCounter:
				viewChildComment()
				print(top_level_comment.body)
			commentCounter = commentCounter + 1



#chooseSubreddit displays the top 20 posts based on the user entry.
def chooseSubreddit(sortBy,chosenSubreddit):
	print(" ")
	if chosenSubreddit == " ":
		chosenSubreddit = input("Enter a subreddit:")
	counter = 1
	print(" ")
	print('{0}{1}{2}'.format("Here are the top 20 Hot posts in '/R/",chosenSubreddit,"'"))
	print('{0:4.4}|{1:6.6}|{2:8.8}|{3:150.150}'.format("Menu","Score","Comments","Title"))
	if sortBy == 'hot':
		for submission in reddit.subreddit(chosenSubreddit).hot(limit=20):
			print('{0:4}|{1:6}|{2:8}|{3:150.150}'.format(counter,submission.score,submission.num_comments,submission.title))
			counter= counter + 1
	if sortBy == 'top':
		for submission in reddit.subreddit(chosenSubreddit).top('all'):
			print('{0:4}|{1:6}|{2:8}|{3:150.150}'.format(counter,submission.score,submission.num_comments,submission.title))
			counter= counter + 1
	print(" ")
	threadMenu = {}
	while True:

		menu = {}
		menu['1']="Choose Post to View"
		if sortBy == 'hot':
			menu['2']="Change Sort By to: All time"
		else:
			menu['2']="Change Sort By to: Hot"
		menu['3']="Choose a Different Subreddit"

		while True:
			options=menu.keys()
			print(" ")
			for entry in options:	
				print(entry, menu[entry])
			print(" ")
			menuSelect = input("Select an Option:")
			if menuSelect =='1':
				
				viewSubmission(submission.id,chosenSubreddit)
			if menuSelect =='2':
				if sortBy == 'hot':
					chooseSubreddit('top',chosenSubreddit)
				if sortBy == 'top':
					chooseSubreddit('hot',chosenSubreddit)
			if menuSelect == '3':
				chosenSubreddit =""
				chooseSubreddit(sortBy)
			#chosenSubmission = input("Enter the submission number you want to view, or enter 'exit' to return to the menu:")
			# if chosenSubmission =='exit':
			# 	break
			# chosenSubmission = int(chosenSubmission)
			# submissionCount = 1
			# for submission in reddit.subreddit(chosenSubreddit).hot(limit=chosenSubmission):
			# 	if submissionCount == chosenSubmission:
			# 		viewSubmission(submission.id,chosenSubreddit)
			# 	submissionCount = submissionCount + 1

#This is the Main menu
menu = {}
menu['1']="Choose Subreddit"
menu['2']="Quit"
while True:
	options=menu.keys()
	print(" ")
	for entry in options:	
		print(entry, menu[entry])
	print(" ")
	menuSelect = input("Select an Option:")
	if menuSelect =='1':
		chooseSubreddit('hot'," ")
	if menuSelect =='2':
		break



