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

#User Infor
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
			print("")
		print("Please enter a valid option.")

def chooseSubreddit(sortBy,chosenSubreddit):
	submissionIdArray = []
	print(" ")
	if chosenSubreddit == " ":
		chosenSubreddit = input("Enter a subreddit:")
	counter = 1
	print(" ")
	try:

		
		print('{0}{1}{2}{3}{4}'.format("Here are the ", sortBy ," posts in '/R/",chosenSubreddit,"'"))
		print('{0:4.4}|{1:6.6}|{2:8.8}|{3:100.100}'.format("Menu","Score","Comments","Title"))
		if sortBy == 'hot':
			for submission in reddit.subreddit(chosenSubreddit).hot(limit=20):
				print('{0:4}|{1:6}|{2:8}|{3:100.100}'.format(counter,submission.score,submission.num_comments,submission.title))
				submissionIdArray.append(submission.id)
				counter= counter + 1
		if sortBy == 'top':
			for submission in reddit.subreddit(chosenSubreddit).top('all',limit=20):
				print('{0:4}|{1:6}|{2:8}|{3:100.100}'.format(counter,submission.score,submission.num_comments,submission.title))
				submissionIdArray.append(submission.id)
				counter= counter + 1
		if sortBy == 'new':
			for submission in reddit.subreddit(chosenSubreddit).new(limit=20):
				print('{0:4}|{1:6}|{2:8}|{3:100.100}'.format(counter,submission.score,submission.num_comments,submission.title))
				submissionIdArray.append(submission.id)
				counter= counter + 1
	except:
		print("No subreddit with the name of",chosenSubreddit,"found.")
		Main()
	print(" ")
	while True:

		menu = {}
		menu['1']="Choose post to view"
		menu['2']="Change post sorting"
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
				chosenSubmission = int(input("Enter the submission number you want to view, or enter '0' to return to the menu:"))
				if chosenSubmission == '0':
					break
				chosenSubmission = int(chosenSubmission)
				viewSubmission(submissionIdArray[chosenSubmission-1],chosenSubreddit,sortBy)		
			if menuSelect =='2':
				sortBy = input("Please enter sorting view('top','hot','new'):")
				chooseSubreddit(sortBy,chosenSubreddit)
				
			if menuSelect == '3':
				chosenSubreddit =""
				chooseSubreddit(sortBy," ")
			if menuSelect == '4':
				chooseSubreddit(sortBy,chosenSubreddit)

def leaveComment(submission,comment,commentIdArray):
	if comment == 0:
		replyCommentNum = '0'
	else:
		replyCommentNum = int(input("Enter the number of the comment you want to reply too, or Enter '0' to reply to the OP:"))
	try:
		if int(replyCommentNum) == 0:
			commentText = input("Enter your reply:")
			submission.reply(commentText)
		if int(replyCommentNum) == 1:
			commentText = input("Enter your comment:")
			comment.reply(commentText)
		if int(replyCommentNum) > 1:
			commentText = input("Enter your comment:")
			for T in commentIdArray:
				print(T)
			commentID = commentIdArray[int(replyCommentNum)-1]
			print(" ")
			commentID = reddit.comment(commentIdArray[replyCommentNum-1])
			print(reddit.comment(commentIdArray[replyCommentNum-1]))
			commentID.reply(commentText)
			print("Your comment was submitted sucessfully")
	except:
		print("There was an error posting your comment")


def displayReplies(replies,depth,commentNum):
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
	#
	while varY <= (math.ceil(len(commentBody)/100)):
		if varY == 1:
			print('{0:6}{1:2}|{2:5}|{3:9.9}|{4}'.format(depthHolder,commentNum,replies.score,replies.author.name,str(commentBody[(varY-1)*(100-((depth+1)*5)):varY*(100-((depth+1)*5))])))
		else:
			print('{0:6}{1:2}|{2:5}|{3:9.9}|{4}'.format(depthHolder,"  "," ","  ",str(commentBody[(varY-1)*(100-((depth+1)*5)):varY*(100-((depth+1)*5))])))
		varY = varY + 1
	print('{0:6}{1:2}|{2:5}|{3:9}|{4}'.format(depthHolder,'  ','_____','_________',widthHolder))
	
def commentMenu(sortBy,chosenSubreddit,submission,comment,commentIdArray):
	userNext = input("'Enter','Back','Menu','Comment':")
	if userNext == 'Menu':
		chooseSubreddit(sortBy,chosenSubreddit)
	
	if userNext == 'Back':
		displayLastComment(lineCount)
	if userNext == 'Comment':
		leaveComment(submission,comment,commentIdArray)
		print(comment)

def viewSubmission(subId,chosenSubreddit,sortBy):
	submission = reddit.submission(id=subId)
	#print('{0:6}|{1:9}|{2:10.10}|{3:11}{4:89.89}'.format("Score","Author","Comment","Post Title:",submission.title))
	varX = 1
	while varX <= (math.ceil(len(submission.title)/100)):
			if varX == 1:
				print('{0:6}|{1:9.9}|{2:97.97}'.format("Score","Author",str(submission.title[(varX-1)*97:varX*97])))
			else:
				print('{0:6}|{1:9}|{2:100}'.format(" "," ",str(submission.title[(varX-1)*97:varX*97])))
			varX = varX + 1
	VarX=1
	if submission.selftext:
		subText = body = str(submission.selftext).replace('\n','')
		while varX <= (math.ceil(len(subText)/100)):
				if varX == 1:
					print('{0:6}|{1:9.9}|{2:97.97}'.format(" "," ",str(subText[(varX-1)*97:varX*97])))
				else:
					print('{0:6}|{1:9}|{2:100}'.format(" "," ",str(subText[(varX-1)*97:varX*97])))
				varX = varX + 1

	lineCount = 1
	x = 1
	for comment in submission.comments:
		commentIdArray = []
		if isinstance(comment, MoreComments):
			continue
		if not comment.author:
			continue
		lineCount = lineCount + 1
		body = str(comment.body).replace('\n','')
		varX = 1
		commentNum = 1
		#This logic splits comments longer than 100 characters into multiples lines
		#It allows us to keep the formatting without longer comments running onto multiples lines
		#
		#This section displays the top level comments only. The format is a little different then replies
		print('{0:6}.{1:9}.{2:100.100}'.format('______','_________','______________________________________________________________________________________________________'))#i removed 3
		while varX <= (math.ceil(len(body)/100)):
			if varX == 1:
				print('{0:2}{1:4}|{2:9.9}|{3:97.97}'.format(commentNum,comment.score,comment.author.name,str(body[(varX-1)*97:varX*97])))
			else:
				print('{0:6}|{1:9}|{2:100}'.format(" "," ",str(body[(varX-1)*97:varX*97])))
			varX = varX + 1
			print('{0:6}|{1:9}|{2:100.100}'.format('______','_________','_________________________________________________________________________________________________________'))	
		commentIdArray.append(comment.id)
		for replies in comment.replies:
			depth = 1
			if isinstance(replies, MoreComments):
				continue
			if not replies.author:
				continue
			commentNum = commentNum + 1 
			commentIdArray.append(replies.id)
			displayReplies(replies,depth,commentNum)
			for children in replies.replies:
				depth = 2
				if isinstance(children, MoreComments):
					continue
				if not children.author:
					continue
				commentNum = commentNum + 1 
				commentIdArray.append(children.id)
				displayReplies(children,depth,commentNum)
				for toddler in children.replies:
					depth = 3
					if isinstance(toddler, MoreComments):
						continue
					if not toddler.author:
						continue
					commentNum = commentNum + 1
					commentIdArray.append(toddler.id)
					displayReplies(toddler,depth,commentNum)
					for baby in toddler.replies:
						depth = 4
						if isinstance(baby, MoreComments):
							continue
						if not baby.author:
							continue
						commentNum = commentNum + 1
						commentIdArray.append(baby.id)
						displayReplies(baby,depth,commentNum)
		print(" ")
		commentMenu(sortBy,chosenSubreddit,submission,comment,commentIdArray)
		lineCount = 1
		x = x + 1
	print(" ")
	commentMenu(sortBy,chosenSubreddit,submission,0,commentIdArray)

Main()