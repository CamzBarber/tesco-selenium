"""
Tesco Add to Basket

Cameron Barber - Feb 2018
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = 'venv/selenium/chromedriver'  # Change this to the location of your Chrome Driver
browser = webdriver.Chrome(chrome_driver)


def tesco_log_in(mail, p):
    browser.get('https://secure.tesco.com/account/en-GB/login?from=/')
    elem = browser.find_element_by_name('username')
    elem.clear()
    elem.send_keys(mail)
    elem = browser.find_element_by_name('password')
    elem.clear()
    elem.send_keys(p)
    elem.send_keys(Keys.RETURN)


def tesco_quantity_get(prod):
    quantity_loc = browser.find_elements_by_xpath("//li[@data-productid='" + prod + "']")
    if quantity_loc and quantity_loc[0].find_elements_by_class_name('trolley-counter--quantity-value'):
        return int(quantity_loc[0].find_element_by_class_name('trolley-counter--quantity-value').text)
    else:
        return 0


def tesco_backend_add():
    product_div = browser.find_element_by_class_name('product-details-page')
    add_control = product_div.find_elements_by_class_name('add-control')
    icon_plus = product_div.find_elements_by_class_name('icon-plus')
    prod_name = product_div.find_element_by_class_name('product-title__h1').text
    if add_control and add_control[0].is_displayed():
        browser.find_element_by_class_name('add-control').click()
        return 'Good', prod_name
    elif icon_plus and icon_plus[0].is_displayed():
        browser.find_element_by_class_name('icon-plus').click()
        return 'Good', prod_name
    else:
        # Could click the 'Rest of the Shelf' button here to return the first few IDs for alternative products
        return 'Product Unavailable', prod_name


def tesco_increased_quant(prod_id, quan):
    if tesco_quantity_get(prod_id) <= quan:
        tesco_increased_quant()
    else:
        return tesco_quantity_get(prod_id)


def tesco_add(prod_id):
    browser.get('https://www.tesco.com/groceries/en-GB/products/' + prod_id)
    quan = tesco_quantity_get(prod_id)
    success, prod_name = tesco_backend_add()
    if success == 'Product Unavailable':
        print(success, "-", prod_name)
    else:
        finalq = tesco_increased_quant(prod_id, quan)
        print('Product Added:', prod_id, 'Total Quantity:', finalq, 'Name:', prod_name)


def tesco_list_add(prod):
    start = time.time()
    for i in prod:
        tesco_add(i)
    finish = time.time() - start
    print("Tesco List Add, time elapsed:", finish, "seconds. Avg. per item:", finish/len(prod), "seconds")


"""
------------
EXAMPLE USE:
------------
"""

tesco_log_in('email-address-here', 'password-here')  # enter your username and password here for Tesco

products = ['252261477', '299160997', '256174499', '253557034']
tesco_list_add(products)  # Adds list of products to your basket

browser.close()
