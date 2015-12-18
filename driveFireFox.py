
from selenium import webdriver
import random
import os, sys, time, datetime

profile = webdriver.FirefoxProfile("data/testdata/")

driver = webdriver.Firefox(firefox_profile=profile)

profiletmp = driver.firefox_profile.path
print profiletmp

mydir = os.path.join("data/testdata/", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.mkdir(mydir)




with open("data/validUrls.txt") as f:
    urllist = f.read().splitlines()


for i in xrange(1000):

    driver.get("http://{}".format(random.choice(urllist)))


    time.sleep(3)
driver.quit()
mydir = os.path.join("data/testdata/", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.mkdir(mydir)

os.system("cp -R {} {}".format(profiletmp,mydir))
