import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

time.sleep(12)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span/span").click()

time.sleep(1)
input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

time.sleep(1)
x=1
while x<20:
    x=x+1
    time.sleep(1)
    input.send_keys("hi there")
    input.send_keys(Keys.ENTER)

driver.quit()