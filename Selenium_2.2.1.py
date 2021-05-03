from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)
    z = str(x + y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)

    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

#end
