# from selenium import webdriver
# import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# service = Service(executable_path=ChromeDriverManager().install())
chrome = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Main Function
if __name__ == '__main__':

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	driver = webdriver.Chrome(executable_path="chromedriver",
							chrome_options=options)
	driver.set_window_size(1024,768)

	# Send a get request to the url
	driver.get('https://www.metric-conversions.org/zh-hans/length/miles-to-kilometers.htm')
	#time.sleep(60)
	element = driver.find_element('xpath','//*[@id="argumentConv1"]')
	element.send_keys("100")
	element2 = driver.find_element('xpath','//*[@id="answer"]')
	print(element2.text)

