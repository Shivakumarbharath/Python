from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # to use the Key board input

search1=input("Enter what Should be searched")

def Select(search1):
    print("1.Stack Overflow\n2.Python Documentation")
    s = int(input())

    if s == 1 :

        search1+=' Stack overflow'
        return search1

    elif s==2:
        search1 += ' Python Documentation'
        return search1
    else:
        print("select again")
        Select(search1)

search2=Select(search1)

driver=webdriver.Chrome(executable_path='C:\Webdrivers\80\chromedriver')

driver.get('https://www.google.com/')
search_bar=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys(search2)
button=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
button.click()


driver.find_element_by_tag_name("cite").click()
