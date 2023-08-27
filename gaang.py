#@title ***SELENIUM SOCKS5***
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = {
        'proxy': {
            #'http': 'socks5://gtuyuckd-rotate:rf9rgi07oj74@p.webshare.io:80',
            #'https': 'socks5://gtuyuckd-rotate:rf9rgi07oj74@p.webshare.io:80',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options,seleniumwire_options=options)
#driver.get("http://httpbin.org/ip")
#print(driver.find_element(By.TAG_NAME, "body").text)
driver.get("https://gmail.com")
print(driver.title)
sleep(99999)
