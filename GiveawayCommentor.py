import random
import praw
import time
import re
from Login import Login

r = praw.Reddit('Respond to giveaways in /r/dogecoin'
                'by /u/echocage for /u/quantumcinematic')
username = 'Example Username'
r.login(username = username,password = Login(username))

already_done = []

messages = ["Thanks!", "Thanks so much!", "Thanks for doing this", "That's really nice of you to do a giveaway!"]  # Just add each new message in " " and separated by commas

def alreadyReminded(list):
        for i in list:
            if i.author.__str__().__eq__(username):
                return True
        return False


while True:
    try:

        subreddit = r.get_subreddit('dogecoin')
        posts = subreddit.get_new()
        for submission in posts:
            if not already_done.__contains__(submission):
                if re.search('(give(ing)? ?away)', submission.title.lower()) != None:
                    if not alreadyReminded(submission.comments):
                        currentMessage= random.choice(messages)
                        if re.match('number',submission.selftext) != None:
                            currentMessage+= '... errr... 12'
                        submission.add_comment(currentMessage)
                        print currentMessage , submission
                        time.sleep(2)
                    already_done.append(submission)
        time.sleep(5)



    except praw.errors.RateLimitExceeded,ex:
        try:
            start = ex.message[ex.message.index(' in ')+4:]
            length = start[:start.index(' ')]

            if (ex.message.find('minute') != -1):
                print "Limited, trying again in "+length+" minutes"
                time.sleep(int(length)*60+.05)
            else:
                print "Limited, trying again in "+length+" seconds"
                time.sleep(int(length)+1)
        except Exception, ex:
            print "Limited, trying again in 10 minutes"
            time.sleep(600+.05)
    except:
        None
