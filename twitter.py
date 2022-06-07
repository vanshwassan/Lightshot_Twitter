import tweepy
import config
import time
import lightshot

auth = tweepy.OAuthHandler(config.API_Key, config.API_Key_Secret)
auth.set_access_token(config.Access_Token, config.Access_Token_Secret)
api = tweepy.API(auth)

def postTweet():
    lightshot.scraper()
    time.sleep(2)
    img = "img.png"
    media = api.media_upload(img)
    time.sleep(2)
    if str(media.size) == 5345:
        print("The screenshot was removed!")
        postTweet()
    else:
        api.update_status(status='', media_ids=[media.media_id])
        print("Tweet Posted!")
        print("The media ID is : " + media.media_id_string)
        print("The size of the file is : " + str(media.size) + " bytes")

    ## Change the time (in seconds) to update the frequency at which it scrapes the screenshots and tweets it.
    time.sleep(700)
    
    postTweet()

postTweet()