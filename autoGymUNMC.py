from selenium import webdriver
import datetime
import win10toast
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

msg = MIMEMultipart()

# Script to send email
sender_email = "sender@gmail.com"
rec_email = "receiver@gmail.com"
password_email = "password12345"
msg['Subject'] = "autoGym Script Successful"

today = datetime.date.today()
bkDate = today + datetime.timedelta(days=3)
bkDateNum = bkDate.strftime("%d")

time = datetime.datetime.now()
time_str = time.strftime("%d-%m-%y %H:%M:%S")

user = "testUser"
password = "password12345"
number = "01234567"
purpose = "Strength Training"
dep = "Computer Science"

# Allows chrome to be headless with chrome version
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get('https://apps.nottingham.edu.my/jw/web/login')

user_textbox = driver.find_element_by_id("j_username")
user_textbox.send_keys(user)

password_textbox = driver.find_element_by_id("j_password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_css_selector("input.form-button")
login_button.click()

driver.get("https://apps.nottingham.edu.my/jw/web/userview/booking/v/_/request")

number_textbox = driver.find_element_by_id("contact_no")
number_textbox.send_keys(number)

purpose_textbox = driver.find_element_by_id("purpose")
purpose_textbox.send_keys(purpose)

slot1 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[8]/div["
                                     "2]/div[2]/div[1]/label[7]/i")
slot1.click()

bkDate_textBox = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[6]/div[2]/div/input")
bkDate_textBox.click()

bkDate_input = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/a[text()=%s]" % bkDateNum)
bkDate_input.click()

submit_btn = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[10]/div[2]/div/i/input")
submit_btn.click()

toaster = win10toast.ToastNotifier()
f = open("C:/Users/abhin/Documents/autoGymLog.txt", 'a')

try:
    # Alert exists
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    f.write("Slot 1 booking successful\n")
    toaster.show_toast("autoGym", "Slot 1 booking successful")
    message_1 = "Greetings Mr. Abhinav,\n\nPython autoGym script completed.\nGym slot 1 booking successful "

except TimeoutException:
    # alert doesn't exist
    f.write("Error while booking slot 1\n")
    toaster.show_toast("autoGym", "Error while booking slot 1")
    message_1 = "Greetings Mr. Abhinav,\n\nPython autoGym script completed.\nGym slot 1 booking failed. "

driver.get("https://apps.nottingham.edu.my/jw/web/userview/booking/v/_/request")

number_textbox = driver.find_element_by_id("contact_no")
number_textbox.send_keys(number)

purpose_textbox = driver.find_element_by_id("purpose")
purpose_textbox.send_keys(purpose)

slot2 = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[8]/div[2]/div[2]/div[1]/label[8]/i")
slot2.click()

bkDate_textBox = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[6]/div[2]/div/input")
bkDate_textBox.click()

bkDate_input = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/a[text()=%s]" % bkDateNum)
bkDate_input.click()

submit_btn = driver.find_element_by_xpath(
    "/html/body/div[2]/div[1]/div/div[2]/main/div[1]/fieldset/form/div[10]/div[2]/div/i/input")
submit_btn.click()

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    f.write("Slot 2 Booking Successful\n")
    toaster.show_toast("autoGym", "Slot 2 Booking Successful")
    message = "".join(
        [message_1, "\nGym Slot 2 Booking Successful.\nPlease Proceed Accordingly \n\nWarm Regards, Python"])

except TimeoutException:
    f.write("Error while booking slot 2\n")
    toaster.show_toast("autoGym", "Error while booking slot 2")
    message = "".join([message_1, "\nGym Slot 2 Booking Failed.\nPlease Proceed Accordingly \n\nWarm Regards, Python"])

driver.get("https://apps.nottingham.edu.my/jw/web/userview/booking/v/_/mybooking")

grid = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/main/div/div[2]/form[2]/table/tbody")
total_height = grid.size["height"] + 300

driver.set_window_size("1920", total_height)
driver.save_screenshot("C:/Users/abhin/Pictures/autoGym/Booking.png")

driver.quit()

img_data = open("C:/Users/abhin/Pictures/autoGym/Booking.png", 'rb').read()

msg.attach(MIMEText(message))

image = MIMEImage(img_data, name=os.path.basename("Booking.png"))
msg.attach(image)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, password_email)
server.sendmail(sender_email, rec_email, msg.as_string())
server.quit()

runTime = datetime.datetime.now() - time
runTime_str = str(runTime)

f.write("Script ran at %s. \nRuntime is %s\n" % (time_str, runTime_str))
f.write("--------------------------------------\n")
f.close()
