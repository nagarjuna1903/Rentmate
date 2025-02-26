import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get Facebook Credentials from Environment Variables
FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")
GROUP_NAME = "Your Group Name"

# Setup Selenium WebDriver in Headless Mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to Log in to Facebook
def facebook_login():
    driver.get("https://www.facebook.com/")
    time.sleep(5)
    
    driver.find_element(By.ID, "email").send_keys(FB_EMAIL)
    driver.find_element(By.ID, "pass").send_keys(FB_PASSWORD)
    driver.find_element(By.ID, "pass").send_keys(Keys.RETURN)
    
    time.sleep(5)

# Function to Share the Latest Post to a Group
def share_new_post():
    driver.get("https://www.facebook.com/me/")
    time.sleep(5)

    posts = driver.find_elements(By.XPATH, "//div[contains(@aria-label, 'Actions for this post')]")
    
    if posts:
        latest_post = posts[0]
        latest_post.click()
        time.sleep(3)
        
        share_button = driver.find_element(By.XPATH, "//span[text()='Share']")
        share_button.click()
        time.sleep(2)
        
        share_to_group = driver.find_element(By.XPATH, "//span[contains(text(), 'Share to a Group')]")
        share_to_group.click()
        time.sleep(2)
        
        group_search = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search for groups')]")
        group_search.send_keys(GROUP_NAME)
        time.sleep(2)
        
        group_search.send_keys(Keys.RETURN)
        time.sleep(2)
        
        post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
        post_button.click()
        
        print("Post shared successfully!")
    else:
        print("No new post found!")

# Run the Functions
facebook_login()
share_new_post()

# Close Browser
driver.quit()