import json
from functools import reduce
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def spider():
    driver = webdriver.Chrome()                 # 启动谷歌驱动，打开浏览器
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)                             # 打开待爬取页面
    page = 1 
    result = []
    while True:
        WebDriverWait(driver, 10).until(        # 显式等待 10 秒，默认轮询 0.5 秒
            EC.text_to_be_present_in_element(   # 设置条件
                (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
                str(page)                       # 上一行代码块里是否有这一行的字段
            )
        )
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf-8'))
        for i in response.css('div.comment-item-wrapper'):
            d = {
                'username': i.css('a.username::text').extract_first().strip(),
                'content': reduce(lambda a, b: a+b, (i.css('p::text').extract()))
            }
            result.append(d)
        if response.css('div.comment-box li.disabled.next-page'):
            break   # 如果有 class 属性值为 disalbed 的 li 标签，表示没有下一页了
        page += 1
        # chromedirver 无法自动定位到当前页面未显示区域，下面两行代码起到定位作用
        ac = driver.find_element_by_css_selector('div.comment-box li.next-page a')
        ActionChains(driver).move_to_element(ac).perform()
        driver.find_element_by_css_selector('div.comment-box li.next-page').click()
    driver.quit()
    with open('comments.json', 'w') as f:
        json.dump(result, f)

if __name__ == '__main__':
    spider()
