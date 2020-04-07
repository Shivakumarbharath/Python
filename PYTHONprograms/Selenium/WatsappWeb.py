from selenium import webdriver


driver=webdriver.Chrome(executable_path='C:\Webdrivers\80\chromedriver')

driver.get('https://web.whatsapp.com/')

name=input('Enter the name of user')

ms=input("Enter your message")
count=int(input('How many times'))

input('Enter any key after scan the qr code')

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()


msg_box=driver.find_element_by_class_name('_1Plpp')



for i in range(count):
    msg_box.send_keys(ms)
    button=driver.find_element_by_class_name('_35EW6')
    button.click()


print("workdone")


'''


msgs=[]
for e in range(cnt):
    msg=input("Enter the msg ")
    msgs.append(msg)



input('Enter any key after scan the qr code')

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()


msg_box=driver.find_element_by_class_name('_1Plpp')



for msg in msgs:
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('_35EW6')
    button.click()

'''