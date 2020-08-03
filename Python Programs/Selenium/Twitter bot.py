from selenium import webdriver

content=input("Enter the hashtag").replace(' ','\n')
driver=webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver')
driver.get('https://twitter.com/login')

name='hruthik_999'
pw='Hruthik@2001'

uname=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
uname.send_keys(name)

pwe=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
pwe.send_keys(pw)

login=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
login.click()
#happening=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
#happening.send_keys(content)

for i in range(15):
    happening=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    happening.send_keys(content)
    tweet=driver.find_element_by_class_name('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div')
    tweet.click()

#PromoteStudentsSaveFuture #promotedegreestudents



