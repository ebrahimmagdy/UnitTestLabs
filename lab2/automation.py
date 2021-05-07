from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://epiphanietutoring.com")
email = driver.find_element_by_name("username")
password = driver.find_element_by_name("passwd")
btn = driver.find_element_by_class_name("e-Bg")
email.send_keys("userlast")
password.send_keys("Jj12345678_")
btn.click()

proceed_btn=driver.find_element_by_id("proceed-button")
proceed_btn.click()

problem=driver.find_element_by_name("problemName")
equation=driver.find_element_by_name("problemStep")
submitproblem=driver.find_element_by_xpath("//input[@type='SUBMIT' and @value='Begin']")

problem.send_keys("ebrahim_assignment")
equation.send_keys("x+2x+7=3")
submitproblem.click()

driver.back()

driver.implicitly_wait(3)
proceed_btn=driver.find_element_by_id("proceed-button")
proceed_btn.click()

driver.implicitly_wait(3)

driver.find_element_by_xpath("//a[@href='index.html']").click();
driver.close();


