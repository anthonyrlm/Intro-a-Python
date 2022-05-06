# variáveis
# strings
apelido = 'batatinha'
# números
idade = 25
altura = 1.75
# booleanos
possui_cnh = False

print(apelido)
print(idade + 5)
print(altura / 2)

# condicionais
if possui_cnh:
    print('Ok! Pode dirigir!')
else:
    print('Não, não diriga o meu carro')

# EXTRAIR DADOS DO USUARIO:
resposta = input('Você possui cnh?(s/n): ')
if resposta == 's':
    print('Ok! Pode dirigir meu carro!')
else:
    print('Não encoste no meu carro!')
