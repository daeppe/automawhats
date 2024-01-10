# Automação de encaminhamento de mensagens no whatsapp.
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem.
# Encaminhar de 5 em 5 mensagens.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get('https://web.whatsapp.com')

mensagem = """Fala galera!
Olha que maneiro esse bot para whatsapp
"""

list_contact = ["Lembretes"]

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Você')
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Você')