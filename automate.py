import math
from selenium import webdriver
from tabulate import tabulate
from playsound import playsound
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import pyperclip
c=''
pyperclip.copy(c)
#https://chrome.google.com/webstore/detail/phantom/bfnaelmomeimhlpmgjnjophhpkkoljpa/related
#from os import environ
msg = "Blank"
tel_group_id = "Jixed999_bot"

def SetSlippage(driver):
    try:
     print("Inside Set Slippage function")
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                  "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/button"))).click()
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                "/html/body/div[1]/div[3]/div[1]/div/div/form/div[2]/div[1]/div/button[1]"))).click()
     print("HELLO")
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                "/html/body/div[1]/div[3]/div[1]/div/div/form/div[2]/div[2]/button/div"))).click()
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/button"))).click()
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                "/html/body/div[1]/div[3]/div[1]/div/div/form/div[2]/div[1]/div[2]/button[4]"))).click()
     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                "/html/body/div[1]/div[3]/div[1]/div/div/form/div[2]/div[2]/button/div"))).click()
    except Exception as e:
     print(e)

def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/{api-link}/sendMessage?chat_id=-4073279255&text={msg}"
    el_resp = requests.get(telegram_api_url)
def getvalue(driver):
    print("Getting Value")
    upper=WebDriverWait(driver, 9 ).until(
             EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/div[1]/div[1]/div/div[1]/div[2]/span[1]")))
    lower=WebDriverWait(driver, 9 ).until(
             EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/div[1]/div[4]/div/div/div[2]/span[1]")))
    return [upper.text,lower.text]
def resultt(driver):
    try:
        print("INSIDE RESULT FUNCTION")
        try:
            WebDriverWait(driver, 0.1).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[3]/div[1]/div/div/div[2]/button[1]"))).click()
        except:
            print("No price warning")
        try:
            WebDriverWait(driver, 0.1).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[3]/div[1]/div/div[2]/button[2]"))).click()
        except:
            print("No liq warning")
        while(WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/div"))).text=="Confirming transaction"):
            time.sleep(3)
            continue
        answer='{Name}',WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div"))).text
        print(answer)
        send_msg_on_telegram(answer)
    except Exception as e:
        print(e)
        time.sleep(5)
        print("Result function failed")
def swapp(driver):
    try:
        swap = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/button[2]/div")))
        print("INSIDE SWAP FUNCTION")
        swap.click()
        print("click done")
        resultt(driver)
        print("result done")
        word = "Successfully swapped"
        print(word)
        #send_msg_on_telegram(word)
    except:
        print("Error Swapping")
        send_msg_on_telegram("Swap failed")

def Automate(driver):
 counter=0
 d=[]
 print(tabulate(d, headers=["Marked Price", "Selling price", "Percent","Small Discount","Med Discount","Big Discount"]))
 small=0
 big=0
 mid=0
 i=0
 f=False
 while(True):
  try:
   if(f==True):
     f=False
     time.sleep(3)
   print("Refresh Button")
   Refresh.click()
   get = getvalue(driver)
   b=get[0]
   print("INPUT")
   print(b)
   baseprice =(float(b))
  # print(b)
   #print(baseprice)
   if(baseprice<1):
      print("inside ")
      time.sleep(3)
      WebDriverWait(driver, 100).until(
         EC.presence_of_element_located((By.XPATH,
                                       "//div[2]/div[2]/div/div[3]/form/div[1]/div[3]/div/button"))).click()
      print("Changed Successfully?")
      f=True
      continue
   else:
     f=False
   print("Getting input value")
   inputElement = WebDriverWait(driver, 99999).until(
       EC.element_to_be_clickable((By.XPATH,
                                   "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/div[1]/div[2]/div/span/div/input")))
   print("Getting max button")
   m=WebDriverWait(driver, 5).until(
       EC.element_to_be_clickable((By.XPATH,
                                   "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/div[1]/div[1]/div/div[2]/button[2]")))
   print("doing loop")
   while(True):
    m.click()
    time.sleep(1)
    initialvalue = WebDriverWait(driver, 99999).until(
       EC.element_to_be_clickable((By.XPATH,
                                   "/html/body/div[1]/div[2]/div[2]/div/div[3]/form/div[1]/div[2]/div/sp"
                                   "an/div/input"))).get_attribute("value")
    initial = initialvalue.replace(',', '')
    print(float(str(initial)),4)
    print(round(float(b),4))
    if(round(float(str(initial)),4)==round(float(b),4)):
        break
  except Exception as e:
      print(e)
      time.sleep(5)
      continue
  try:
      result = WebDriverWait(driver, 9).until(
          EC.presence_of_element_located(
              (By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/form/div[1]/div[5]/div/span/div/input"))).get_attribute("value")
      print(result)
      val=result.replace(',', '')
      print("WERF")
     # print("fweefewfwefw")
      print(val)
      val = float(val)
      print(val)
      # print("WWERWR")
      ##      EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div[2]/div[2]/div/div/div[6]/div[1]/span")))
      print("Checking ...")
      flag=True
      difference = ((float(val) - float(baseprice)) * 100) / baseprice
      try:
       t= WebDriverWait(driver, 5).until(
             EC.presence_of_element_located((By.XPATH, "")))
      except:
          print("tryin  som")
      # t=t.text
      # length = len(t)
      # last_chars = t[length - 4 :]
      # print(last_chars)
      if (difference >= 0.1):
       swapp(driver)
      #  flag=False
      # if(last_chars == 'USDC' and difference>0):
      #     swapp(driver)
      # if(flag==True):
      #     time.sleep(3)
      # print(h)
      # msg=tabulate([['TC',baseprice,float(val),difference,small,mid,big,r[0:4],host.text]])
  except Exception as e:
     print(e)
    #print("EXCEPTION")
     #time.sleep(5)
     continue





#driver.minimize_window()
driver.get(url)
driver.set_page_load_timeout(-1)
print("Script started")
driver.refresh()
time.sleep(60)
while(SetSlippage(driver)==False):
    continue
print("Slippage set successfully")
Refresh=WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/button")))
Automate(driver)

