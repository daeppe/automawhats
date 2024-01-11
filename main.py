from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(options=options, service=service)
nav.get('https://web.whatsapp.com')
time.sleep(10)

mensagem = """
Fala galera!
Olha que maneiro esse bot para whatsapp
"""

contact_list = ["Lembretes", "Você"]

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Você')
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

qtde_contacts = len(contact_list)

if qtde_contacts % 5 == 0:
    qtde_blocs = qtde_contacts / 5
else:
    qtde_blocs = int(qtde_contacts / 5) + 1

for index in range(qtde_blocs):
    initial_index = index * 5
    final_index = (index + 1) * 5
    send_list = contact_list[initial_index:final_index]

    elements_list = nav.find_elements('class name', '_1uv-a')
    element = elements_list[-1]

    ActionChains(nav).move_to_element(element).perform()
    element.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()

    for name in send_list:
        time.sleep(1)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(name)
        time.sleep(0.7)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(0.7)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(0.7)
    
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div').click()
    time.sleep(3)