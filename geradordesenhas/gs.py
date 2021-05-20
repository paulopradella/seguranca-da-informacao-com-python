import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja:\n'))

chars = string.ascii_letters + string.digits +  'ç!@#$%ˆ&*()-=+,.;:/?'

rnd = random.SystemRandom()

print(' '.join(rnd.choice(chars) for i in range(tamanho)))