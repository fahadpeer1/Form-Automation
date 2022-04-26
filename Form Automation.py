from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Selenium browser\chromedriver.exe")

time.sleep(0)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdmZOI1FwGfiQjyV1GvpQ-_OmEFkZ6HwQzkEX6OpWhaSDGlQw/viewform")

LastName = "IT"
last = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName= "Lahore"
first = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="i22"]/div[3]/div')
RadioButtonPeriod.click()

submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()


get_confirmation_div_text = driver.find_element_by_css_selector('vHW8K')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text)== "Your response has been recorded."):
  print ("Test was successful")
else:
    print ("Test was not successful")