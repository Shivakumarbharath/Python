from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # to use the Key board input

search=input("Enter the error")
search+=' Stack overflow'


driver=webdriver.Chrome(executable_path='C:\Webdrivers\80\chromedriver')

driver.get('https://www.google.com/')
search_bar=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys(search)
button=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
button.click()


driver.find_element_by_tag_name("cite").click()
