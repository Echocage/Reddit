import time
import re
import traceback
import praw
import sys
from requests.packages.urllib3.exceptions import HTTPError
from Login import Login
r = praw.Reddit('Respond to users on r/shadowbanned'
                'by /u/echocage')
username = 'ShadowBanCheckBot'
r.login(username = username,password= Login(username))
r.is_logged_in()
already_done = []
bannedMessage = """ You're shadowbanned.

The only thing that you can do is to [message the admins](http://www.reddit.com/message/compose?to=%2Fr%2Freddit.com)  *using your shadowbanned account* and patiently wait for a response.

They don't always respond to the first message. Be mildly persistent but don't message them more than once a day.

*Be honest.* Your activity, including PMs, private subreddits, alt accounts and voting history are utterly transparent to them.

Read up on possible rules you may have violated:
http://www.reddit.com/rules. **Read them all and click every link.**

[The details of some are not as obvious as others.](http://www.reddit.com/r/ShadowBan/comments/1x92jy/an_unofficial_guide_on_how_to_avoid_being/)



***I AM A BOT***, however real people will be along to answer any subsequent questions you may still have so feel free to leave a comment anyway.


If you do have success getting your account back in good standing, the author would appreciate that you reply [to this thread](http://www.reddit.com/r/ShadowBan/comments/1vyaa2/a_guide_to_getting_unshadowbanned_sticky_maybe/cez1fl3) letting him know that it helped.
Good luck.

    /r/Shadowban Copypasta version 2.2.1"""

notBannedMessage = """You're not shadowbanned.

You can prove that to yourself by clicking your own username to go to your overview then logging out. You should still see your overview. If you were shadowbanned, it would go to [Reddit's 404 page](http://www.reddit.com/user/healthyyi).

If you're asking because something you posted isn't showing up in /r/<subreddit>/new, (or in your overview *when you log out*) [click here](http://www.reddit.com/wiki/faq#wiki_why_don.27t_my_submissions_show_up_on_the_new_page.3F) to learn  the procedure for dealing with the spam filter.

**Do not delete & resubmit them** as this will train the spam filter to continue doing this. You may have to repeat the procedure until the spam filter learns that your posts are okay.
"""
def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
def isShadowbanned(user):
    try:
        r.get_redditor(user)
        return False
    except:
        return True

subreddit = r.get_subreddit('ShadowBan')
posts = subreddit.get_new()
while True:
    try:
        posts = subreddit.get_new()
        for submission in posts:
                if not submission in already_done\
                   and not len(submission.comments) \
                   and re.search('((i am)|(am) (i)|(shadow) ?(ban(ned)?)\?)|(test)', submission.title.lower()) is not None:
                    if isShadowbanned(submission.author):
                        submission.add_comment(bannedMessage)
                        submission.set_flair('TRUE','true')
                    else:
                        submission.add_comment(notBannedMessage)
                        submission.set_flair('FALSE','false')
                    print "[Shadowbanned: "+ isShadowbanned(submission.author).__str__()+ "]", submission.title
                    already_done.append(submission)
        time.sleep(5)
    except praw.errors.RateLimitExceeded as err:
        print "Rate Limit Exceeded:\n" + str(err), sys.stderr
        time.sleep(err.sleep_time0+.05)
    except HTTPError:
        print 'Http Error...'
    except:
        print traceback.format_exc()



