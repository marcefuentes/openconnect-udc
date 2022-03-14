#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import os

os.system("sudo ifconfig tun0 down")
host = "vpn.udc.es"
driver = webdriver.Chrome("/usr/bin/chromedriver")
#driver = webdriver.gecko.driver("/usr/bin/geckodriver")
print('Ok')
wait = WebDriverWait(driver, 60)
driver.get("https://"+host)
dsid = wait.until(lambda driver: driver.get_cookie("DSID"))
driver.quit()
subprocess.run(["sudo", "/usr/sbin/openconnect", "-b", "-C", dsid["value"], "--protocol=pulse", host])
