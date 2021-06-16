from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import pandas as pd

options = webdriver.ChromeOptions()


# Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

with webdriver.Chrome(
        executable_path="C:\\Users\\Mike\\Google Drive\\Code\\Springboard\\Springboard\\capstones\\Kaggle_DataScienceJobs\\Kaggle-Glassdoor-andresionek\\chromedriver.exe",
        options=options) as driver:

    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=data%20scientist&locT=C&locId=1140039'

    driver.get(url)

    # driver.current_url

    # react-job-listing css-wp148e eigr9kq3
    # test = driver.find_element(By.ID, "react-job-listing css-wp148e eigr9kq3")
    # test = driver.find_elements_by_css_selector("#react-job-listing css-wp148e eigr9kq3 li")
    # element = driver.findElements(By.xpath("//[starts-with(@id, ‘react-job-listing’)]")
    #element = driver.findElement(By.xpath("//div[contains(text(),'react-job-listing')]"))
    job_buttons = driver.find_elements_by_class_name("jl")

    print('test')