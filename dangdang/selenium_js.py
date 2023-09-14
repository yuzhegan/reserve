# encoding='utf-8

# @Time: 2023-09-14
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get("https://login.dangdang.com/")
# read c.js 
with open(os.path.join(os.path.dirname(__file__), 'dd.js'), 'r', encoding='utf-8') as f:
    js = f.read()
    # ic(js)
    # ruan c.js the function test and ouptut test value
    output = driver.execute_script(js)
    ic(output)
    ic(output['permanent_id'])
    ic(output['sign'])

