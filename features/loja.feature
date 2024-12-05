Feature: Login do usuário
  Para que eu possa navegar pelo site de compras
  Preciso realizar o login

  Scenario: Realizar login
    Given entro na página de login da loja Joga Junto
    When insiro minhas credenciais
    And clico no botão de Iniciar Sessão
    Then entro na pagina inicial da loja