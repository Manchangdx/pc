import json
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver import ActionChains

def spider():
    driver = webdriver.Chrome()    # 启动谷歌驱动，打开浏览器
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)                # 打开待爬取页面
    result = []
    while True:
        driver.implicitly_wait(3)  # 隐式等待 3 秒
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf-8'))
        for comment in response.css('div.col-11'):
            d = {
                'username': comment.css('a::text').extract_first().strip(),
                'content': ' '.join([i.strip() for i in list(comment.css(
                    'div.content::text').extract())])
            }
            result.append(d)
        # 如果第二个 li 标签 class 属性值包含 disalbed 字段，表示没有下一页了
        if 'disabled' in response.xpath('(//li[contains'
            '(@class, "page-item")])[2]/@class').extract_first():
            break
        # chromedirver 无法自动定位到当前页面未显示区域，下面三行代码起到定位作用
        # 定位到第二个 li 标签，也就是“下一页”那个按钮
        ac = driver.find_element_by_xpath(
            '(//li[contains(@class, "page-item")])[2]')
        ActionChains(driver).move_to_element(ac).perform()
        time.sleep(1)  # 等待按钮加载
        ac.click()     # 点击下一页按钮
    driver.quit()
    with open('comments.json', 'w') as f:
        json.dump(result, f)

if __name__ == '__main__':
    spider()
