from bs4 import BeautifulSoup
from selenium import webdriver


def scrape():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("")

