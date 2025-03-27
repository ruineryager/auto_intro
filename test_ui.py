from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def test_sale():
    options=Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.get('https://magento.softwaretestingboard.com/')
    sleep(1)
    sale_link = browser.find_element(By.ID, 'ui-id-8')
    sale_link.click()
    sleep(1)
    title = browser.find_element(By.CLASS_NAME, 'base')
    assert title.text == 'Sale'
    browser.close()

test_sale()