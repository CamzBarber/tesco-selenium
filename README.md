# Tesco Selenium - Add to Basket
Adds a list of items to your Tesco shopping basket in Python. This is whilst we wait for Tesco to produce an API capable of this. 

1. Install the 'Selenium' library in Python.
2. Install the Selenium Driver [here.](http://selenium-python.readthedocs.io/installation.html#drivers)
3. Download or clone the [tescoAddBasket.py](tescoAddBasket.py) file and open it in your Python editor.
4. Input your Tesco Username, Password and location of the Selenium driver in to the following locations:
```python
chrome_driver = 'venv/selenium/chromedriver'
tesco_log_in('email-address-here', 'password-here')
```
5. Change the 'products' list to your product ID's of your Tesco products. These are in the Tesco URL or is also called the TPNC in the Tesco API.
