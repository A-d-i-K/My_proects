import datetime       # Smoke testing всего бизнес пути
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Adik\\PycharmProjects\\python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver_g.find_element(By.XPATH, "//input[@id='user-name']")   #data-test XPATH
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver_g.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver_g.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Product #1"""
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

"""INFO Product 2"""
product_2 = driver_g.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Select Product 2")

cart = driver_g.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter cart")

"""INFO Cart Product 1"""
cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Price Product 1 GOOD')

"""INFO Cart Product 2"""
cart_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print('INFO Cart Product 2 GOOD')

price_cart_product_2 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print('INFO Cart Price Product 2 GOOD')

button_checkout = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
button_checkout.click()
print("Click Checkout")

"""Select User INFO"""
first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Alex")
print("Input First-Name")

last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("Input Last-Name")

zip = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys(1234)
print("Click Zip")

button_continue = driver_g.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish Product 1"""
finish_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_cart_product_1
print('INFO finish Product 1 GOOD')

price_finish_product_1 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('INFO finish Price Product 1 GOOD')

"""INFO Finish Product 2"""
finish_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_cart_product_2
print('INFO finish Product 2 GOOD')

price_finish_product_2 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print('INFO finish Price Product 2 GOOD')

summery_price = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summery_price = summery_price.text
print(value_summery_price)
num_1 = float(value_finish_price_product_1[1:])
num_2 = float(value_finish_price_product_2[1:])
sum_num = float(num_1 + num_2)
item_total = "Item total: " + ("$" + str(sum_num))
print(item_total)
assert value_summery_price == item_total
print("Total summary price Good")
