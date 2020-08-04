from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # to use the Key board input


def MainSearch(search2):
    print("Processing")
    driver = webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver')
    driver.get('https://www.google.com/')
    search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(search2)
    button = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    button.click()
    driver.find_element_by_tag_name("cite").click()


root = Tk()
root.title("Search For Your Query")

root.iconbitmap('E:\Bharath\Python\PYTHONprograms\Selenium\Custom-Icon-Design-Flatastic-5-Search-globe.ico')

label = Label(root, text="What Should be searched?", padx=10, pady=10, fg='blue', font=('ariel', 15, 'bold'))
label.grid(row=1, column=1)

e = Entry(root, width=40, borderwidth=3)
e.grid(row=1, column=2, padx=15, pady=15, columnspan=2)

opt = StringVar()
opt.set(None)
frame = LabelFrame(root, text="Get the Solution From ?", padx=10, pady=10, font=('ariel', 10, 'bold'))
frame.grid(row=2, column=1, padx=30, pady=30)
Radiobutton(frame, text="Stack Overflow", variable=opt, value=" Stack Overflow").pack(anchor=W)
Radiobutton(frame, text="Python Documentation", variable=opt, value=" Python Documentation").pack(anchor=W)
btn = Button(root, text="Submit", relief=GROOVE, fg='blue', command=lambda: MainSearch(e.get() + opt.get())).grid(row=2,
                                                                                                                  padx=0,
                                                                                                                  pady=0,
                                                                                                                  column=3)
qbtn = Button(root, text="Quit", relief=GROOVE, fg='red', command=root.quit)

qbtn.grid(row=2, column=2, columnspan=2)
# btn.grid(row=3,column=1)
root.mainloop()
