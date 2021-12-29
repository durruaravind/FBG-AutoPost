import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random

file = ""
root = Tk()
root.title("FBAutoPost")
root.geometry('960x720')
root.configure(bg = "#03203C")
root.resizable(0,0)
frame = Frame(root, height = 30)
frame.pack(side = TOP)
lbl_title = Label(frame, text = "FACEBOOK GROUP POST AUTOMATION PROJECT", font = "Sans 20", bg = "#207398", width = 300, fg = "WHITE")
lbl_title.pack(fill = X)
l1 = Label(root, text = "USERNAME", bg = "#03203C", fg = "WHITE", font = "Sans 14 bold")
l1.place(x = 120, y = 80)
user_field = Entry(root, width = 50)
user_field.place(x = 360, y = 80)
l2 = Label(root, text = "PASSWORD", bg = "#03203C", fg = "WHITE", font = "Sans 14 bold")
l2.place(x = 120, y = 120)
passw_field = Entry(root, show = "*", width = 50)
passw_field.place(x = 360, y = 120)
l3 = Label(root,text = "GROUP ID(s)",bg = "#03203C", fg = "WHITE", font = "Sans 14 bold")
l3.place(x = 120, y = 160)
msg1 = Text(root, height = 10, width = 40)
msg1.place(x = 360, y = 160)
l4 = Label(root, text = "POST TEXT", bg = "#03203C", fg = "WHITE", font = "Sans 14 bold")
l4.place(x = 120, y = 380)
msg2 = Text(root, height = 10, width = 40)
msg2.place(x = 360, y = 380)
l5 = Label(root, fg = "WHITE", bg = "#03203C", font = "Sans 14 bold")
l5.place(x = 360, y = 660)

# sending the data for execution
def SEND():
    if(user_field.get() == '' or passw_field.get() == '' or  msg1.get("1.0", END) == '' or  msg1.get('1.0', END) == ''):
            messagebox.showinfo("ERROR!", "Fill all details")  
    else:
        m = []
        l = msg1.get("1.0", END)
        if '\n' not in l:
            l = l[:-1]
            m.append(l)
        else:
            m = l.split("\n")
            s = m[-1]
            s = s[1:-1]
            m[-1] = s
        print(m)
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options = options, executable_path = 'C:\Drivers\chromedriver')    
        driver.get('https://www.facebook.com/')
        time.sleep(10)
        while(True):
            try:
                driver.maximize_window()
                time.sleep(5)
                driver.find_element_by_id('email').click()
                driver.find_element_by_id('email').send_keys(user_field.get())
                driver.find_element_by_id('pass').click()
                driver.find_element_by_id('pass').send_keys(passw_field.get())
                driver.find_element_by_id('pass').send_keys(Keys.ENTER)
                break
            except:
                pass
        time.sleep(5)
        i = 0
        while(i<len(m)):
            driver.get('https://www.facebook.com/groups/%s'%(m[i]))
            time.sleep(11)
            postbox = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span"
            Element = driver.find_element_by_xpath(postbox)
            Element.click()
            time.sleep(5)
            pyautogui.typewrite(msg2.get("1.0", END))
            time.sleep(10)
            submit = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div"
            button = driver.find_element_by_xpath(submit)
            button.click()
            root.update()
            l5.configure(text = "%d/%d Tasks completed"%(i+1, (len(m)-1)))
            time.sleep(random.randint(10,20))   # getting a random sleep time before next post execution
            i+= 1

# clearing the contents of the GUI
def CLEAR():
    l5.configure(text = "")
    user_field.delete(first = 0, last = 100)
    passw_field.delete(first = 0, last = 100)
    msg1.delete('1.0', END)
    msg2.delete('1.0', END)

# buttons for the GUI
b1 = Button(root, text = "SEND", bg = "WHITE", font = "Sans 14 bold", activebackground = "WHITE", command = SEND)
b1.place(x = 420, y = 600)
b2 = Button(root, text = "CLEAR", bg = "WHITE", font = "Sans 14 bold", activebackground = "WHITE", command = CLEAR)
b2.place(x = 580, y = 600)
root.mainloop()