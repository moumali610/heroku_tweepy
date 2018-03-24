# Dependencies
import tweepy
import time

# Twitter API Keys
consumer_key = "yLptuAaXk8lfclf4qmwIwEahq"
consumer_secret = "trV35gs663D7FNiI1kgYlLMiyOwLZWynUWHZ7Jo66qXXef7MKz"
access_token = "215954340-Ww1bjJbk2JV4hUV1v23VS5e4DF8Rb1pmH3qeNCyC"
access_token_secret = "ppKCCcJFKgWOWzDUovBX9jQkLWe7hgmgf2lL80q73blRO"

# Quotes to Tweet
quote_list = [
    "Quote 1",
    "Quote 2",
    "Quote 3"]


# Create function for tweeting
def QuoteItUp(quote_num):

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
counter = 0

while(counter < len(quote_list)):
    QuoteItUp(counter)
    time.sleep(60)