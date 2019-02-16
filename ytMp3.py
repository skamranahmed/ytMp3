import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome('/Users/syedkamrnahmed/Desktop/Scrape/chromedriver', chrome_options=options)
chrome_options = Options()
chrome_options.add_argument("--headless")

# driver = webdriver.Chrome('/Users/syedkamrnahmed/Desktop/Scrape/chromedriver')

yt_link = str(input("Enter the youtube url :\n"))



driver.get("https://ytmp3.cc/")

driver.find_element_by_xpath('//*[@id="input"]').send_keys(yt_link)
driver.find_element_by_xpath('//*[@id="submit"]').send_keys(Keys.RETURN)
print("Loading")
time.sleep(4)
# driver.find_element_by_xpath('//*[@id="download"]').send_keys(Keys.RETURN)

element = driver.find_element_by_xpath('//*[@id="download"]')
download_link = element.get_attribute('href')
video_name = driver.find_element_by_xpath('//*[@id="title"]')

name_of_the_video = video_name.text

name_of_the_video = name_of_the_video+".mp3"



# print(download_link)
# print(name_of_video)


try:
    print("Downloading started ...\n")
    urllib.request.urlretrieve(download_link,name_of_the_video)
    print("Download complete")

except Exception as e:
    print(e)