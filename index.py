print("Seja bem vindo à plataforma de descarte da Urbitável. Deseja fazer o seu cadastro?")
resposta = input()

if resposta.lower() == "não":
    print("Ok! Programa encerrado.")
else:
    print("Digite seu novo usuário:")
    usuario = input()
    print("Agora digite sua nova senha:")
    senha = int(input())
    print("Cadastro feito. Deseja fazer o login?")
    respostaLogin = input()
    
    if respostaLogin.lower() == "não":
        print(f"Ok! Programa encerrado. Até mais {usuario}!")
    else:
        print("Insira seu usuário:")
        login = input()

        if login.lower() != usuario:
            print("Usuário incorreto, tente novamente.")
        else:
            print("Ok! Agora digite sua senh:")
            senhaLogin = int(input())

            if senhaLogin != senha:
                print("Senha incorreta, tente novamente.")
            else:
                print("Login feito. Seja bem-vindo, {usuario}!")
                
print("o que deseja fazer em nossa plataforma? REALIZAR SAQUE | FALE CONOSCO | SOBRE NÓS")
decisãoUsuario = input()

if decisãoUsuario == "realizar saque":
    print("saque realizado.")
elif decisãoUsuario == "fale conosco":
    print("mande um email para o nosso suporte. O nosso email é urbitável@atendimento.com.br")
elif decisãoUsuario == "sobre nós":
    print("Somos um grupo de estudantes de Engenharia de Software.")