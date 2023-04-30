from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # service = Service('/Users/TANYA/QA_Automation/internship/chromedriver')
    service = Service('/Users/TANYA/QA_Automation/internship/geckodriver')
    # context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Firefox(service=service)

     ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(chrome_options=options, service=Service('/Users/TANYA/QA_Automation/internship/chromedriver'))

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
