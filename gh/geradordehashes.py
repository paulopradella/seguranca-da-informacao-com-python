import  hashlib

string = input('Digite o texto a ser gerado a hash.\n')

while True:
    menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                                    1  - MD5
                                    2 - SHA1
                                    3 - SHA256
                                    4 - SHA512
                                    Informe o Hash desejado:\n'''))

    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print('A hash MD5 de:' , string,  'é: ', resultado.hexdigest())
    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print('A hash SHA1 de:' , string,  'é: ', resultado.hexdigest())
    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print('A hash SHA256 de:' , string,  'é: ', resultado.hexdigest())
    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print('A hash SHA512 de:' , string,  'é: ', resultado.hexdigest())
    else:
        print('A opção selecionada é inválida')