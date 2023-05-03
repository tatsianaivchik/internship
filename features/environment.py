from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from app.application import Application

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    service = Service('/Users/TANYA/QA_Automation/internship/chromedriver')
    # service = Service('/Users/TANYA/QA_Automation/internship/geckodriver')
    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)

     ## HEADLESS MODE CHROME####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(chrome_options=options, service=Service('/Users/TANYA/QA_Automation/internship/chromedriver'))

     ## HEADLESS MODE FIREFOX####
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Firefox(options=options, service=Service('/Users/TANYA/QA_Automation/internship/geckodriver'))

    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'tanyai_bTmr7F'
    # bs_key = 'pXqnZeDdae6Zu87rfJee'
    #
    # desired_cap = {
    #     'browserName': 'Chrome',  # Safari or FireFox
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '11',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # browser_init(context)
    #for browerstack
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
