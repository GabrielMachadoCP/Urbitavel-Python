import random

print("Seja bem vindo à plataforma de descarte da Urbitável. Deseja fazer o seu cadastro?")
resposta = input()

if resposta == "não":
    print("Ok! Programa encerrado. ")
else:
    print("Digite seu novo usuario.")
    usuario = input()
    print(f"Ok! Agora digite sua nova senha, {usuario}.")
    senha = int(input())
    print("Cadastro feito. Deseja fazer o login?")
    respostaLogin = input()
    if respostaLogin == "não":
        print(f"Ok! Programa encerrado. Até mais, {usuario}. ")
    else:
        print("Insira o seu usuário anteriormente cadastrado.")
        login = input()
        if login != usuario:
            print("Usuário incorreto. Tente novamente.")
        else:
            print("Ok! Agora digite sua senha anteriormente cadastrada.")
            senhaLogin = int(input())
            if senhaLogin != senha:
                print("Senha incorreta, digite novamente.")
            else:
                print("Login feito. Seja bem vindo(a) a sua conta,", usuario,"!")
                print("O que deseja fazer em nossa plataforma?  REALIZAR SAQUE | FALE CONOSCO | SOBRE NÓS | SAIR DA MINHA CONTA")
                decisãoUsuario = input()

                #estrutura menu programa
                pontosAcumulados = random.randint(0,5.000)
                comprovanteDeDescarte = ""
                if decisãoUsuario == "realizar saque":
                    print(f"{usuario}, você tem o total de {pontosAcumulados} pontos. Deseja prosseguir a retirada?")
                    respostaRetirada = input()
                    if respostaRetirada == "sim":
                        print("Ok! Qual seria a sua forma de realizar o saque,>>> OPÇÕES: PIX | TRANSAÇÃO BANCÁRIA <<<")
                    else:
                        print(f"Ok! Programa encerrado. Até mais, {usuario}")
                    formadepag = input()
                    if formadepag == "pix":
                        print("Certo! Registre sua chave PIX e faremos o depósito em até 24h após a solicitação. Ajudo em algo mais?")
                    else:
                        print("Certo! Registre suas credenciais bancárias e faremos o depósito em até 24h após a solicitaçaõ. Ajudo em algo mais?")
                    respostajuda = input()
                    if respostajuda == "sim":
                        print("O que deseja fazer em nossa plataforma?  REALIZAR SAQUE | FALE CONOSCO | SOBRE NÓS | SAIR DA MINHA CONTA")
                    elif decisãoUsuario == "fale conosco":
                        print(f"Mande um email para o nosso suporte para que possamos ajudá-lo(a), {usuario}. O nosso email é urbitável@atendimento.com.br.")
                    elif decisãoUsuario == "sobre nós":
                        print("O projeto Urbitável é uma iniciativa coletiva de estudantes da FIAP, que busca apresentar uma solução sustentável, relativa a um dos problemas ambientais mais ocorridos pelo mundo todo: O inadequado descarte dos lixos e substratos prejudiciais ao ambiente em meiosurbanos. Se trata, portanto,de uma ideia interventiva que tem como objetivo recompensar a população urbana por descartar corretamente os seus lixos,através do programa consciente de descarte.")
                    elif decisãoUsuario == "sair da minha conta":
                        print(f"Você saiu da sua conta. Até mais, {usuario}!")
                    else:
                        print(f"Ok! Programa encerrado. Até mais, {usuario}")

                    
                     








