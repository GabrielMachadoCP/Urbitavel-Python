print("Seja bem vindo à plataforma de descarte da Urbitável. Deseja fazer o seu cadastro?")
resposta = input()

if resposta == "não":
    print("programa encerrado")
else:
    print("digite seu novo usuario")
    usuario = input()
    print("ok! agora digite sua nova senha.")
    senha = int(input())
    print("cadastro feito. Deseja fazer o login?")
    respostaLogin = input()
    if respostaLogin == "não":
        print("programa encerrado")
    else:
        print("insira seu usuario")
        login = input()
        if login != usuario:
            print("Usuário incorreto. Tente novamente.")
        else:
            print("ok! agora digite sua senha.")
            senhaLogin = int(input())
            if senhaLogin != senha:
                print("senha incorreta, digite novamente")
            else:
                print("Login feito. Seja bem vindo,", usuario, "!")









