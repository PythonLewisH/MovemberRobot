import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
os.environ

import time
import random

# List of potential tweets

TWEETS = ["I am a bot driven by purpose! Please donate to my #Movember efforts and help me change the face of men’s "
          "health. https://movember.com/m/14759858?mc=1 ",
          "Prostate cancer is the second most common cancer in men worldwide. Please donate to my "
          "#Movember efforts to change this statistic and support men's health "
          "https://movember.com/m/14759858?mc=1 ", "Testicular "
                                                   "cancer is the "
                                                   "most common cancer in "
                                                   "men under 40. Please "
                                                   "donate to my #Movember "
                                                   "efforts to change this "
                                                   "statistic and support "
                                                   "men's health. https://movember.com/m/14759858?mc=1",
          "Mental health matters. #Movember is working to help men stay mentally healthy, but they can’t do it alone. "
          "Please donate to my Movember efforts and support men's health. https://movember.com/m/14759858?mc=1"]

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


service = Service("/Users/LewisHudson/Desktop/Development/chromedriver")
driver = webdriver.Chrome(service=service)


def login(username, password):
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)
    username_entry = driver.find_element(By.NAME, 'text')
    username_entry.send_keys(username)
    username_entry.send_keys(Keys.ENTER)
    time.sleep(5)
    password_entry = driver.find_element(By.NAME, 'password')
    password_entry.send_keys(password)
    password_entry.send_keys(Keys.ENTER)


def random_tweet():
    # Find top 3 trending hashtags
    time.sleep(5)
    driver.get("https://twitter.com/explore")
    time.sleep(5)
    trending = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div['
                                   '2]/nav/div/div[2]/div/div[2]/a/div/span')
    time.sleep(2)
    trending.click()
    time.sleep(2)

    trending_1 = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div['
                                     '2]/div/section/div/div/div[3]/div/div/div/div[2]/span')
    first_hashtag = trending_1.text.replace('#', '')
    first_hashtag = first_hashtag.replace(' ', '')

    trending_2 = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div['
                                     '2]/div/section/div/div/div[4]/div/div/div/div[2]/span')
    time.sleep(2)
    second_hashtag = trending_2.text.replace('#', '')
    second_hashtag = second_hashtag.replace(' ', '')

    trending_3 = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div['
                                     '2]/div/section/div/div/div[5]/div/div/div/div[2]/span')
    time.sleep(2)
    third_hashtag = trending_3.text.replace('#', '')
    third_hashtag = third_hashtag.replace(' ', '')

    # Write and send random tweet with hashtags
    driver.get("https://twitter.com/compose/tweet")
    time.sleep(5)
    new_tweet = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                    '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div['
                                    '1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
                                    '2]/div/div/div/div/span/br')
    new_tweet.send_keys(f"{random.choice(TWEETS)} #{first_hashtag} #{second_hashtag} #{third_hashtag} ")
    time.sleep(5)
    post_tweet = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div["
                                     "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div["
                                     "2]/div[4]")
    post_tweet.click()
    time.sleep(5)


def tweet_stat():
    file = open("stats.txt")
    contents = file.read()
    stats = contents.splitlines()
    n = len(stats)
    random_no = random.randrange(0, n - 1)
    driver.get("https://twitter.com/compose/tweet")
    time.sleep(5)
    new_tweet = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                    '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div['
                                    '1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
                                    '2]/div/div/div/div/span/br')
    new_tweet.send_keys(f"{stats[random_no]} #Movember")
    time.sleep(5)
    # Using JS to click here as above method didn't work???
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,
                                                                       "/html/body/div[1]/div/div/div[1]/div["
                                                                       "2]/div/div/div/div/div/div[2]/div[ "
                                                                       "2]/div/div/div/div[3]/div/div["
                                                                       "1]/div/div/div/div/div[2]/div[3]/div/div/div[ "
                                                                       "2]/div[4]"))

    time.sleep(5)


def logout():
    driver.get("https://twitter.com/logout")
    time.sleep(5)
    logout_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div['
                                                  '2]/div[1]')
    logout_button.click()
    time.sleep(5)


while True:
    login(USERNAME, PASSWORD)
    time.sleep(5)
    random_tweet()
    time.sleep(5)
    tweet_stat()
    time.sleep(5)
    logout()
    time.sleep(1800)
