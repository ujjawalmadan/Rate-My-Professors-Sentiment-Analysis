# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
import re
from shutil import which
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'

    def start_requests(self):
        for i in range(0,25000):
            link = 'https://www.ratemyprofessors.com/campusRatings.jsp?sid=' + str(i)
            yield SeleniumRequest(
                url = link,
                wait_time = 1,
                callback = self.parse, 
                meta = {'Code': i}
            )

    def parse(self, response):
        driver = response.meta['driver']
        try:
            cookies_tab = driver.find_element_by_xpath("//button[@class='big-close ccpa-close']")
            cookies_tab.click()
        except:
            pass
        try:
            for i in range(0, 50):
                load = WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//a[@id='loadMore']")))
                load.click()    
        except:
            pass
        html = driver.page_source
        resp = Selector(text = html)
        yield{
            'Code': response.meta['Code'],
            'School Name': resp.xpath("//div[@class='result-text']/span/text()").get()[8:-7],
            'Location': resp.xpath("//div[@class='result-title']//span/text()").get()[8:-7],
            'Overall Quality Rating': resp.xpath("//div[@class='right-breakdown school-averages']//span[@class='score medium' or @class='score fair' or @class='score poor' or @class='score good']/text()").get(),
            'Scores': [score.get() for score in resp.xpath("//div[@class='right-breakdown school-averages']//span[@class='score']/text()")],
            'Comment Scores': [scores.get() for scores in resp.xpath("//div[@class='rating']/div[@class='score fair' or @class='score poor' or @class='score good']/text()")],
            'Comments': [comment.get().replace('\n','').replace('\t','') for comment in resp.xpath("//td[@class='comments']/p/text()")],
        }
