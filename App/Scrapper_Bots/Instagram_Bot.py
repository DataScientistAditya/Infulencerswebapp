#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget


def Insta_Bot(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    file_path = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(file_path,options=chrome_options)
    driver.get("https://www.instagram.com")
    
    driver.implicitly_wait(50)


    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    username.send_keys("mightyneuronttt")

    password.clear()
    password.send_keys("#Aditya22")

    Login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


    alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    try:
        alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except:
        pass

    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()
    keyword = url
    searchbox.send_keys(keyword)

    my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[0:] + "/')]")))

    my_link.click()

    import time
    n_scrolls = 3
    for i in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    images = driver.find_elements_by_tag_name('img')
    try:
        Is_Varified = driver.find_element_by_xpath("//span[@title='Verified']").text
    except:
        Is_Varified = "Not Varified"
    Profile_Description = driver.find_element_by_class_name('-vDIg').text
    Number_of_Posts = driver.find_element_by_class_name('g47SY').text
    followers = driver.find_element_by_xpath("//a[@tabindex='0']").text

    images = [image.get_attribute('src') for image in images]
    images = images[:-2] #slicing-off IG logo and Profile picture

    print('Number of scraped images:', len(images))

    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

    print('Found ' + str(len(anchors)) + ' links to images')

    images = []
    Post_Comments = []
    Like=[]
    for a in anchors[0:5]:
        driver.get(a)
        time.sleep(5)
        img = driver.find_elements_by_tag_name('img')
        try:
            Spans = driver.find_element_by_class_name("C4VMK").text
            Likes = driver.find_element_by_class_name("Nm9Fw").text
            Like.append(Likes)
            Post_Comments.append(Spans)
        except:
            continue
        img = [i.get_attribute('src') for i in img]
        images.append(img)
        
    List_Lines = []
    for tags in Post_Comments:
        Found = str(tags).find("#")
        if Found>-1:
            #print(tags)
            Splt = str(tags).splitlines()
            List_Lines.append(Splt)

    Dict = {}
    Dict["Is_Varified"]=Is_Varified
    Dict["Profile_Description"]=Profile_Description
    Dict["Number_of_Posts"]=Number_of_Posts
    Dict["Likes"] = Like
    Dict["followers"]=followers
    Dict["Post_Comments"]=Post_Comments[0:4]
    Dict["images"]=images
    Dict["Tag_Posts"]=List_Lines

    driver.quit()
    return Dict





