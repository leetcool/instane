#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.keys import Keys
import time
import sys
import waiter
import itertools
import random
from art import *
import getopt
import json
import pickle
import requests
import re
import urllib3
import os
import socket
import string
from selenium.webdriver.common.by import By
CLASS_NAME = By.CLASS_NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINK = By.LINK_TEXT
NAME = By.NAME
PARTIAL_LINK = By.PARTIAL_LINK_TEXT
TAG = By.TAG_NAME
XPATH = By.XPATH
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__author__ = "Manish Pathak"
__license__ = "GPLv3"
__version__ = "1.1-stable"

def banner():
    print("")
    tprint("INSTANE",font="sub-zero",chr_ignore=True)
    print(("""%s %s%s\t# Instagram Bot - Selenium\n    # Coded By Manish Pathak - info@codeawm.com%s
        """ % ('\033[91m', '\033[0m', '\033[93m', '\033[0m')))

class instane():
    def __init__(self):
        self.browser = webdriver.Firefox()
    
    def close_browser(self):
        self.browser.quit()
        
    def cookie_dump(self,username,password):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        usernameInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        pickle.dump( self.browser.get_cookies() , open("instane.pickle","wb"))
        self.browser.quit()
            
    def inject_cookie(self):
        self.browser.get("https://www.instagram.com/")
        cookies = pickle.load(open('instane.pickle', "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.get("https://www.instagram.com/")


    def logout(self):
        ProfileButton = self.browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]')
        ProfileButton.click()
        time.sleep(2)
        LogoutButton = self.browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[5]/div[2]/div[2]/div[2]/div[2]')
        LogoutButton.click()
        time.sleep(5)
        self.browser.quit()

    def load_page(self, url):
        self.browser.get(url)
        time.sleep(3)

    def like(self):
        LikeButtonState = self.browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[3]/section[1]/span[1]/button[1]/div[1]/span[1]/*')
        if "Unlike" in LikeButtonState.get_attribute("aria-label"):
            print("Already Liked")
            pass
        else:
            LatestPostLikeButton = self.browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[3]/section[1]/span[1]/button[1]')
            LatestPostLikeButton.click()
            print('New Like Given')

    def wait_after_interaction(self,wait_time):
        time.sleep(wait_time)

    def close_like_popup(self):
        ClosePostButton = self.browser.find_element_by_xpath('/html[1]/body[1]/div[5]/div[3]/button[1]')
        ClosePostButton.click()

    def comment(self):
        first_part = [] # comment first part holder
        second_part = [] # comment second part holder
        emoji = [] # emoji holder
        with open('one.txt','r') as part_one, open('two.txt','r') as part_two, open('emoji.txt','r') as em:
            part_one_lines = part_one.readlines()
            part_two_lines = part_two.readlines()
            em_lines = em.readlines()
            for line1 in part_one_lines:  
                first_part.append(line1.strip()+' ')
            for line2 in part_two_lines:
                second_part.append(line2.strip()+' ')
            for em in em_lines:
                emoji.append(em.strip())
        selected_first = first_part[random.randint(0, len(first_part)-1)]
        selected_second = second_part[random.randint(0, len(second_part)-1)]
        selected_emoji = emoji[random.randint(0, len(emoji)-1)]
        final_comment = selected_first + selected_second + selected_emoji
        comment_string = final_comment
        try:
            self.browser.find_element_by_class_name('Ypffh').click()
            comment_box= self.browser.find_element_by_class_name('Ypffh')
            time.sleep(2)
            for keys in comment_string:
                comment_box.send_keys(keys)
                time.sleep(random.randint(1,1))
            comment_box.send_keys(Keys.ENTER)
            print('Comment Done')
        except:
            print('Comment Failed')
            return
        return

    def get_followers(self,url):
        latest_followers = []
        enum_sink = self.get_followers_stub(url)
        for follower in enumerate(enum_sink, 1):
            (serial, username) = follower
            latest_followers.append('https://www.instagram.com/'+str(username))
        newbut = self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
        newbut.click()
        #returns 100 recent followers
        return latest_followers
    
    def get_followers_stub(self,url):
        self.browser.get(url)
        FollowersButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        FollowersButton.click()
        waiter.find_element(self.browser, "//div[@role='dialog']", by=XPATH)
        allfoll = int(100)
        follower_css = "ul div li:nth-child({}) a.notranslate"
        try:
            for group in itertools.count(start=1, step=12):
                for follower_index in range(group, group + 12):
                    if follower_index > allfoll:
                        raise StopIteration
                    yield waiter.find_element(self.browser, follower_css.format(follower_index)).text
                last_follower = waiter.find_element(self.browser, follower_css.format(group+11))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", last_follower)
        except StopIteration:
            return
    
    def hashtags_photos(self, hashtag):
        photo_hrefs = []
        self.browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for _ in range(1, 7):
            try:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs_hooks = self.browser.find_elements_by_tag_name('a')
                hrefs_hooks = [elem.get_attribute('href') for elem in hrefs_hooks
                                    if '.com/p/' in elem.get_attribute('href')]
                [photo_hrefs.append(href) for href in hrefs_hooks if href not in photo_hrefs]
            except Exception:
                continue
        return photo_hrefs[10:] #return only most recent no need of pupular posts

    def is_profile_private(self, url):
        private_profile = None
        self.browser.get(url)
        time.sleep(3)
        try:
            PrivateHead = self.browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[1]/h2[1]').text
        except:
            PrivateHead = 'NoPriv'

        if 'Private' in PrivateHead:
            private_profile = True
            return
        else:
            private_profile = False
        return private_profile

    def get_posts_link_from_profile(self):
        #self.browser.get(url)
        post_hrefs = []
        try:
            hrefs_hooks = self.browser.find_elements_by_tag_name('a')
            hrefs_hooks = [elem.get_attribute('href') for elem in hrefs_hooks
                                if '.com/p/' in elem.get_attribute('href')]
            [post_hrefs.append(href) for href in hrefs_hooks if href not in post_hrefs]
        except Exception:
            return
        return post_hrefs[:3] #:3 to return first 3 posts


######################### END OF CLASS ######################

def main():
    banner()
    comment_counter = ''
    comment = False
    
    userinput = input('Select a method\n \n[1] Dump Cookie\n[2] Check Cookie\n[3] Hash Snooper (188 Links Approx.)\n[4] Profile Snooper (100 Recent Followers )\n\nEnter your choice : ')
    
    if userinput == '1':
        username = input("\n\nPlease enter username : ")
        password = input("\n\nPlease enter password : ")
        bot = instane()
        bot.cookie_dump(username,password)
    elif userinput == '2':
        bot = instane()
        bot.inject_cookie()
        bot.close_browser()
    elif userinput == '3':
        selectedhash = input("\nPlease enter hashtag (without #) : ")
        comment_switch = input("\nEnable comments ? (y/N) : ")
        
        if comment_switch == 'y':
            comment = True
            comment_counter = int(input("\nComment, after how many likes ? (Safe 9) : "))
        else:
            comment = False
        wait_time = int(input("\nHow many seconds to wait after each like ? (Enter only number) : "))
        bot = instane()
        bot.inject_cookie()
        urls = bot.hashtags_photos(selectedhash)
        print('\n'+str(len(urls))+' URLs Selected.')
        counter = 0
        for url in urls:
            try:
                bot.load_page(url)
                bot.like()
                if counter == 0 and comment is True:
                    bot.comment()
                counter = counter + 1
                if counter == comment_counter+1:
                    counter = 0
            except:
                pass
            time.sleep(wait_time)
            
        bot.close_browser()
        
    elif userinput == '4':
        selectedprofile = input("\nPlease enter username : ")
        comment_switch = input("\nEnable comments ? (y/N) : ")
        
        if comment_switch == 'y':
            comment = True
        else:
            comment = False
        wait_time = int(input("\nHow many seconds to wait after each like ? (Enter only number) : "))
        bot = instane()
        bot.inject_cookie()
        followers = bot.get_followers('https://www.instagram.com/'+selectedprofile)
        print('\n'+str(len(followers))+' Followers Selected.')
        for follower in followers:
            try:
                bot.load_page(follower)
                profile_posts = bot.get_posts_link_from_profile()
                print('Recent '+str(len(profile_posts))+'Posts Selected')
                counter = 0
                for post in profile_posts:
                    try:
                        bot.load_page(post)
                        bot.like()
                        if counter == 0 and comment is True:
                            bot.comment()
                        counter = counter + 1
                        if counter == 3:
                            counter = 0     #Reset Comment Counter
                    except:
                        pass
                    time.sleep(wait_time)
            except:
                print('Exception raised! Error with this profile.')
                pass
            
        bot.close_browser()
    sys.exit()
        
    
if __name__ == '__main__':
    main()
