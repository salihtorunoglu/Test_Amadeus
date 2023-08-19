import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search():
    driver = webdriver.Chrome()
    driver.get("https://flights-app.pages.dev/")

    from_Input =driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    to_Input=driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)")
    driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Istanbul")
    driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("Istanbul")
    driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(1)

    from_value = from_Input.get_attribute("value")
    to_value = to_Input.get_attribute("value")
    assert from_value != to_value


def listing():
    driver = webdriver.Chrome()
    driver.get("https://flights-app.pages.dev/")

    driver.find_element(By.CSS_SELECTOR,"body > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("New York")
    driver.find_element(By.CSS_SELECTOR,"body > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR,"body > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("London")
    driver.find_element(By.CSS_SELECTOR,"body > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)

    flights = driver.find_elements(By.XPATH, "(//li[@class='overflow-hidden rounded-xl border border-gray-200'])")
    flights_count = len(flights)

    sentence_element = driver.find_element(By.CLASS_NAME, "mb-10")
    sentence = sentence_element.text
 # Split the text into a list of words.
    words = sentence.split(" ")
    listed_flights = words[1]

    assert listed_flights != flights_count
    print("Test is successful ")
    time.sleep(2)
    exit()
#search()
#listing()
