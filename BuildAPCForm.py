import time
import traceback
import praw
import sys
from Login import Login
r = praw.Reddit('Reminds users to use form for submissions on r/buildapcforme '
                'by /u/echocage')
username = 'BuildAPC4MeBot'
r.login(username = username,password = Login(username))
r.is_logged_in()
already_done = []
message = """Looks like you might have forgotten to fill out the form in the sidebar [[Link here](http://www.reddit.com/r/buildapcforme/submit?selftext=true&text=*%20What%20will%20you%20be%20doing%20with%20this%20PC?%20Be%20as%20specific%20as%20possible.%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20What%20is%20your%20maximum%20budget%20before%20rebates/shipping/taxes?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20When%20do%20you%20plan%20on%20building/buying%20the%20PC?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20What,%20exactly,%20do%20you%20need%20included%20in%20the%20budget?%20[Tower/OS/monitor/keyboard/mouse/etc]%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Which%20country%20[and%20state/province]%20will%20you%20be%20purchasing%20the%20parts%20in?%20If%20you%27re%20in%20US,%20do%20you%20have%20access%20to%20a%20Microcenter%20location?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20If%20reusing%20any%20parts%20[including%20monitor[s]/keyboard/mouse/etc],%20what%20parts%20will%20you%20be%20reusing?%20Brands%20and%20models%20are%20appreciated.%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Will%20you%20be%20overclocking?%20If%20yes,%20are%20you%20interested%20in%20overclocking%20right%20away,%20or%20down%20the%20line?%20CPU%20and/or%20GPU?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Are%20there%20any%20specific%20features%20or%20items%20you%20want/need%20in%20the%20build?%20[ex:%20SSD,%20large%20amount%20of%20storage%20or%20a%20RAID%20setup,%20CUDA%20or%20OpenCL%20support,%20etc]%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Do%20you%20have%20any%20specific%20case%20preferences%20[Size%20like%20ITX/microATX/mid-tower/full-tower,%20styles,%20colors,%20window%20or%20not,%20LED%20lighting,%20etc],%20or%20a%20particular%20color%20theme%20preference%20for%20the%20components?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Do%20you%20already%20have%20a%20copy%20of%20Windows%207%20or%208,%20or%20do%20you%20need%20a%20copy%20included%20with%20the%20build?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Extra%20info%20if%20required:)], if you fill it out you'll get a lot more responses and the builds posted will be specific to your needs.

---------------------------
*I am a bot.* """

messageBuildReview ="""Looks like you forgot to fill out the form in the sidebar [[Link here](http://www.reddit.com/r/buildapcforme/submit?selftext=true&text=*%20What%20will%20you%20be%20doing%20with%20this%20PC?%20Be%20as%20specific%20as%20possible.%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20What%20is%20your%20maximum%20budget%20before%20rebates/shipping/taxes?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20When%20do%20you%20plan%20on%20building/buying%20the%20PC?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20What,%20exactly,%20do%20you%20need%20included%20in%20the%20budget?%20[Tower/OS/monitor/keyboard/mouse/etc]%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Which%20country%20[and%20state/province]%20will%20you%20be%20purchasing%20the%20parts%20in?%20If%20you%27re%20in%20US,%20do%20you%20have%20access%20to%20a%20Microcenter%20location?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20If%20reusing%20any%20parts%20[including%20monitor[s]/keyboard/mouse/etc],%20what%20parts%20will%20you%20be%20reusing?%20Brands%20and%20models%20are%20appreciated.%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Will%20you%20be%20overclocking?%20If%20yes,%20are%20you%20interested%20in%20overclocking%20right%20away,%20or%20down%20the%20line?%20CPU%20and/or%20GPU?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Are%20there%20any%20specific%20features%20or%20items%20you%20want/need%20in%20the%20build?%20[ex:%20SSD,%20large%20amount%20of%20storage%20or%20a%20RAID%20setup,%20CUDA%20or%20OpenCL%20support,%20etc]%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Do%20you%20have%20any%20specific%20case%20preferences%20[Size%20like%20ITX/microATX/mid-tower/full-tower,%20styles,%20colors,%20window%20or%20not,%20LED%20lighting,%20etc],%20or%20a%20particular%20color%20theme%20preference%20for%20the%20components?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Do%20you%20already%20have%20a%20copy%20of%20Windows%207%20or%208,%20or%20do%20you%20need%20a%20copy%20included%20with%20the%20build?%20%0A%0A*%20%5BInsert%20answer%20here%5D%20%0A%0A*%20Extra%20info%20if%20required:)].

**Depending on your answers to the questions, the build you posted might be great or horrible for you. It might be totally not what you need and you might be wasting money in an area that you aren't going to need.**
---------------------------
*I am a bot.* """
subreddit = r.get_subreddit('buildapcforme')

while True:
    try:

        posts = subreddit.get_new()

        for submission in posts:
            if not submission in already_done \
               and not 'What will you be doing with this PC?' in submission.selftext  \
               and not 'meta' in submission.title.lower()  \
               and not username.lower() in [str(comment.author).lower() for comment in submission.comments]:
                    i = len([comment for comment in submission.author.get_comments(limit = None) if str(comment.subreddit) == 'buildapcforme'])
                    print submission.author, i
                    if i <= 20:
                        print "Trying to post on" ,submission
                        if 'Type|Item|Price' in submission.selftext or 'pcpartpicker.com' in submission.selftext:
                            submission.add_comment(messageBuildReview)
                        else:
                            submission.add_comment(message)
                        print "Success"
                        time.sleep(5)
                    already_done.append(submission)
        time.sleep(20)
    except praw.errors.RateLimitExc as err:
        print "Rate Limit Exceeded:\n" + str(err), sys.stderr
        time.sleep(err.sleep_time0+.05)
    except:
        print traceback.format_exc()


