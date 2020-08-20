# solution 1
# Login with requests
from selenium import webdriver
import requests
payload = {
    'log': 'admin',
    'pwd': '123456aA'
}
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
with requests.Session() as s:
    response = s.post(url, data=payload)
    cookie = s.cookies.get_dict()
    username = cookie.get(
        'wordpress_logged_in_9b3f1ac684a4401c524e27c6c40e95d5').split('%')[0]
    print(username)


# Login with selenium
# requirement
# sudo apt-get install chromium-chromedriver
# sudo pip3 install selenium
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
driver.get(url)
username = driver.find_element_by_id('user_login')
password = driver.find_element_by_id('user_pass')

username.send_keys('admin')
password.send_keys('123456aA')

driver.find_element_by_name('wp-submit').click()
username = driver.get_cookies()[2].get('value').split('%')[0]
print(username)
