# Aula de Programação Aplicada ao Direito - Nível Iniciante
# Projeto Final - Iniciação à Automação de Peças Jurídicas (Código Simplificado)


def imprimir_separador1():
    print("\n\n--------------\n")


def imprimir_separador2():
    print("\n\n")

def imprimir_apresentacao():
    # Tarefa
    #Escreva aqui a tela inicial com a apresentação de seu programa.
    pass


def empresa_cadastrar_razao_social():
    # Tarefas:
    # Utilize a função input para receber a razão social da empresa.
    # Escreva um validador
    # Garanta que o input dado é composto apenas por letras ou espaços.
    # Caso contrário:
    # 1) imprima na tela uma mensagem de erro;
    # 2) peça para que os dados sejam novamente inseridos.
    # Depois da verificação, retorne o campo razão social devidamente preenchido.
    pass


def empresa_cadastrar_cnpj():
    # Tarefas:
    # Utilize a função input para receber o cnpj da empresa.
    # Escreva um validador
    # Garanta que o input dado é composto apenas por 14 números, podendo conter pontos, traços e barras.
    # Caso contrário:
    # 1) imprima na tela uma mensagem de erro;
    # 2) peça para que os dados sejam novamente inseridos.
    # Depois da verificação, retorne o campo cnpj devidamente preenchido.
    pass



def funcionarios_definir_numero_funcionarios():
    # Tarefas:
    # Utilize a função input para receber o número de funcionários.
    # Escreva um validador
    # Garanta que o input dado é composto apenas por números.
    # Caso contrário:
    # 1) imprima na tela uma mensagem de erro;
    # 2) peça para que os dados sejam novamente inseridos.
    # Depois da verificação, retorne o campo número de funcionários devidamente preenchido.
    pass


def funcionarios_cadastrar_nome_funcionario():
    # Tarefas:
    # Utilize a função input para receber o nome do funcionário.
    # Escreva um validador
    # Garanta que o input dado é composto apenas por letras ou espaços.
    # Caso contrário:
    # 1) imprima na tela uma mensagem de erro;
    # 2) peça para que os dados sejam novamente inseridos.
    # Depois da verificação, retorne o campo nome do funcionário devidamente preenchido.
    pass


def funcionarios_cadastrar_cpf_funcionario():
    # Tarefas:
    # Utilize a função input para receber o cpf do funcionário.
    # Escreva um validador
    # Garanta que o input dado é composto apenas por 11 números, podendo conter pontos e traços.
    # Caso contrário:
    # 1) imprima na tela uma mensagem de erro;
    # 2) peça para que os dados sejam novamente inseridos.
    # Depois da verificação, retorne o campo cpf devidamente preenchido.
    pass

def cadastrar_funcionarios(funcionarios_numero):
    # Tarefa (Difícil) 
    # Escreva uma função que retornará uma lista de funcionários contendo outras listas.
    # Cada uma destas últimas listas, por sua vez, deverão conter o nome e cpf de um funcionário.
    # Dicas: 
    # O número de funcionários já é dado como o parâmetro 'funcionários_numero'
    # Então, crie listas vazias e utilize o método .append para adicionar dados a elas.
    # O uso de for-loop é muito bem vindo.
    pass

def adquirir_dados_usuario():
    # Essa é a nossa função principal e já está completa.
    # Ela retorna as variáveis contendo dados que serão utilizados para imprimir a nossa autorização.
    # Para isso, ela chama as funções de input e validação, implementadas a seguir.
    imprimir_apresentacao()
    empresa_razao_social = empresa_cadastrar_razao_social()
    imprimir_separador1()
    empresa_cnpj = empresa_cadastrar_cnpj()
    imprimir_separador1()
    funcionarios_lista_nomes_e_cpfs = cadastrar_funcionarios(int(funcionarios_definir_numero_funcionarios()))
    return empresa_razao_social, empresa_cnpj, funcionarios_lista_nomes_e_cpfs

def montar_autorizacao(empresa_razao_social, empresa_cnpj, funcionarios_lista_nomes_e_cpfs):
    # Função já está completa
    # Monta autorização utilizando os dados recebidos como argumentos
    texto = "\n\nAutorização\n"
    texto += f"\nA empresa {empresa_razao_social}, CNPJ {empresa_cnpj}, autoriza\n"
    for index, nome_e_cpf in enumerate(funcionarios_lista_nomes_e_cpfs): #adiciona inf. funcionarios
        texto += f"{str(index+1)} - {nome_e_cpf[0]}, CPF {nome_e_cpf[1]}\n"
    texto += "a retirar talões de cheque que forem a esta endereçados.\n"
    texto += "\nCidade da Justiça, 04 de Maio de 1984.\n\n"
    texto += "------------------------\n"
    texto += f"{empresa_razao_social}"
    return texto


##############


# Descrição:
# Chama a função adquirir_dados_usuario e 'extrai' as variáveis retornadas.
# Após, monta e imprime a autorização.
empresa_razao_social, empresa_cnpj, funcionarios_lista_nomes_e_cpfs = adquirir_dados_usuario()
print(montar_autorizacao(empresa_razao_social, empresa_cnpj,
                     funcionarios_lista_nomes_e_cpfs))
