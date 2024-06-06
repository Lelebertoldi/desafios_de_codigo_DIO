class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades
    
    def __str__(self):
        return self.nome

# Função para recomendar o modelo de IA com base nas características desejadas
def recomendar_modelo(caracteristicas):
    modelos = criar_modelos()  # Chamada da função para criar a lista de modelos
    modelo_recomendado = None

    # Aqui é convertido as capacidades inseridas pelo usuário para minúsculas:
    capacidades_usuario = set(capacidade.lower() for capacidade in caracteristicas['Capacidades'])

    for modelo in modelos:
        # Convertemos as capacidades do modelo para minúsculas:
        capacidades_modelo = set(capacidade.lower() for capacidade in modelo.capacidades)
        
        if capacidades_usuario.issubset(capacidades_modelo):  # Verifica se as capacidades do usuário estão presentes no modelo
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."

# Função para criar uma lista de modelos de IA com suas características pontuadas
def criar_modelos():
    modelos = [
        ModeloIA("Claude 3 Opus", 9, 10, 5, ["pesquisa", "desenvolvimento acelerado"]),
        ModeloIA("Claude 3 Sonnet", 8, 5, 7, ["codificação", "recuperação de informações"]),
        ModeloIA("Claude 3 Haiku", 7, 9, 6, ["velocidade", "resumo de dados não estruturados"])
        # Adicione outros modelos conforme necessário
    ]
    return modelos

# Função para gerar uma explicação para o modelo recomendado
def gerar_explicacao(modelo, caracteristicas):
    if isinstance(modelo, ModeloIA):
        explicacao = f"O {modelo.nome} é o modelo recomendado."
        return explicacao
    else:
        return modelo

import sys

# Função para solicitar características desejadas ao usuário
def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(sys.stdin.readline())
    caracteristicas['Velocidade'] = int(sys.stdin.readline())
    caracteristicas['Custo'] = int(sys.stdin.readline())
    capacidades = sys.stdin.readline().strip().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
    return caracteristicas

# Aqui começa a execução do programa
caracteristicas_entrada = obter_caracteristicas()
melhor_modelo = recomendar_modelo(caracteristicas_entrada)
explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)

print(explicacao)
