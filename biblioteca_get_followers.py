#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import tweepy
from bs4 import BeautifulSoup


# In[2]:


def get_facebook_followers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    followers = soup.find("div",text=re.compile('pessoas estão seguindo isso')).text
    followers = followers.split(' ')[0].replace('.','')    
    return int(followers)


# In[3]:


def get_facebook_likes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    likes = soup.find("div",text=re.compile('pessoas curtiram isso')).text
    likes = likes.split(' ')[0].replace('.','') 
    return int(likes)


# In[4]:


def get_twitter_followers(user):
    auth = tweepy.OAuthHandler('46pvnSwIVylfWepbPsP4433wL', 
                           'xWDPHaUkk0ub93qj1DaYgJcO8QtkPUhNFIE7uBAvzbSVLLpLzR')
    auth.set_access_token('1952916806-9WbU9ROPLd4aVPprQZqWJhaW4RSXrBw4oK8A4Ow',
        'gW5iuYPtrTxVhPmQxBemsKz6jCAOqbYx1fT0ewKHFyAkG')
    twitter = tweepy.API(auth)
    followers = twitter.get_user(user).followers_count
    return followers


# In[5]:


def get_instagram_followers(url):
    r = requests.get(url).text
    followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)
    return int(followers)


# In[6]:


user = 'user'
url_face = 'https://www.facebook.com/'+ user
url_insta = "https://www.instagram.com/" + user


# In[7]:


num_seguidores_face = get_facebook_followers(url_face)


# In[8]:


num_seguidores_twitter = get_twitter_followers(user)


# In[9]:


num_seguidores_instagram = get_instagram_followers(url_insta)


# In[10]:


num_seguidores_face


# In[11]:


num_seguidores_twitter


# In[12]:


num_seguidores_instagram


# In[ ]:




