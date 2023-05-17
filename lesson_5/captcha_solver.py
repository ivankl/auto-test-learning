import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def solver(browser):
    value = browser.find_element(By.ID, 'input_value').text
    calculated_value = calc(value)
    print(calculated_value, value)
    input_field = browser.find_element(By.NAME, 'text')
    input_field.send_keys(calculated_value)

    button = browser.find_element(By.ID, 'solve')
    button.click()
