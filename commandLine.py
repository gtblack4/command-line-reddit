import praw
from praw.models import MoreComments
import textwrap
import math
import getpass
#Session Information -- Please Don't steal my account
	#client_id='0rDPWpdN0p5rnA
	#client_secret='FIKkxfmqKdlst2etbot6pjaLtf8',
	#password='XemogDev',
	#username='Xemog_Dev')
#viewSubmission displays the top 20 comments using the user selection
#This function needs work, but I'm not sure the direction to take it in yet
loggedIn = False
reddit = praw.Reddit(client_id='0rDPWpdN0p5rnA',
	client_secret='FIKkxfmqKdlst2etbot6pjaLtf8',
	user_agent='test scripts',
	password='XemogDev',
	username='Xemog_Dev')
def Main():
	
	menu = {}
	menu['1']="Homepage"
	menu['2']="Choose Subreddit"
	menu['3']="Quit"
	while True:
		options=menu.keys()
		print(" ")
		for entry in options:	
			print(entry, menu[entry])
		print(" ")
		menuSelect = input("Select an Option:")
		if menuSelect =='1':
			chooseSubreddit('hot',"all")
		if menuSelect =='2':
			chooseSubreddit('hot'," ")
		if menuSelect =='3':
			break

def printParentNewline():
	print('{0:6}|{1:9}|{2:100.100}'.format('______','_________','_________________________________________________________________________________________________________'))

def leaveComment():
	print("lravecomment")
def displayReplies(replies,depth):
	varY = 1
	depthHolder = ""
	width = depth
	widthCounter = 1
	widthHolder = ""
	while True:
		depthHolder = depthHolder + str('     ')
		depth = depth - 1
		if depth == 0:
			break;
	while True:
		widthHolder = widthHolder + "_____"
		if widthCounter == (20-width):
			break
		widthCounter = widthCounter + 1
		commentBody = replies.body.replace('\n','')#I'm stripping out newline tags. It will ruin the comments format, but it will look prettier

	while varY <= (math.ceil(len(commentBody)/100)):
		if varY == 1:
			print('{0:6}{1:5}|{2:9.9}|{3}'.format(depthHolder,replies.score,replies.author.name,str(commentBody[(varY-1)*(100-((depth+1)*5)):varY*(100-((depth+1)*5))])))
		else:
			print('{0:6}{1:5}|{2:9.9}|{3}'.format(depthHolder,"     "," ",str(commentBody[(varY-1)*(100-((depth+1)*5)):varY*(100-((depth+1)*5))])))
		varY = varY + 1
	print('{0:6}{1:5}|{2:9}|{3}'.format(depthHolder,'     ','_________',widthHolder))
	
def displayLastComment(lineCount):
	print("This is under construction")
def viewSubmission(subId,chosenSubreddit,sortBy):
	submission = reddit.submission(id=subId)
	print('{0:6}|{1:9}|{2:10.10}|{3:11}{4:89.89}'.format("Score","Author","Comment","Post Title:",submission.title))
	lineCount = 1
	x = 1
	for comment in submission.comments:
		if isinstance(comment, MoreComments):
			continue
		lineCount = lineCount + 1
		body = str(comment.body).replace('\n','')
		varX = 1
		commentNum = 1
		#This logic splits comments longer than 100 characters into multiples lines
		#It allows us to keep the formatting without longer comments running onto multiples lines
		#
		print('{0:6}.{1:9}.{2:100.100}'.format('______','_________','_________________________________________________________________________________________________________'))
		while varX <= (math.ceil(len(body)/100)):
			if varX == 1:
				print('{0:6}|{1:9.9}|{2:100.100}'.format(comment.score,comment.author.name,str(body[(varX-1)*100:varX*100])))
			else:
				print('{0:6}|{1:9}|{2:100}'.format(" "," ",str(body[(varX-1)*100:varX*100])))
			varX = varX + 1
			
		printParentNewline()#this is 120 characters long
		print(commentNum)
		
		for replies in comment.replies:
			depth = 1
			if isinstance(replies, MoreComments):
				continue
			commentNum = commentNum + 1 
			displayReplies(replies,depth)
			for children in replies.replies:
				depth = 2
				if isinstance(children, MoreComments):
					continue
				commentNum = commentNum + 1 
				displayReplies(children,depth)
				for toddler in children.replies:
					depth = 3
					if isinstance(toddler, MoreComments):
						continue
					commentNum = commentNum + 1 
					displayReplies(toddler,depth)
					for baby in toddler.replies:
						depth = 4
						if isinstance(baby, MoreComments):
							continue
						commentNum = commentNum + 1 
						displayReplies(baby,depth)
			print(" ")
			userNext = input("'Enter','Back','Menu','Comment':")
			if userNext == 'Menu':
				chooseSubreddit(sortBy,chosenSubreddit)
			if userNext == 'Next':
				continue
			if userNext == 'Back':
				displayLastComment(lineCount)
			if userNext == 'Comment':
				leaveComment()
			lineCount = 1
			x = x + 1
	print(" ")

#chooseSubreddit displays the top 20 posts based on the user entry.
def chooseSubreddit(sortBy,chosenSubreddit):
	print(" ")
	if chosenSubreddit == " ":
		chosenSubreddit = input("Enter a subreddit:")
	counter = 1
	print(" ")
	print('{0}{1}{2}{3}{4}'.format("Here are the ", sortBy ," posts in '/R/",chosenSubreddit,"'"))
	print('{0:4.4}|{1:6.6}|{2:8.8}|{3:100.100}'.format("Menu","Score","Comments","Title"))
	if sortBy == 'hot':
		for submission in reddit.subreddit(chosenSubreddit).hot(limit=20):
			print('{0:4}|{1:6}|{2:8}|{3:100.100}'.format(counter,submission.score,submission.num_comments,submission.title))
			counter= counter + 1
	if sortBy == 'top':
		for submission in reddit.subreddit(chosenSubreddit).top('all',limit=20):
			print('{0:4}|{1:6}|{2:8}|{3:100.100}'.format(counter,submission.score,submission.num_comments,submission.title))
			counter= counter + 1
	print(" ")
	while True:

		menu = {}
		menu['1']="Choose Post to View"
		if sortBy == 'hot':
			menu['2']="Change Sort By to: All time"
		else:
			menu['2']="Change Sort By to: Hot"
		menu['3']="Choose a Different Subreddit"
		menu['4']="Re-Display Posts"

		while True:
			options=menu.keys()
			print(" ")
			for entry in options:	
				print(entry, menu[entry])
			print(" ")
			menuSelect = input("Select an Option:")
			submissionCount = 1
			if menuSelect =='1':
				chosenSubmission = input("Enter the submission number you want to view, or enter 'exit' to return to the menu:")
				if chosenSubmission == 'exit':
					break
				chosenSubmission = int(chosenSubmission)
				if chosenSubmission =='exit':
					break
				if sortBy == 'hot':	
					for submission in reddit.subreddit(chosenSubreddit).hot(limit=chosenSubmission):
						if submissionCount == chosenSubmission:
							viewSubmission(submission.id,chosenSubreddit,sortBy)
						submissionCount = submissionCount + 1
				if sortBy == 'top':	
					for submission in reddit.subreddit(chosenSubreddit).top(limit=chosenSubmission):	
						if submissionCount == chosenSubmission:
							viewSubmission(submission.id,chosenSubreddit,sortBy)
						submissionCount = submissionCount + 1
				
			if menuSelect =='2':
				if sortBy == 'hot':
					chooseSubreddit('top',chosenSubreddit)
				if sortBy == 'top':
					chooseSubreddit('hot',chosenSubreddit)
			if menuSelect == '3':
				chosenSubreddit =""
				chooseSubreddit(sortBy," ")
			if menuSelect == '4':
				chooseSubreddit(sortBy,chosenSubreddit)
Main()




