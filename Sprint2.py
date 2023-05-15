import random
import re
erro = ""

try:
    print("Seja bem vindo à plataforma de descarte da Urbitável. Deseja fazer o seu cadastro? (Sim ou Não)")
    resposta = input()

    if resposta.lower() == "não":
        print("Ok! Programa encerrado. ")
    else:
        print("Digite seu novo usuário.")
        usuario = input()
        if re.search("\d", usuario):
            erro = "Nomes não podem conter números"
            raise ValueError
        print(f"Ok! Agora digite sua nova senha, {usuario}.")
    
        senha = input()
        if not re.search("\d{8}", senha):
            erro = "A senha deve conter no mínimo 8 dígitos, sendo estes apenas números!"
            raise ValueError
        
        print("Cadastro feito. Deseja fazer o login? (Sim ou Não)")
        respostaLogin = input()
        if respostaLogin.lower() == "não":
            print(f"Ok! Programa encerrado. Até mais, {usuario}. ")
        elif respostaLogin.lower() == "sim":
            print("Insira o seu usuário anteriormente cadastrado.")
            login = input()
            while login != usuario:
                print("Usuário incorreto. Tente novamente.")
                login = input()
            else:
                print("Ok! Agora digite sua senha anteriormente cadastrada.")
                senhaLogin = input()
                while senhaLogin != senha:
                    print("Senha incorreta, digite novamente.")
                    senhaLogin = input()

                print("Login feito. Seja bem vindo(a) a sua conta,", usuario,"!")
                
                #estrutura menu programa
                pontosAcumulados = random.randint(10,200)
                dinheiro = pontosAcumulados * 1.5
                            
                print("Qual ação desejar realizar?\nVERIFICAR PONTOS | FALE CONOSCO | SOBRE NÓS | SAIR\n") 
                acao = input()
                while acao.lower() != "sair":
                    #Vendo os pontos e fazendo ou não o saque
                    if acao.lower() == "verificar pontos":
                        print(f"{usuario}, você tem o total de {pontosAcumulados} pontos, equivalentes a R${dinheiro:.2f}. Deseja prosseguir com a retirada?\n")
                        respostaRetirada = input()
                        if respostaRetirada.lower() != "sim":
                            pontosAcumulados = pontosAcumulados
                        elif respostaRetirada.lower() == "sim":
                            print("Ok! Qual seria a sua forma de realizar o saque || OPÇÕES: PIX/TRANSAÇÃO BANCÁRIA ||\n")
                            pontosAcumulados = 0
                            dinheiro = 0
                            formadepag = input()
                            if formadepag.lower() == "pix":
                                print("Certo! Registre sua chave PIX e faremos o depósito em até 24h após a solicitação.\n")
                                pix = input()
                            
                            elif formadepag.lower() == "transação bancária":
                                print("Certo! Registre suas credenciais bancárias e faremos o depósito em até 24h após a solicitação.\n")
                                credBan = input()
                    #Seção Fale Conosco
                    elif acao.lower() == "fale conosco":
                        print(f"\nMande um email para o nosso suporte para que possamos ajudá-lo(a), {usuario}. O nosso email é urbitável@atendimento.com.br.\n")
                    #Seção Sobre nós
                    elif acao.lower() == "sobre nós":
                        print("\nO projeto Urbitável é uma iniciativa coletiva de estudantes da FIAP, que busca apresentar uma solução sustentável, relativa a um dos problemas ambientais mais ocorridos pelo mundo todo: O inadequado descarte dos lixos e substratos prejudiciais ao ambiente em meiosurbanos. Se trata, portanto,de uma ideia interventiva que tem como objetivo recompensar a população urbana por descartar corretamente os seus lixos,através do programa consciente de descarte.\n")
                    
                    print("Qual outra ação deseja realizar?\nVERIFICAR PONTOS | FALE CONOSCO | SOBRE NÓS | SAIR\n") 
                    acao = input()
                #Mensagem de resumo e Despedida do usuário
                print(f"\nObrigado por visitar nosso programa {usuario}!\tVocê possui {pontosAcumulados} pontos, equivalentes a R${dinheiro:.2f}.\nVolte Sempre!\n\nSOBRE A SUA CONTA:\n\nUSUÁRIO: {usuario}\tSENHA: {senha}")
except ValueError:
    print(erro)