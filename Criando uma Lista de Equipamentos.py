import sys


# Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []


# Crie um loop para solicitar os itens ao usuário:
for i in range(3):
    # Solicite o item e armazene na variável "item":
    item = sys.stdin.readline().strip()
    # Adicione o item à lista "itens":
    itens.append(item)


# Exibe a lista de itens
sys.stdout.write("Lista de Equipamentos:\n")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    sys.stdout.write(f"- {item}\n")