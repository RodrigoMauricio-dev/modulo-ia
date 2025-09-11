# Este programa é um simulador com fins educativos para ilustrar o conceito de
# ataque de força bruta. A senha e as tentativas são definidas de antemão.
# Use este conhecimento de forma responsável e ética.

import time

def ataque_de_forca_bruta_simulado():
    """
    Simula um ataque de força bruta para encontrar uma senha pré-definida.
    """
    senha_secreta = "pinguim123"
    
    # A lista de senhas que o programa vai "tentar"
    tentativas = [
        "123456",
        "senha1",
        "pinguim",
        "password",
        "pinguim123", # A senha correta
        "outrasenha"
    ]

    print("Iniciando simulação de ataque de força bruta...")
    print("-" * 40)
    
    # Itera sobre a lista de tentativas
    for tentativa in tentativas:
        print(f"Tentando: '{tentativa}'")
        time.sleep(0.5)  # Pequeno atraso para visualização

        # Verifica se a tentativa é a senha correta
        if tentativa == senha_secreta:
            print("-" * 40)
            print(f"SUCESSO! A senha '{senha_secreta}' foi encontrada!")
            return
            
    print("-" * 40)
    print("FALHA: A senha não foi encontrada na lista de tentativas.")

# Executa a simulação
ataque_de_forca_bruta_simulado()