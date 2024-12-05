from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time 

@given(u'entro na página de login da loja Joga Junto')
def step_impl(context):
    context.browser.get("https://projetofinal.jogajuntoinstituto.org/")
    time.sleep(5)  # Aguarda o carregamento da página

@when(u'insiro minhas credenciais')
def step_impl(context):
    # Preenche os campos do formulário
    context.browser.find_element(By.NAME, "email").send_keys("testejogajunto1945@gmail.com")
    context.browser.find_element(By.NAME, "password").send_keys("teste123123123teste")
    time.sleep(5)  # Aguarda para simular o preenchimento

@when(u'clico no botão de Iniciar Sessão')
def step_impl(context):
    # Envia o formulário
    context.browser.find_element("xpath", '//*[@id="root"]/main/form/button').click()
  

@then(u'entro na pagina inicial da loja')
def step_impl(context):
    time.sleep(10)
    context.browser.quit()
    
