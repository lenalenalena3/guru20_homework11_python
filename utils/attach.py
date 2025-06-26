import allure
from allure_commons.types import AttachmentType

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# логи
def add_logs(browser):
    try:
        logs =browser.execute("getlog",{"type": 'browser'})["value"]
        log_text="\n".join(str(log) for log in logs)
    except Exception as e:
        log_text=f"Логи не доступны: {e}"
    allure.attach(log_text, 'browser_logs', AttachmentType.TEXT)

# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')