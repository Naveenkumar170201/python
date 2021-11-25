from selenium import webdriver
browser=webdriver.Chrome('chromedriver.exe')
browser.get('http://web.whatsapp.com')
input("Enter any key press after QR scan")
name=input("Enter the name:")
#to find span tag title
user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg='hii...'
count=10
msgbox=browser.find_element_by_class_name('_2vbn4')   #msg area

for i in range(count):
    msgbox.send_key(msg)
    button=browser.find_element_by_class_name('_4sWnG')   #send button

    button.click()
print('complete')




