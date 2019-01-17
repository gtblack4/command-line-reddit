#Enter your Client ID, Secret, Username, and password here
#In order to optain a Client ID and Secret you must register this application with Reddit
#You can add it as a script application here https://ssl.reddit.com/prefs/apps/
import praw 
reddit = praw.Reddit(client_id='YOUR CLIENT ID',
 	client_secret='YOUR CLIENT SECRET',	
 	user_agent='YOUR USER AGENT',
 	username='YOUR USERNAME',
 	password='YOUR PASSWORD')
