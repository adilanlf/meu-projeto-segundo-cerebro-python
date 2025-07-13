# 📚 Índice de Códigos

- [🧮 Calculadora Simples (com menu)](#calculadora-simples)
- [🔎 Validador de CPF (sem usar regex)](#validador-de-cpf)
- [🛒 Cadastro de Produtos com Menu (usando Lista e Dicionário)](#cadastro-de-produtos)
- [🔤 Contador de Vogais em uma Frase](#contador-de-vogais)
- [🎮 Jogo de Adivinhação com Tentativas Limitadas](#jogo-de-adivinhacao)








# 🧮 Calculadora Simples (com menu) <a id="calculadora-simples"></a>

Este código implementa uma **calculadora simples** que realiza as operações básicas de adição, subtração, multiplicação e divisão, usando funções, estruturas condicionais, laços de repetição, entrada do usuário, além de comentários e saídas simuladas.

---

### Como o código funciona?

1. **Definição das funções de operação:**  
   - `add(a, b)`: retorna a soma de `a` e `b`.  
   - `subtract(a, b)`: retorna a subtração de `b` de `a`.  
   - `multiply(a, b)`: retorna o produto de `a` e `b`.  
   - `divide(a, b)`: realiza a divisão de `a` por `b`. Caso `b` seja zero, retorna uma mensagem de erro `"Cannot divide by zero!"`.

2. **Menu interativo em loop:**  
   O programa entra em um laço `while True` que mantém o menu ativo até o usuário escolher sair.  
   Ele exibe as opções numeradas para o usuário escolher a operação desejada ou sair (`0`).

3. **Leitura da escolha do usuário:**  
   O usuário digita a opção desejada (exemplo: `1` para adição). Se escolher `0`, o programa imprime uma mensagem de despedida e termina o loop, encerrando a calculadora.

4. **Entrada dos números:**  
   Se a opção for válida e diferente de `0`, o programa solicita que o usuário informe dois números (float).

5. **Execução da operação selecionada:**  
   Com base na opção escolhida, chama a função correspondente passando os dois números digitados, e armazena o resultado.  
   Depois imprime o resultado da operação.  
   Caso o usuário escolha uma opção inválida, imprime mensagem de erro e volta ao menu.

---

### O que foi utilizado?

- **Funções:** para cada operação matemática, facilitando a organização do código.  
- **Estruturas condicionais (`if`, `elif`, `else`):** para tratar as escolhas do usuário.  
- **Laço de repetição `while`:** para manter o menu ativo até a saída.  
- **Entrada do usuário:** com `input()` para capturar opções e números.  
- **Tratamento básico de erro:** impedindo divisão por zero.  
- **Comentários:** para facilitar a leitura e entendimento do código.  

---

### O que o código faz, na prática?

- Apresenta um menu de operações para o usuário escolher.  
- Recebe os números para realizar a operação matemática escolhida.  
- Exibe o resultado ou uma mensagem de erro caso a operação não seja possível.  
- Permite que o usuário realize quantas operações desejar até escolher sair.

---

### Simulação de uso e saída:

```plaintext
=== Simple Calculator ===
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
0 - Exit
Choose an option: 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```
<br>





<br>

# 🔎 Validador de CPF (sem usar regex) <a id="validador-de-cpf"></a>

Esse código tem como objetivo **validar um número de CPF**, verificando se ele é válido ou não, sem usar expressões regulares (regex). O CPF pode ser digitado pelo usuário tanto no formato com pontuação (`xxx.xxx.xxx-xx`) quanto apenas os números juntos (`xxxxxxxxxxx`).

### Como o código funciona?

1. **Entrada do CPF:**  
   O programa recebe o CPF como entrada do usuário via `input()`. O usuário pode digitar o CPF com ou sem pontos e hífen.

2. **Limpeza da entrada:**  
   A função `validate_cpf` faz a remoção dos caracteres `.` (pontos) e `-` (hífen) com o método `.replace()`, além de remover espaços em branco nas extremidades com `.strip()`. Isso deixa o CPF apenas com os números.

3. **Validação básica da estrutura:**  
   - Verifica se o CPF contém exatamente **11 dígitos**.  
   - Verifica se todos os caracteres restantes são números (`cpf.isdigit()`).  
   Caso algum desses critérios falhe, retorna `False`, indicando CPF inválido.

4. **Filtro de CPFs inválidos com todos os dígitos iguais:**  
   CPFs como `11111111111`, `22222222222`, etc., são inválidos. O código checa isso comparando o CPF com o primeiro dígito repetido 11 vezes. Se for igual, retorna `False`.

5. **Cálculo do primeiro dígito verificador:**  
   - Para os primeiros 9 dígitos, multiplica cada um por um peso decrescente de 10 até 2, e soma os resultados.  
   - Multiplica essa soma por 10 e obtém o resto da divisão por 11 (`(sum1 * 10) % 11`).  
   - Se o resultado for 10, considera 0. Esse é o primeiro dígito verificador esperado.

6. **Cálculo do segundo dígito verificador:**  
   - Agora considera os primeiros 10 dígitos (os 9 originais mais o primeiro dígito verificador calculado).  
   - Multiplica cada um por um peso decrescente de 11 até 2, soma os resultados.  
   - Multiplica a soma por 10 e calcula o resto da divisão por 11.  
   - Se o resultado for 10, considera 0. Esse é o segundo dígito verificador esperado.

7. **Comparação dos dígitos verificadores:**  
   Compara os dois últimos dígitos do CPF fornecido com os dois dígitos verificadores calculados. Se coincidem, o CPF é válido (`True`); caso contrário, inválido (`False`).

---

### O que foi utilizado?

- **Entrada e saída básica:** `input()` para receber o CPF, `print()` para mostrar o resultado.  
- **Manipulação de strings:** `.replace()`, `.strip()`, `.isdigit()`.  
- **Estruturas condicionais:** `if` para validar as condições do CPF.  
- **Laços `for`:** para iterar sobre os dígitos e calcular os somatórios dos pesos.  
- **Operadores matemáticos:** multiplicação, resto da divisão `%`.  
- **Retorno booleano:** `True` ou `False` para indicar validade do CPF.  

---

### O que o código faz, na prática?

- Permite que o usuário insira um CPF em formatos diferentes (com ou sem pontuação).  
- Verifica se o CPF está estruturado corretamente (11 números, sem caracteres inválidos).  
- Filtra CPFs óbvios inválidos (todos os dígitos iguais).  
- Aplica o cálculo oficial dos dígitos verificadores do CPF, que é uma forma matemática de conferir a validade do número.  
- Retorna se o CPF é válido ou não, com mensagens claras para o usuário.

---

### Simulação de uso e saída:

```plaintext
Enter your CPF (only numbers or formatted): 529.982.247-25
 CPF is valid!
```
<br>





<br>

# 🛒 Cadastro de Produtos com Menu (usando Lista e Dicionário) <a id="cadastro-de-produtos"></a>

Este código implementa um **sistema simples de cadastro de produtos** com menu interativo. Ele permite adicionar produtos com nome e preço, remover produtos pelo nome, listar os produtos cadastrados e calcular a média de preços.

---

### Como o código funciona?

1. **Lista inicial vazia:**  
   O programa começa com uma lista chamada `products`, que armazena dicionários com as chaves `"name"` e `"price"` para cada produto.

2. **Menu com laço `while`:**  
   O menu principal é exibido repetidamente usando um `while True`, até o usuário escolher a opção de sair (`0`).

3. **Opção 1 – Adicionar produto:**  
   - O usuário informa o nome e o preço do produto.  
   - Um dicionário com esses dados é criado e adicionado à lista `products`.  
   - O programa confirma com uma mensagem usando f-string:  
     `"Banana added successfully."`

4. **Opção 2 – Remover produto:**  
   - O usuário digita o nome do produto que deseja remover.  
   - O programa procura esse nome (ignorando maiúsculas e minúsculas com `.lower()`), e se encontrar, remove o produto da lista.  
   - Se o produto não for encontrado, exibe: `"Product not found."`

5. **Opção 3 – Listar produtos:**  
   - Verifica se a lista está vazia.  
   - Se houver produtos, exibe a lista com nome e preço formatado (2 casas decimais):  
     `Banana - R$2.50`

6. **Opção 4 – Calcular média de preços:**  
   - Se a lista estiver vazia, mostra uma mensagem informando que não há produtos para calcular.  
   - Caso contrário, calcula a média dos preços somando todos os valores e dividindo pela quantidade de produtos:  
     `Average price: R$2.75`

7. **Opção inválida:**  
   - Caso o usuário digite algo fora do menu (por exemplo, `5`), o sistema responde: `"Invalid option. Try again."`

---

### O que foi utilizado?

- **Listas:** para armazenar os produtos cadastrados.  
- **Dicionários:** cada produto é representado como `{"name": ..., "price": ...}`.  
- **Laço `while`:** para manter o menu ativo até a saída.  
- **Condicionais (`if/elif/else`):** para tratar as opções do menu.  
- **Funções nativas:** `input()`, `print()`, `float()`, `sum()`, `len()`.  
- **f-strings:** para exibir mensagens formatadas com valores dinâmicos.  
- **Métodos de string:** `.lower()` para comparar nomes de forma case-insensitive.  

---

### O que o código faz, na prática?

- Cadastra novos produtos com nome e preço.  
- Permite remover produtos pelo nome.  
- Lista todos os produtos cadastrados com formatação.  
- Calcula e exibe a média de preços dos produtos.  
- Funciona de forma interativa e contínua até que o usuário escolha sair.

---

### Simulação de uso e saída:

```plaintext
=== PRODUCT MENU ===
1 - Add product
2 - Remove product
3 - List products
4 - Average price
0 - Exit
Choose an option: 1
Product name: Banana
Product price: 2.50
Banana added successfully.
```
<br>





<br>

# 🔤 Contador de Vogais em uma Frase <a id="contador-de-vogais"></a>

Este código implementa um programa simples que conta quantas **vogais (a, e, i, o, u)** existem em uma frase digitada pelo usuário. Ele desconsidera letras maiúsculas ou minúsculas, funcionando com qualquer tipo de entrada.

---

### Como o código funciona?

1. **Entrada do usuário:**  
   O programa solicita que o usuário digite uma frase usando `input()`.  
   Exemplo: `"Python is Amazing!"`

2. **Conversão para minúsculas:**  
   Para facilitar a verificação das vogais, a frase é convertida para **letras minúsculas** usando `.lower()`.  
   Assim, não importa se o usuário digitou `"A"` ou `"a"`, ambas serão tratadas igualmente.

3. **Definição das vogais e contador:**  
   - Define-se uma string com as vogais: `"aeiou"`  
   - Um contador (`count`) é inicializado com `0` para armazenar o número de vogais encontradas.

4. **Laço de repetição `for`:**  
   O programa percorre cada letra da frase digitada.  
   A cada letra, verifica se ela está presente na string de vogais (`if letter in vowels`).  
   Se for uma vogal, incrementa o contador em 1.

5. **Saída final:**  
   Após percorrer toda a frase, imprime o total de vogais encontradas com uma f-string:  
   `Number of vowels: 5`

---

### O que foi utilizado?

- **Entrada com `input()`:** para receber a frase do usuário.  
- **Conversão com `.lower()`:** para padronizar o texto em minúsculo.  
- **Estrutura `for`:** para iterar sobre cada caractere da frase.  
- **Condicional `if in`:** para verificar se o caractere é uma vogal.  
- **Contador:** para armazenar e somar o número de vogais encontradas.  
- **f-string:** para exibir o resultado de forma clara.

---

### O que o código faz, na prática?

- Lê uma frase digitada pelo usuário.  
- Converte a frase para letras minúsculas.  
- Percorre cada caractere verificando se é uma vogal.  
- Conta o total de vogais e exibe esse número na tela.  
- Funciona com qualquer tipo de frase, incluindo letras maiúsculas e minúsculas.

---

### Simulação de uso e saída:

```plaintext
Enter a sentence: Python is Amazing!
Number of vowels: 5
```
<br>





<br>

# 🎮 Jogo de Adivinhação com Tentativas Limitadas <a id="jogo-de-adivinhacao"></a>

Este projeto é um **jogo simples de adivinhação**, onde o usuário tem **três tentativas** para adivinhar um número secreto entre 1 e 10. O jogo fornece **dicas se o palpite está alto ou baixo**, e mostra mensagens claras de vitória ou derrota.

---

###  Como o código funciona

1. **Geração do número aleatório:**
   - Utiliza o módulo `random` para gerar um número secreto entre 1 e 10:
     ```python
     secret = random.randint(1, 10)
     ```

2. **Configuração do jogo:**
   - Define-se o número máximo de tentativas:
     ```python
     max_attempts = 3
     ```
   - Um contador `attempts` acompanha quantas tentativas já foram feitas.

3. **Início do jogo:**
   - Exibe uma mensagem explicando as regras:
     ```
     Guess the number between 1 and 10!
     You have 3 attempts.
     ```

4. **Loop principal (`while`):**
   - Enquanto o número de tentativas for menor que o máximo, o jogo continua pedindo palpites.
   - A entrada do usuário é convertida para inteiro com `int(input())`.

5. **Verificação do palpite:**
   - Se o usuário acertar, o jogo exibe:
     ```
     Correct! You won!
     ```
     e finaliza com `break`.
   - Se o palpite for **menor** que o número secreto:
     ```
     Too low.
     ```
   - Se for **maior**:
     ```
     Too high.
     ```

6. **Tentativas restantes:**
   - Após cada tentativa, o programa calcula e mostra quantas restam:
     ```python
     remaining = max_attempts - attempts
     ```

7. **Mensagem final (se perder):**
   - Quando as tentativas acabam sem acerto, exibe:
     ```
     You lost! The number was {secret}.
     ```

---

###  Recursos utilizados

- `import random` – para gerar números aleatórios.
- `while` – para manter o jogo rodando até esgotar as tentativas.
- `if / elif / else` – para comparar o palpite com o número secreto.
- `input()` e `int()` – para capturar e converter a entrada do usuário.
- `f-strings` – para formatar as mensagens dinamicamente.

---

###  O que esse código faz, na prática?

- Escolhe aleatoriamente um número entre 1 e 10.
- Permite até 3 tentativas do jogador para adivinhar o número.
- Informa se o palpite está **muito alto** ou **muito baixo**.
- Mostra o resultado final: vitória ou derrota.
- Exibe o número correto caso o jogador perca.

---

###  Exemplo de uso e saída

####  Quando o jogador acerta:

```plaintext
Guess the number between 1 and 10!
You have 3 attempts.
Your guess: 8
Too high.
You have 2 attempt(s) left.
Your guess: 5
Too low.
You have 1 attempt(s) left.
Your guess: 7
Correct! You won!