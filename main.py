#Author Thalrod

import codecs
import random
from time import sleep

from selenium import webdriver

from installation import InstallPackage

types_of_encoding = ["cp1252"]


class Start():
    # Using @property decorator
    def __init__(self):
        def loadResearch(self):
            self.research = []
            self.linenumber = []
            for encoding_type in types_of_encoding:
                with codecs.open("res/research.txt", encoding=encoding_type, errors='replace') as f:
                    for line in f:
                        line = line.replace("\n", "")
                        s = line.split(": ")
                        self.linenumber.append(s[0])
                        self.research.append(s[1])

        loadResearch(self)
        browser = webdriver.Chrome(executable_path=r'res/chromedriver.exe')
        browser.get("https://www.ecosia.org/")
        sleep(2)
        while True:
            choice = random.choice(self.research)
            browser.find_element_by_css_selector(
                "#__layout > div > section.search-section.section.hero > div.content > form > div.input-wrapper > input").send_keys(
                choice)
            sleep(1)
            browser.find_element_by_css_selector(
                "#__layout > div > section.search-section.section.hero > div.content > form > div.buttons-wrapper > "
                "button.button.button-submit.icon-button.icon-button--elevation-0.icon-button--size-m.icon-button"
                "--variant-bare > svg").click()
            sleep(20)
            browser.get("https://www.ecosia.org/")
            sleep(2)


InstallPackage()
Start()
