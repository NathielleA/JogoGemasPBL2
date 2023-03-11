# JogoGemasPBL2
Projeto do PBL 2 do 1° semestre : Jogo Gemas feito em Python 

Regras do jogo:
-	Primeiro passo: o jogador deve escolher o tamanho do tabuleiro, ou seja, a quantidade de colunas e linhas;
-	Para jogar e fazer pontos, o jogador deve mover de posição duas gemas adjacentes, para reunir 3 ou mais gemas da mesma cor;

 ->	PONTUAÇÃO:
-	Ao formar uma cadeia de gemas da mesma cor, elas são eliminadas, gerando pontos para o jogador igual a quantidade de gemas eliminadas;
-	Ao eliminar as gemas, novas irão “cair” no lugar; caso ao cair as gemas, novas cadeias se formem, elas serão automaticamente eliminadas e acrescidas na pontuação do jogador;

->	DICAS:
-	Durante o jogo, é possível obter dicas, que são fornecidas na forma da posição de uma gema cuja permutação com outra gema é válida. Cada dica obtida gera o desconto de 1 gema do total de pontos (dados pelo total de gemas destruídas anteriormente).
-	ATENÇÂO: Duas gemas são consideradas adjacentes se elas se encontram na mesma linha e em colunas adjacentes, ou se elas se encontram na mesma coluna e em linhas adjacentes (diagonais não fazem parte da adjacência).
-	O jogo acaba quando não houver combinações que geram cadeias de gemas.
