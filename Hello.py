from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

assert len(sys.argv) == 2
if sys.argv[1] == "64":
    driver = webdriver.Chrome("chromedriver_linux64/chromedriver")
else:
    driver = webdriver.Chrome("chromedriver_linux32/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()