#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import subprocess

host = vpn.udc.es
driver = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(driver, 60)
driver.get("https://"+host)
dsid = wait.until(lambda driver: driver.get_cookie("DSID"))
driver.quit()
subprocess.run(["openconnect", "-b", "-C", dsid["value"], "--protocol=pulse", host])
