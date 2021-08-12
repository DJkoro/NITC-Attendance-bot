from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule 
import time




def attendance():
    
    browser = webdriver.Chrome('Enter path to Chrome driver')#Enter the path to location of Chromedriver (eg. /User/username/desktop/chromedriver)
    browser.get("https://eduserver.nitc.ac.in/login/index.php")
    search = browser.find_element_by_name("username")
    search.send_keys("Enter your username")   #Enter your username
    search.send_keys(Keys.RETURN)
    search1 = browser.find_element_by_name("password")
    search1.send_keys("Enter your password")  #Enter your pasword
    login = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/section/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button")
    login.click()
    
    
    try:

        time.sleep(2)
        elePresent = browser.find_element_by_link_text("Attendance").is_displayed()
        if elePresent==True:
            element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Attendance"))
            )
            
            browser.execute_script("arguments[0].click();", element)
            element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Go to activity"))
            )
            element.click()
            element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Submit attendance"))
            )
            element.click()
            element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "status"))
            )
            element.click()
            element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "submitbutton"))
            )
            element.click()
            print("Attendance Marked")
    
    except :
        print("Attendance Was not Marked")
        browser.quit()

# schedule the code according to your time table! :)
   
if __name__ == "__main__":

    # schedule.every().wednesday.at("13:15").do(attendance)
    # schedule.every().minute.at(":17").do(attendance)
    while True:
       schedule.run_pending()
       time.sleep(1) # wait one minute
    attendance()
