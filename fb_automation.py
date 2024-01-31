import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import re
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
crome_path = r"D:\JSP\Web scrapping\chromedriver.exe"
driver = webdriver.Chrome(crome_path,chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)

while True:
    email = input("Enter your FB E-mail: ")
    password = input("Enter your FB password: ")
    url = "https://www.facebook.com/"
    driver.get(url)
    time.sleep(3)
    
    try:
        
        driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        # Home_click
        driver.find_element(By.XPATH,"//a[@aria-label='Home']").click()
        print("Login Succesful")
        break
    except:
        print("Invalid Credentials")
        
#post =input("Enter your post text: ")
#img_vid = input("Enter your image/video path without Quotes (" "): ")  

time.sleep(10)
# whats on your mind
driver.find_element(By.XPATH, "//span[contains(text(), \"What's on your mind\")]").click()
time.sleep(5)
# click to select public/friends
#element = driver.find_element(By.XPATH, "//div[@class='x6s0dn4 x78zum5 xl56j7k']")
#driver.execute_script("arguments[0].click();", element)

post =input("Enter your post text: ")
pic_post = str(input("Do You want to post pic/video? Enter yes or no: ")).lower()
if pic_post=="yes":
    img_vid = input("Enter your image/video path without Quotes (' '): ")  
else:
    pass

# while True:
#     post_type = input("Enter to whom you want to post \n1. Public  \n2. Friends \nselect 1 or 2 :") 
#     if post_type == "1":
        
#         # Public
#         driver.find_element(By.XPATH, "//span[text()='Anyone on or off Facebook']").click()
#         break
#     elif post_type == "2":
        
#         # Friends
#         driver.find_element(By.XPATH,"//span[text()='Your friends on Facebook']").click()
#         break
#     else:
#         print("Please Enter 1 or 2")


# time.sleep(3)
# # select and click Done
# driver.find_element(By.XPATH,"//span[text()='Done']").click()
time.sleep(5)
# Post_text
driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']").send_keys(post)
time.sleep(2)

# click pic/video
driver.find_element(By.XPATH,"//div[@aria-label='Photo/video']").click()
time.sleep(2)
# Post img/video
if pic_post=="yes":

    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(fr"{img_vid}")
else:
    pass

time.sleep(3)
# Post
driver.find_element(By.XPATH, "//span[text()='Post']").click()
while True:
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Posting')]")
        time.sleep(1)  # Wait for 1 second before checking again
    except NoSuchElementException:
        print("'Posting' text is no longer present!")
        break 
time.sleep(10)
print("Post Completed")
# Logout
driver.find_element(By.XPATH, "//div[@class='x78zum5 x1n2onr6']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Log out']").click()
time.sleep(3)
driver.close()