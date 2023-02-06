#https://sites.google.com/chromium.org/driver/?pli=1
from selenium import wepdriver 
PATH = " C:\chromedriver_win32"
driver = wepdriver.chrome(PATH)
driver.get("https://www.mailinator.com/site/home-application-minimal/mailinator-blog/")
