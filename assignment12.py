#question1

#Access tokens are the thing that applications use to make API requests on behalf of a user. The access token represents the authorization of a specific application to access specific parts of a user’s data.
from keys import consumer_secret,consumer_key,access_secret,access_token
print(access_token)

#question2

import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
addr3 = socket.gethostbyname('facebook.com')

print(addr1)
print(addr2)
print(addr3)

#question3

from keys import consumer_secret,consumer_key,access_secret,access_token
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
user=api.search('#race3')


#question4

#A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself. Typically a library will only offer one area of functionality (processing images or operating on zip files)

#An API (application programming interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you - the interface to the library.

#question5

from keys import consumer_key,consumer_secret,access_secret,access_token
import  tweepy

oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api= tweepy.API(oauth)
print(api.search("#sanju"))

user=api.get_user('mohit_sharma09')
print(user.screen_name)
print(user.followers_count)



