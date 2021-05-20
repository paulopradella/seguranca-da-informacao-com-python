import  ctypes

pasta = input('Digite o caminho da pasta  ou arquivo que deseja ocultar:\n')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAtrributesW(pasta, atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')
