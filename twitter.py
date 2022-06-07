import tweepy
import config


auth = tweepy.OAuthHandler(config.API_Key, config.API_Key_Secret)
auth.set_access_token(config.Access_Token, config.Access_Token_Secret)
api = tweepy.API(auth)

api.update_status('tweet')