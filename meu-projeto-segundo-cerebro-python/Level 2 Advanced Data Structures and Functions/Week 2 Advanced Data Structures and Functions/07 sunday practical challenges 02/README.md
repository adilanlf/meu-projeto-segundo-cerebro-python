# 📚 Índice de Códigos

- [🔐 Gerador de Senhas Aleatórias](#gerador-de-senhas-aleatorias)  
- [📇 Agenda de Contatos com Arquivo](#agenda-de-contatos-com-arquivo)  
- [📄 Leitor de Arquivo CSV Simples](#leitor-de-arquivo-csv-simples)  
- [📊 Mini-Estatísticas com Listas](#mini-estatisticas-com-listas)  
- [✂️ Jogo Pedra, Papel ou Tesoura](#jogo-pedra-papel-ou-tesoura)  








# 🔐 Gerador de Senhas Aleatórias <a id="gerador-de-senhas-aleatorias"></a>

Este código gera senhas aleatórias contendo letras, números e símbolos usando o módulo `random` e o conjunto de caracteres do módulo `string`.

---

### Como o código funciona?

1. **Definição da função `generate_password(length=10)`:**  
   - Define o conjunto de caracteres permitidos: letras maiúsculas e minúsculas, dígitos e símbolos (`string.ascii_letters + string.digits + string.punctuation`).  
   - Gera a senha escolhendo aleatoriamente caracteres desse conjunto pelo tamanho definido (padrão 10).  
   - Retorna a senha gerada como uma string.

2. **Geração e impressão da senha:**  
   - Chama a função com comprimento 12.  
   - Imprime a senha gerada.

---

### O que foi utilizado?

- Módulos `random` e `string` para geração aleatória e caracteres.  
- Função com parâmetro padrão para flexibilidade no tamanho da senha.  
- Compreensão de lista para montar a senha rapidamente.  
- Função `join()` para concatenar caracteres em uma string.

---

### O que o código faz, na prática?

- Gera senhas seguras e aleatórias com letras, números e símbolos.  
- Permite definir o tamanho da senha.  
- Exibe a senha para uso imediato.

---

### Simulação de uso e saída:

```plaintext
 Your password: w2R!e9#Kb@Lq
```
<br>




<br>

# 📇 Agenda de Contatos com Arquivo <a id="agenda-de-contatos-com-arquivo"></a>

Este programa permite **adicionar, listar e buscar contatos** salvos em arquivo `.txt`, usando funções e manipulação básica de arquivos.

---

### Como o código funciona?

1. **Função `add_contact(name, phone)`:**  
   - Abre o arquivo `contacts.txt` no modo append (`"a"`).  
   - Escreve o contato no formato `"nome,telefone\n"` para salvar.

2. **Função `list_contacts()`:**  
   - Abre o arquivo `contacts.txt` no modo leitura (`"r"`).  
   - Para cada linha, separa o nome e telefone com `.split(",")`.  
   - Imprime cada contato formatado, por exemplo: `"Alice: 1234-5678"`.

3. **Adiciona dois contatos exemplo:** Alice e Bob.  
4. **Lista todos os contatos salvos no arquivo.**

---

### O que foi utilizado?

- Manipulação de arquivos com `with open` para leitura e escrita segura.  
- Métodos de string `.strip()` e `.split()` para processar dados lidos do arquivo.  
- Estruturação em funções para organização e reutilização do código.  
- Impressão formatada com f-strings para exibir contatos de forma clara.

---

### O que o código faz, na prática?

- Salva contatos permanentemente em arquivo `.txt`.  
- Permite inserir novos contatos sem apagar os existentes.  
- Lista os contatos salvos mostrando nome e telefone formatados.

---

### Simulação de uso e saída:

```plaintext
Contact List:
 Alice: 1234-5678
 Bob: 9876-4321
```
<br>




<br>

# 📄 Leitor de Arquivo CSV Simples <a id="leitor-de-arquivo-csv-simples"></a>

Este código lê um arquivo `.csv` contendo nome e preço dos produtos, exibindo-os formatados na tela.

---

### Como o código funciona?

1. **Função `read_csv_file(filename)`:**  
   - Abre o arquivo no modo leitura (`"r"`).  
   - Lê todas as linhas com `readlines()`.  
   - Para cada linha, remove espaços com `.strip()` e divide os campos pelo caractere vírgula usando `.split(",")`.  
   - Imprime nome e preço formatados, por exemplo: `"Mouse -> R$50"`.

2. **Chama a função com o nome do arquivo `"products.csv"` para exibir seu conteúdo.**

---

### O que foi utilizado?

- Leitura de arquivos com `open` e `readlines()`.  
- Métodos de string `.strip()` e `.split()` para separar os dados.  
- Laço `for` para iterar sobre as linhas do arquivo.  
- Impressão formatada com f-string para exibir as informações de forma clara.

---

### O que o código faz, na prática?

- Lê dados de produtos armazenados em um arquivo CSV simples.  
- Exibe nome e preço dos produtos com formatação amigável.  
- Pode ser adaptado facilmente para outros arquivos CSV similares.

---

### Simulação de uso e saída:

```plaintext
Product List:
Mouse -> R$50
Keyboard -> R$100
Monitor -> R$800
```
<br>




<br>

# 📊 Mini-Estatísticas com Listas <a id="mini-estatisticas-com-listas"></a>

Este código recebe uma lista de notas e calcula a média, a maior e a menor nota, exibindo esses valores formatados.

---

### Como o código funciona?

1. **Função `stats(grades)`:**  
   - Calcula a média das notas usando `sum(grades) / len(grades)`.  
   - Obtém a maior nota com `max(grades)`.  
   - Obtém a menor nota com `min(grades)`.  
   - Imprime os resultados formatados, mostrando a média com duas casas decimais.

2. **Define uma lista de notas exemplo e chama a função `stats` para calcular e mostrar as estatísticas.**

---

### O que foi utilizado?

- Funções nativas do Python: `sum()`, `max()`, `min()` para cálculos simples.  
- Listas para armazenar as notas.  
- Impressão formatada com f-string para exibir a média com precisão.

---

### O que o código faz, na prática?

- Recebe uma coleção de notas.  
- Calcula e exibe estatísticas básicas: média, maior e menor valor.  
- Facilita a análise rápida do desempenho em avaliações.

---

### Simulação de uso e saída:

```plaintext
Average: 8.30
Highest: 10.0
Lowest: 6.8
```
<br>




<br>

# ✂️ Jogo Pedra, Papel ou Tesoura <a id="jogo-pedra-papel-ou-tesoura"></a>

Este projeto é um jogo simples onde o usuário escolhe entre pedra, papel ou tesoura para competir contra o computador, que faz uma escolha aleatória.

---

### Como o código funciona?

1. **Definição das opções:**  
   - A lista `options = ["rock", "paper", "scissors"]` contém as escolhas possíveis.

2. **Entrada do usuário:**  
   - Solicita que o usuário escolha uma opção e converte a resposta para minúsculas para facilitar a comparação.

3. **Escolha do computador:**  
   - Utiliza `random.choice(options)` para que o computador selecione aleatoriamente uma opção.

4. **Exibição das escolhas:**  
   - Imprime a escolha do usuário e do computador.

5. **Determinação do vencedor:**  
   - Se as escolhas forem iguais, o resultado é empate.  
   - Verifica se a combinação escolhida pelo usuário ganha do computador, segundo as regras do jogo.  
   - Caso contrário, o usuário perde.

---

### O que foi utilizado?

- Módulo `random` para geração de escolha aleatória do computador.  
- Entrada do usuário com `input()` e manipulação de string `.lower()`.  
- Estruturas condicionais (`if`, `elif`, `else`) para decidir o resultado.  
- Impressão formatada para mostrar as escolhas e resultado.

---

### O que o código faz, na prática?

- Permite interação divertida com o usuário.  
- Decide quem vence com base nas regras clássicas do jogo.  
- Exibe resultado final com mensagens claras e amigáveis.

---

### Simulação de uso e saída:

```plaintext
You chose: rock
Bot chose: scissors
You win!
```