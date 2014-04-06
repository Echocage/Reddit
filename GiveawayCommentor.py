
import praw
import time
import re

r = praw.Reddit('Respond to giveaways in /r/dogecoin'
                'by /u/quantumcinematic')
r.login(username = 'Example Username',password = 'Example Pass')

already_done  = []

while True:
    try:
        subreddit = r.get_subreddit('dogecoin')
        posts = subreddit.get_new()
        for submission in posts:
            if not already_done.__contains__(submission):
                if re.search('(giveaway)', submission.title.lower()) != None:
                    None


        time.sleep(20)
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
