# Aula de Programação Aplicada ao Direito - Nível Iniciante
# Projeto Final - Iniciação à Automação de Peças Jurídicas (Código Simplificado)


def imprimir_separador1():
    print("\n\n--------------\n")


def imprimir_separador2():
    print("\n\n")

def imprimir_apresentacao():
    # Tarefa
    #Escreva aqui a tela inicial com a apresentação de seu programa.
    input("Bem vindo ao automatizador de documentos jurídicos! ")
    input("Hoje iremos emitir uma autorização ")
    input("Tecle enter para começar ")


def empresa_cadastrar_razao_social():
    razao_social = input("Digite a razão social da empresa: ")
    # Prato Bom Alimentos ltda
    while not razao_social.replace(" ", "").isalpha():
        print("Entrada inválida. A razão social só deve conter letras e espaços")
        razao_social = input("Digite a razão social da empresa: ")
    return razao_social


def empresa_cadastrar_cnpj():
    cnpj = input("Digite o CNPJ da empresa: ")
    checks = 0
    while checks < 2:
        while not cnpj.replace("/","").replace(".", "").replace("-", "").isnumeric() or "/" not in cnpj or "." not in cnpj or "-" not in cnpj:
            checks = 0
            print("Entrada inválida. O CNPJ deverá conter apenas números, pontos ou traços.")
            cnpj = input("Digite o CNPJ da empresa: ")
        checks += 1
        while len(cnpj.replace("/","").replace(".", "").replace("-", "")) != 14:
            checks = 0
            print("Entrada inválida. O CNPJ deverá conter 14 números.")
            cnpj = input("Digite o CNPJ da empresa: ")
        checks += 1
    return cnpj



def funcionarios_definir_numero_funcionarios():
    numero_funcionarios = input("Digite o número de funcionários: ")
    while not numero_funcionarios.isnumeric():
        print("Entrada inválida.")
        numero_funcionarios = input("Digite o número de funcionários: ")
    return numero_funcionarios


def funcionarios_cadastrar_nome_funcionario():
    nome_funcionario = input("Digite o nome do funcionário da empresa: ")
    # Prato Bom Alimentos ltda
    while not nome_funcionario.replace(" ", "").isalpha():
        print("Entrada inválida. O nome do funcionário só deve conter letras e espaços")
        nome_funcionario = input("Digite o nome do funcionário da empresa: ")
    return nome_funcionario



def funcionarios_cadastrar_cpf_funcionario():
    cpf = input("Digite o CPF do funcionário: ")
    checks = 0
    while checks < 2:
        while not cpf.replace(".", "").replace("-", "").isnumeric() or "." not in cpf or "-" not in cpf:
            checks = 0
            print("Entrada inválida. O CPF deverá conter apenas números, pontos ou traços.")
            cpf = input("Digite o CPF do funcionário: ")
        checks += 1
        while len(cpf.replace(".", "").replace("-", "")) != 11:
            checks = 0
            print("Entrada inválida. O CPF deverá conter 11 números.")
            cpf = input("Digite o CPF do funcionário: ")
        checks += 1
    return cpf

def cadastrar_funcionarios(funcionarios_numero):
    # Tarefa (Difícil) 
    # Escreva uma função que retornará uma lista de funcionários contendo outras listas.
    # Cada uma destas últimas listas, por sua vez, deverão conter o nome e cpf de um funcionário.
    # Dicas: 
    # O número de funcionários já é dado como o parâmetro 'funcionários_numero'
    # Então, crie listas vazias e utilize o método .append para adicionar dados a elas.
    # O uso de for-loop é muito bem vindo.
    funcionarios_lista_nomes_e_cpfs = []
    for funcionario_atual in range(funcionarios_numero):
        print(f"Funcionario {funcionario_atual + 1}: ")
        nome_e_cpf = []
        nome_e_cpf.append(funcionarios_cadastrar_nome_funcionario())
        nome_e_cpf.append(funcionarios_cadastrar_cpf_funcionario())
        funcionarios_lista_nomes_e_cpfs.append(nome_e_cpf)
        imprimir_separador1()
    return funcionarios_lista_nomes_e_cpfs

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
# Chama a função adqurirDadosUsuario e 'desempacota' as variáveis retornadas. Após, imprime a autorização.
empresa_razao_social, empresa_cnpj, funcionarios_lista_nomes_e_cpfs = adquirir_dados_usuario()
print(montar_autorizacao(empresa_razao_social, empresa_cnpj,
                     funcionarios_lista_nomes_e_cpfs))
