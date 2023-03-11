#*******************************************************************************
#Autor: Nathielle Cerqueira Alves
#Componente Curricular: Algoritmos I
#Concluido em: 26/10/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************

#AQUI COMEÇA A MODULARIZAÇÃO (FUNÇÕES) DO CÓDIGO ------------------------------------------------------------------------------------------------

def criarTabuleiro(n, m): #Função que cria e preenche o tabuleiro, recebe como parâmetro o número de linhas e colunas do tabuleiro
    matriz = [] #matriz para o tabuleiro
    for i in range(n): #formação das linhas
        linha = []
        for j in range(m): #formação das colunas

            import random

            #lista com coloração das letras, descomentar essa e comentar a outra caso queira testar com coloração (mesmo processo na função novos índices)
            #c = ['\033[1;34mA\033[m', '\033[1;32mB\033[m', '\033[1;31mC\033[m', '\033[1;35mD\033[m', '\033[1;33mE\033[m', '\033[1;36mF\033[m', '\033[1;95mG\033[m', '\033[1;92mH\033[m', '\033[1;91mI\033[m', '\033[1;93mJ\033[m'] 
            
            c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #---> como a lista é sem a coloração das letras
            #Seleciona apenas os n primereiros ítens da lista para randomizar
            cores = []
            for i in range(0, m):  #importar o random para gerar cores aleatórias a partir do tamanho da tabela
                cores.append(c[i]) 

            linha.append(random.choice(cores)) #acrescenta um elemento na mesma linha e em colunas diferentes
        matriz.append(linha) #acrescenta a linha na matriz

    return matriz
#--------------------------------------------------------------------------------------------------------------------------------------------------

def exibirTabuleiro(tab, ncolunas, nlinhas, score): #função que recebe a matriz do tabuleiro e o exibe na forma adequada
    import time
    time.sleep(0.6) #função time para não mostrar os tabuleiros de uma vez só
    print()
    print("========== TABULEIRO ==========")
    print("\n     ", end = '')
    for i in range(0, ncolunas):
        print(i, " ", end = '') #índices das colunas
    print()
    print("     ", end = '')
    for i in range(0, ncolunas):
        print("---", end = '')
    print()

    for l in range(0, nlinhas):
        print(l, " | ", end = '') #índice das linhas
        for c in range(0, ncolunas):
            print(tab[l][c], " ", end = '')
        print() #para pular uma linha
    print("\nSUA PONTUAÇÃO: ", score)
#--------------------------------------------------------------------------------------------------------------------------------------------------

def permutacao(tab, L1, C1, L2, C2): #função para permutar as posições escolhidas pelo jogador
    
    if L1 == L2 and C1 == C2: #verifica se o jogador não colocou a posição 1 igual a posição 2
        return False
    elif L1 != L2 and C1 != C2: #verifica se o jogador não irá mover peças não adjacentes
        return False
    elif (C1 == C2 and (L2 > L1+1 or L2 < L1-1)) or (L1 == L2 and (C2 > C1+1 or C2 < C1-1)): #verifica se o jogador não irá mover uma peça não adjacente
        return False
    elif L1>linhas or L2>linhas or C1>colunas or C2>colunas: #verifica se o jogador colocou uma posição que não existe no tabuleiro
        return False
    else:
        guardaPosicao1 = tab[L1][C1] #salva a "cor" que está na posição 1 em uma variável e na posição 2 em outra, depois troca os valores
        guardaPosicao2 = tab[L2][C2]
        tab[L1][C1] = guardaPosicao2
        tab[L2][C2] = guardaPosicao1
    return tab
#--------------------------------------------------------------------------------------------------------------------------------------------------

def eliminarSequencia(tab, L, C): #função que elimina a cadeia de índices e conta os pontos
    if tab == False:
        return False

    if C>=5 or L>=5: #só fazem cadeias de 5 os tabuleiro maiores que 4x4
        for i in range(L): #horizontal
            for j in range(C-4):
               if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] and tab[i][j+2] == tab[i][j+3] and tab[i][j+3] == tab[i][j+4]):
                    tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i][j+3] = tab[i][j+4] = ' '  #elimina cadeia de 5 elementos iguais na horizontal
        
        i = j = 0 #zera as variáveis para o for da linha e da coluna
        for i in range(L):
            for j in range(C-3):
                if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] and tab[i][j+2] == tab[i][j+3]):
                    tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i][j+3] = ' ' #elimina cadeia de 4 elementos iguais na horizontal
        i = j = 0
        for i in range(L):
            for j in range(C-2):
                if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] ):
                    if (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+1] == tab[i-2][j+1]:  #eliminação em T virado para baixo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+1] = tab[i-2][j+1] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+1] == tab[i+2][j+1]:  #eliminação em T
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+1] = tab[i+2][j+1] = ' '

                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j] == tab[i-1][j]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i-1][j] = ' ' 
                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j+2] == tab[i-1][j+2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i-1][j+2] = ' '

                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j] == tab[i-2][j]: #eliminação em L 
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j] = tab[i-2][j] = ' '
                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+2] == tab[i-2][j+2]: #eliminação em L invertido
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+2] = tab[i-2][j+2] = ' '
                    
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j] == tab[i+2][j]:  #eliminação em L virado para baixo no lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i+2][j] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+2] == tab[i+2][j+2]:  #eliminação em L virado para baixo no lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i+2][j+2] = ' '
                    else:
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = ' ' #elimina cadeia de 3 elementos iguais na horizontal
        i = j = 0

        for i in range(L-4): #vertical
            for j in range(C):
               if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] and tab[i+2][j] == tab[i+3][j] and tab[i+3][j] == tab[i+4][j]):
                    tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+3][j] = tab[i+4][j] = ' '  #elimina cadeia de 5 elementos iguais na vertical
        i = j = 0
        for i in range(L-3):
            for j in range(C):
                if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] and tab[i+2][j] == tab[i+3][j]):
                    tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+3][j] = ' ' #elimina cadeia de 4 elementos iguais na vertical
        i = j = 0
        for i in range(L-2):
            for j in range(C):
                if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] ):
                    if (j+2) < C and (j+1) < C and tab[i][j] == tab[i+1][j+1] == tab[i+1][j+2]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j+1] = tab[i+1][j+2] = ' ' 
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+1][j-1] == tab[i+1][j-2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j-1] = tab[i+1][j-2] = ' '

                    elif (j+2) < C and (j+1) < C and tab[i][j] == tab[i+2][j+1] == tab[i+2][j+2]: #eliminação em L 
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j+1] = tab[i+2][j+2] = ' '
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+2][j-2] == tab[i+2][j-1]: #eliminação em L invertido
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j-2] = tab[i+2][j-1] = ' '
                    else:
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = ' ' #elimina cadeia de 3 elementos iguais na vertical
        i = j = 0     

    elif C==4 or L==4:
        for i in range(L): #horizontal
            for j in range(C-3):
                if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] and tab[i][j+2] == tab[i][j+3]):
                    tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i][j+3] = ' ' #elimina cadeia de 4 elementos iguais na horizontal
        i = j = 0
        for i in range(L):
            for j in range(C-2):
                if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] ):
                    if (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+1] == tab[i-2][j+1]:  #eliminação em T virado para baixo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+1] = tab[i-2][j+1] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+1] == tab[i+2][j+1]:  #eliminação em T
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+1] = tab[i+2][j+1] = ' '

                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j] == tab[i-1][j]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i-1][j] = ' ' 
                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j+2] == tab[i-1][j+2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i-1][j+2] = ' '

                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j] == tab[i-2][j]: #eliminação em L 
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j] = tab[i-2][j] = ' '
                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+2] == tab[i-2][j+2]: #eliminação em L invertido
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+2] = tab[i-2][j+2] = ' '

                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j] == tab[i+2][j]:  #eliminação em L virado para baixo no lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i+2][j] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+2] == tab[i+2][j+2]:  #eliminação em L virado para baixo no lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i+2][j+2] = ' '
                    else:
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = ' ' #elimina cadeia de 3 elementos iguais na horizontal
        i = j = 0

        for i in range(L-3): #vertical
            for j in range(C):
                if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] and tab[i+2][j] == tab[i+3][j]):
                    tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+3][j] = ' ' #elimina cadeia de 4 elementos iguais na vertical
        i = j = 0
        for i in range(L-2):
            for j in range(C):
                if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] ):
                    if (j+2) < C and (j+1) < C and tab[i][j] == tab[i+1][j+1] == tab[i+1][j+2]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j+1] = tab[i+1][j+2] = ' ' 
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+1][j-1] == tab[i+1][j-2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j-1] = tab[i+1][j-2] = ' '

                    elif (j+2) < C and (j+1) < C and tab[i][j] == tab[i+2][j+1] == tab[i+2][j+2]: #eliminação em L 
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j+1] = tab[i+2][j+2] = ' '
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+2][j-2] == tab[i+2][j-1]: #eliminação em L invertido
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j-2] = tab[i+2][j-1] = ' '
                    else:
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = ' ' #elimina cadeia de 3 elementos iguais na vertical
        i = j = 0

    elif C==3 or L==3:
        for i in range(L): #horizontal
            for j in range(C-2):
                if ( tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] ):
                    if (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+1] == tab[i-2][j+1]:  #eliminação em T virado para baixo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+1] = tab[i-2][j+1] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+1] == tab[i+2][j+1]:  #eliminação em T
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+1] = tab[i+2][j+1] = ' '

                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j] == tab[i-1][j]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i-1][j] = ' ' 
                    elif (i+1) < L and (i-1) >= 0 and tab[i][j] == tab[i+1][j+2] == tab[i-1][j+2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i-1][j+2] = ' '

                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j] == tab[i-2][j]: #eliminação em L 
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j] = tab[i-2][j] = ' '
                    elif (i-1) >= 0 and (i-2) >= 0 and tab[i][j] == tab[i-1][j+2] == tab[i-2][j+2]: #eliminação em L invertido
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i-1][j+2] = tab[i-2][j+2] = ' '
                        
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j] == tab[i+2][j]:  #eliminação em L virado para baixo no lado esquerdo
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j] = tab[i+2][j] = ' '
                    elif (i+1) < L and (i+2) < L and tab[i][j] == tab[i+1][j+2] == tab[i+2][j+2]:  #eliminação em L virado para baixo no lado direito
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = tab[i+1][j+2] = tab[i+2][j+2] = ' '
                    else:
                        tab[i][j] = tab[i][j+1] = tab[i][j+2] = ' ' #elimina cadeia de 3 elementos iguais na horizontal
        i = j = 0
        
        for i in range(L-2): #vertical
            for j in range(C):
                if ( tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] ):
                    if (j+2) < C and (j+1) < C and tab[i][j] == tab[i+1][j+1] == tab[i+1][j+2]:  #eliminação em T virado para o lado direito
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j+1] = tab[i+1][j+2] = ' ' 
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+1][j-1] == tab[i+1][j-2]:  #eliminação em T virado para o lado esquerdo
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+1][j-1] = tab[i+1][j-2] = ' '

                    if (j+2) < C and (j+1) < C and tab[i][j] == tab[i+2][j+1] == tab[i+2][j+2]: #eliminação em L 
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j+1] = tab[i+2][j+2] = ' '
                    elif (j-2) >= 0 and (j-1) >= 0 and tab[i][j] == tab[i+2][j-2] == tab[i+2][j-1]: #eliminação em L invertido
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = tab[i+2][j-2] = tab[i+2][j-1] = ' '
                    else:
                        tab[i][j] = tab[i+1][j] = tab[i+2][j] = ' ' #elimina cadeia de 3 elementos iguais na vertical
        i = j = 0

    check = 0
    for a in range(L): #verificação se fez e eliminou alguma cadeia, caso não tenha feito ele retorna False
            for b in range(C):
                if tab[a][b] == ' ':
                    check = 1
    if check == 0:
        return False

    return tab
#--------------------------------------------------------------------------------------------------------------------------------------------------

def deslocarColunas(tab, L, C):
    for a in range(L):
        for i in range(L-1, 0, -1):  #verificação é feita de baixo para cima 
            for j in range(C-1, -1, -1):
                if tab[i][j] == ' ':
                    desloca1 = tab[i][j]
                    desloca2 = tab[i-1][j]
                    tab[i][j] = desloca2
                    tab[i-1][j] = desloca1 #SÓ ESTÁ INDO COM CADEIAS NA HORIZONTAL
                
    return tab
#--------------------------------------------------------------------------------------------------------------------------------------------------

def somaPontuação(tab, L, C, score): #função para somar a a pontuação do jogador
    for i in range(L):
        for j in range(C):
            if tab[i][j] == ' ':
                score += 1
    return score
#--------------------------------------------------------------------------------------------------------------------------------------------------

#ESSA FUNÇÃO É DEPOIS DE DESLOCAR AS COLUNAS PARA BAIXO
def novosIndices(tab, L, C): #função que randomiza e adiciona os elementos nos lugares vazios
    import random
    #c = ['\033[1;34mA\033[m', '\033[1;32mB\033[m', '\033[1;31mC\033[m', '\033[1;35mD\033[m', '\033[1;33mE\033[m', '\033[1;36mF\033[m', '\033[1;95mG\033[m', '\033[1;92mH\033[m', '\033[1;91mI\033[m', '\033[1;93mJ\033[m']
    c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #---> lista sem a coloração das letras
    cores = []
    for i in range(0, C):
         cores.append(c[i])

    for i in range(L):
        for j in range(C):
            if tab[i][j] == ' ':
                tab[i][j] = random.choice(cores)

    return tab
#--------------------------------------------------------------------------------------------------------------------------------------------------

def obterDica(tab, L, C):
    for i in range(L):
        for j in range(C):
            if (j+1) < C and tab[i][j] == tab[i][j+1]: #Para DOIS ELEMENTOS IGUAIS JUNTOS na HORIZONTAL
                if (j-2) >= 0 and tab[i][j-2] == tab[i][j]:
                    return print(f"\nMova a posição {i, j-2} para a posição {i, j-1}")

                elif (i-1) >= 0 and (j-1) >= 0 and tab[i-1][j-1] == tab[i][j]:
                    return print(f"\nMova a posição {i-1, j-1} para a posição {i, j-1}")

                elif (i+1) < L and (j-1) >= 0 and tab[i+1][j-1] == tab[i][j]:
                    return print(f"\nMova a posição {i+1, j-1} para a posição {i, j-1}")

                elif (j+3) < C and tab[i][j+3] == tab[i][j]:
                    return print(f"\nMova a posição {i, j+3} para a posição {i, j+2}")

                elif (i-1) >= 0 and (j+2) < C and tab[i-1][j+2] == tab[i][j]:
                    return print(f"\nMova a posição {i-1, j+2} para a posição {i, j+2}")

                elif (i+1) < L and (j+2) < C and tab[i+1][j+2] == tab[i][j]:
                    return print(f"\nMova a posição {i+1, j+2} para a posição {i, j+2}")

                
            elif (j+2) < C and tab[i][j] == tab[i][j+2]:   #Para DOIS ELEMENTOS IGUAIS SEPARADOS na HORIZONTAL E UM IGUAL NO MEIO
                if (i-1) >= 0 and (j+1) < C and tab[i-1][j+1] == tab[i][j]:
                    return print(f"\nMova a posição {i-1, j+1} para a posição {i, j+1}")

                elif (i+1) < L and (j+1) < C and tab[i+1][j+1] == tab[i][j]:
                    return print(f"\nMova a posição {i+1, j+1} para a posição {i, j+1}")


            elif (i+1) < L and tab[i][j] == tab[i+1][j]:   #Para DOIS ELEMENTOS IGUAIS JUNTOS na VERTICAL
                if (i-2) >= 0 and tab[i-2][j] == tab[i][j]:
                    return print(f"\nMova a posição {i-2, j} para a posição {i-1, j}")

                elif (i-1) >= 0 and (j-1) >= 0 and tab[i-1][j-1] == tab[i][j]:
                    return print(f"\nMova a posição {i-1, j-1} para a posição {i-1, j}")

                elif (i-1) >= 0 and (j+1) < C and tab[i-1][j+1] == tab[i][j]:
                    return print(f"\nMova a posição {i-1, j+1} para a posição {i-1, j}")

                elif (i+3) < L and tab[i+3][j] == tab[i][j]:
                    return print(f"\nMova a posição {i+3, j} para a posição {i+2, j}")

                elif (i+2) < L and (j-1) >= 0 and tab[i+2][j-1] == tab[i][i]:
                    return print(f"\nMova a posição {i+2, j-1} para a posição {i+2, j}")

                elif (i+2) < L and (j+1) < C and tab[i+2][j+1] == tab[i][j]:
                    return print(f"\nMova a posição {i+2, j+1} para a posição {i+2, j}")

                
            elif (i+2) < L and tab[i][j] == tab[i+2][j]:  #Para DOIS ELEMENTOS IGUAIS SEPARADOS na VERTICAL E UM IGUAL NO MEIO
                if (i+1) < L and (j-1) >= 0 and tab[i+1][j-1] == tab[i][j]:
                    return print(f"\nMova a posição {i+1, j-1} para a posição {i+1, j}")
                    
                elif (i+1) < L and (j+1) < C and tab[i+1][j+1] == tab[i][j]:
                    return print(f"\nMova a posição {i+1, j+1} para a posição {i+1, j}")
#--------------------------------------------------------------------------------------------------------------------------------------------------

def verificarTabuleiro(tab, L, C): #função para verificar se ainda há possibilidade de cadeias
    for i in range(L):
        for j in range(C):
            if (j+1) < C and tab[i][j] == tab[i][j+1]: #Para DOIS ELEMENTOS IGUAIS JUNTOS na HORIZONTAL
                if (j-2) >= 0 and tab[i][j-2] == tab[i][j]:
                    return True
                elif (i-1) >= 0 and (j-1) >= 0 and tab[i-1][j-1] == tab[i][j]:
                    return True
                elif (i+1) < L and (j-1) >= 0 and tab[i+1][j-1] == tab[i][j]:
                    return True
                elif (j+3) < C and tab[i][j+3] == tab[i][j]:
                    return True
                elif (i-1) >= 0 and (j+2) < C and tab[i-1][j+2] == tab[i][j]:
                    return True
                elif (i+1) < L and (j+2) < C and tab[i+1][j+2] == tab[i][j]:
                    return True

                
            elif (j+2) < C and tab[i][j] == tab[i][j+2]:   #Para DOIS ELEMENTOS IGUAIS SEPARADOS na HORIZONTAL E UM IGUAL NO MEIO
                if (i-1) >= 0 and (j+1) < C and tab[i-1][j+1] == tab[i][j]:
                    return True
                elif (i+1) < L and (j+1) < C and tab[i+1][j+1] == tab[i][j]:
                    return True


            elif (i+1) < L and tab[i][j] == tab[i+1][j]:   #Para DOIS ELEMENTOS IGUAIS JUNTOS na VERTICAL
                if (i-2) >= 0 and tab[i-2][j] == tab[i][j]:
                    return True
                elif (i-1) >= 0 and (j-1) >= 0 and tab[i-1][j-1] == tab[i][j]:
                    return True
                elif (i-1) >= 0 and (j+1) < C and tab[i-1][j+1] == tab[i][j]:
                    return True
                elif (i+3) < L and tab[i+3][j] == tab[i][j]:
                    return True
                elif (i+2) < L and (j-1) >= 0 and tab[i+2][j-1] == tab[i][j]:
                    return True
                elif (i+2) < L and (j+1) < C and tab[i+2][j+1] == tab[i][j]:
                    return True
                
                
            elif (i+2) < L and tab[i][j] == tab[i+2][j]:  #Para DOIS ELEMENTOS IGUAIS SEPARADOS na HORIZONTAL E UM IGUAL NO MEIO
                if (i+1) < L and (j-1) >= 0 and tab[i+1][j-1] == tab[i][j]:
                    return True
                elif (i+1) < L and (j+1) < C and tab[i+1][j+1] == tab[i][j]:
                    return True
                
                
#AQUI COMEÇA O MAIN-----------------------------------------------------------------------------------------------------------------------------
print("\n================================================================")
print("                        Bem-vindo ao Gemas!                     ")
print("================================================================")

print("\n------------------------------------------------------------- REGRAS DO JOGO -----------------------------------------------------------------------")
print(
    "\n1) Primeiro passo: escolher o tamanho do tabuleiro, o numero de linhas e colunas;"
    "\n2) Para marcar pontos você deve mover de posição duas gemas (cores representadas pelas letras) adjacentes e formar uma cadeia com 3 ou mais cores iguais;"
    "\n3) Para fazer a movimentação, indique a linha e coluna da 1º posição e a linha e a coluna da 2º posição, respectivamente;"
    "\n4) Ao formar uma cadeia de gemas da mesma cor, elas são eliminadas;"
    "\n5) Cada gema eliminada equivale a um ponto;"
    "\n6) Após a sequência eliminada, as gemas acima irão descer e novas gemas serão geradas nos lugares vazios;" 
    "\n7) Caso cadeias se formem ao gerar novas cores, elas serão automaticamente eliminadas e acrescidas na pontuação;"
    "\n8) DICAS: durante o jogo, é possível obter dicas, que são fornecidas na forma das posições a serem permutadas para formar uma sequência;"
    "\n9) Cada dica obtida gera o desconto de 1 gema do total de pontos (dados pelo total de gemas destruídas anteriormente);"
    "\n10) ATENÇÃO: Duas gemas são consideradas adjacentes se elas se encontram na mesma linha ou na mesma coluna, diagonais não fazem parte da adjacência;"
    "\n11) O jogo acaba quando não houver mais combinações que gerem cadeias de gemas iguais."
)
print("\n---------------------------------------------------------------- BOM JOGO --------------------------------------------------------------------------")

linhas = input("\nDigite o número de linhas do tabuleiro (min: 3, max: 10): ")
colunas = input("Digite o número de colunas do tabuleiro (min: 3, max: 10): ")

while True:
    if linhas.isnumeric() == True and colunas.isnumeric() == True: #verificação caso os dados de entrada não sejam numéricos
        linhas = int(linhas)
        colunas = int(colunas)
        if linhas >= 3 and linhas <= 10 and colunas >= 3 and colunas <= 10: #verificação caso os dados de entrada não indiquem um tamanho apropriado
            break
        else:
            print("\nTamanho inválido!")
        linhas = input("\nDigite o número de linhas do tabuleiro (min: 3, max: 10): ")
        colunas = input("Digite o número de colunas do tabuleiro (min: 3, max: 10): ")
    else:
        print("\nDados inválidos!")
        linhas = input("\nDigite o número de linhas do tabuleiro (min: 3, max: 10): ")
        colunas = input("Digite o número de colunas do tabuleiro (min: 3, max: 10): ")

tabuleiro = criarTabuleiro(linhas, colunas) #chamada da função para criar o tabuleiro de acordo com as dimensões dadas pelo jogador

while True: #para verificar sequencias já formadas no início do jogo 
    if eliminarSequencia(tabuleiro, linhas, colunas) == False:
        break
    else:
        tabuleiro = eliminarSequencia(tabuleiro, linhas, colunas)
        tabuleiro = deslocarColunas(tabuleiro, linhas, colunas)
        tabuleiro = novosIndices(tabuleiro, linhas, colunas)

check = verificarTabuleiro(tabuleiro, linhas, colunas)
pontuacao = 0
exibirTabuleiro(tabuleiro, colunas, linhas, pontuacao)
   
while check == True:  #Aqui o jogo começa. Enquanto o tabuleiro tiver possibilidades de permutação ele irá repetir esse while:
    
    print("\nPara qual posição deseja mover?")

    if pontuacao > 0:
        #essa condicional é para a dica: caso a pontuação seja suficiente, ele exibi esse print
        print('-'*55)
        print("Se desejar obter uma DICA digite d em todas as posições")
        print('-'*55)

    posicao1linha = (input("\nLinha da posição 1: ")) #input para a entrada das posições (linha e coluna) para permutar
    posicao1coluna = (input("Coluna da posição 1: "))
    posicao2linha = (input("\nLinha da posição 2: "))
    posicao2coluna = (input("Coluna da posição 2: "))

    while True:
        if posicao1linha.isnumeric() == True and posicao1coluna.isnumeric() == True \
            and posicao2linha.isnumeric() == True and posicao2coluna.isnumeric() == True:  #verifica se o jogador digitou um valor numérico
            posicao1linha = int(posicao1linha)
            posicao1coluna = int(posicao1coluna)
            posicao2linha = int(posicao2linha)
            posicao2coluna = int(posicao2coluna)
            break
        elif posicao1linha == posicao1coluna == posicao2linha == posicao2coluna == 'd':
            #caso o jogador peça a dica, ela é exibida no painel
            obterDica(tabuleiro2, linhas, colunas)
            pontuacao -= 1
            print("\nPara qual posição deseja mover?")
            posicao1linha = (input("\nLinha da posição 1: "))
            posicao1coluna = (input("Coluna da posição 1: "))
            posicao2linha = (input("\nLinha da posição 2: "))
            posicao2coluna = (input("Coluna da posição 2: "))
        else:
            print("\nPosição inválida!")
            print("\nPara qual posição deseja mover?")
            posicao1linha = (input("\nLinha da posição 1: "))
            posicao1coluna = (input("Coluna da posição 1: "))
            posicao2linha = (input("\nLinha da posição 2: "))
            posicao2coluna = (input("Coluna da posição 2: "))

    tabuleiroTeste = permutacao(list(map(list, tabuleiro)), posicao1linha, posicao1coluna, posicao2linha, posicao2coluna)
    #para evitar que a permutação seja feita mesmo estando errada (não formando sequência), 
    #foi modificado apenas um tabuleiro teste para verificação dos dados.

    if tabuleiroTeste == False or eliminarSequencia(list(map(list, tabuleiroTeste)), linhas, colunas) == False: #verifica se a permutação foi válida e fez uma sequência com uma cópia da matriz
        check2 = False #variável para verificação no while
        while check2 == False: #verifica se a permutação foi válida
            print("\nTroca inválida!")
            print("\nPara qual posição deseja mover?")

            if pontuacao > 0:
                print('-'*55)
                print("Se desejar obter uma DICA digite d em todas as posições")
                print('-'*55)

            posicao1linha = (input("\nLinha da posição 1: "))
            posicao1coluna = (input("Coluna da posição 1: "))
            posicao2linha = (input("\nLinha da posição 2: "))
            posicao2coluna = (input("Coluna da posição 2: "))

            while True:
                if posicao1linha.isnumeric() == True and posicao1coluna.isnumeric() == True \
                    and posicao2linha.isnumeric() == True and posicao2coluna.isnumeric() == True: #usando o isnumeric() para verificar se é um valor numérico      
                    posicao1linha = int(posicao1linha)
                    posicao1coluna = int(posicao1coluna)
                    posicao2linha = int(posicao2linha)
                    posicao2coluna = int(posicao2coluna)
                    break #sendo verdade, sai do loop e continua o jogo
                elif posicao1linha == posicao1coluna == posicao2linha == posicao2coluna == 'd':
                    #caso o jogador digite 'd' para todas as posições a função dica é chamada
                    obterDica(tabuleiro2, linhas, colunas)
                    pontuacao -= 1
                    print("\nPara qual posição deseja mover?")
                    posicao1linha = (input("\nLinha da posição 1: "))
                    posicao1coluna = (input("Coluna da posição 1: "))
                    posicao2linha = (input("\nLinha da posição 2: "))
                    posicao2coluna = (input("Coluna da posição 2: "))
                else:
                    print("\nPosição inválida!")
                    print("\nPara qual posição deseja mover?")
                    posicao1linha = (input("\nLinha da posição 1: "))
                    posicao1coluna = (input("Coluna da posição 1: "))
                    posicao2linha = (input("\nLinha da posição 2: "))
                    posicao2coluna = (input("Coluna da posição 2: "))
            
            tabuleiroTeste = permutacao(list(map(list, tabuleiro)), posicao1linha, posicao1coluna, posicao2linha, posicao2coluna)
            if not(tabuleiroTeste == False):
                if not(eliminarSequencia(list(map(list, tabuleiroTeste)), linhas, colunas) == False):
                    check2 = True #se a permutação for válida ele para de verificar
    
    tabuleiro2 = permutacao(tabuleiro, posicao1linha, posicao1coluna, posicao2linha, posicao2coluna) #quando a verificação acaba, ele modifica o tabuleiro original

    exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

    tabuleiro2 = eliminarSequencia(tabuleiro2, linhas, colunas) #função para verificar se fez uma cadeia e se fizer, eliminar ela
    pontuacao = somaPontuação(tabuleiro2, linhas, colunas, pontuacao) #acrescenta as gemas eliminadas a pontuação
    exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao) #o tabuleiro é exibido a cada modificação

    tabuleiro2 = deslocarColunas(tabuleiro2, linhas, colunas) #As colunas acima passam para os espaços vazios embaixo
    exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

    tabuleiro2 = novosIndices(tabuleiro2, linhas, colunas) #função para randomizar novos elementos nas posições vazias
    exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

    while True: #para verificar se os novos índices formaram novas sequências
        #esse loop se repete até não ter mais sequências formadas espontâneamente
        if eliminarSequencia(tabuleiro2, linhas, colunas) == False:
            break
        else:
            tabuleiro2 = eliminarSequencia(tabuleiro2, linhas, colunas) #função para verificar se fez uma cadeia e se fizer eliminar ela
            pontuacao = somaPontuação(tabuleiro2, linhas, colunas, pontuacao)
            exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

            tabuleiro2 = deslocarColunas(tabuleiro2, linhas, colunas)
            exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

            tabuleiro2 = novosIndices(tabuleiro2, linhas, colunas) #função para randomizar novos elementos nas posições vazias
            exibirTabuleiro(tabuleiro2, colunas, linhas, pontuacao)

    check = verificarTabuleiro(tabuleiro, linhas, colunas)
    #função para verificar se ainda há possibilidade de cadeias, se sim:
       #pergunta novamente sobre a posição para troca
    #Se não:
       # O while encerra, jogo acaba e a pontuação final é exibida

print("\nNÃO HÁ MAIS PERMUTAÇÕES VÁLIDAS --- JOGO ENCERRADO!")
print(f"Sua Pontuação Final --- {pontuacao} pontos")
print("Reinicie o jogo para outra partida.")