import os
#Importa a biblioteca/módulo OS que intera os programas e recursos do S.O.

print('#' * 60)
#imprime # por 60 vezes

ip_ou_host = input('Digite o IP ou Host a ser verificado:\n')
#criando uma variável, que vai receber o usuário um ip ou host
print('-' * 60)
#imprime - por 60 vezes
os.system('ping -c 6 {}'.format(ip_ou_host))
#chamando system da biblioteca os - comando:
# ping (OSX = -c Windows = -n) -num de pacotes que serão enviados.
print('-' * 60)
#imprime - por 60 vezes