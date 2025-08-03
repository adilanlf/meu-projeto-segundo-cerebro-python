# 📚 Índice de Códigos

- [📄 Leitor e Escritor de Arquivo TXT – Armazenar e Recuperar Dados de Clientes](#leitor-e-escritor-de-arquivo-txt--armazenar-e-recuperar-dados-de-clientes)  
- [📊 Manipulador Simples de CSV – Cálculo de Médias e Totais](#manipulador-simples-de-csv--cálculo-de-médias-e-totais)  
- [🌐 Consumidor de API Pública – Requisição e Exibição de Dados](#consumidor-de-api-pública--requisição-e-exibição-de-dados)  
- [📰 Web Scraping de Notícias – Extração e Salvamento de Títulos](#web-scraping-de-notícias--extração-e-salvamento-de-títulos)  
- [📅 Manipulação de Datas e Dados – Cálculo e Formatação](#manipulação-de-datas-e-dados--cálculo-e-formatação)  








# 📄 Leitor e Escritor de Arquivo TXT – Armazenar e Recuperar Dados de Clientes <a id="leitor-e-escritor-de-arquivo-txt--armazenar-e-recuperar-dados-de-clientes"></a>

Programa para armazenar dados de clientes em arquivo `.txt` e recuperá-los para visualização.

---

### Como o código funciona?

1. **Abertura do arquivo em modo escrita (`"w"`):**  
   - Cria ou sobrescreve o arquivo `clients.txt`.  
   - Escreve dados de clientes formatados (nome e e-mail).

2. **Abertura do arquivo em modo leitura (`"r"`):**  
   - Lê todo o conteúdo do arquivo usando `.read()`.

3. **Exibição dos dados:**  
   - Mostra as informações dos clientes no terminal.

---

### O que foi utilizado?

- Manipulação básica de arquivos com os modos `"w"` (escrita) e `"r"` (leitura).  
- Escrita de strings formatadas com quebra de linha (`\n`).  
- Leitura completa do conteúdo do arquivo com `.read()`.  
- Estrutura `with` para garantir fechamento automático do arquivo.

---

### O que o código faz, na prática?

- Armazena informações simples de clientes em um arquivo texto.  
- Permite recuperar e exibir essas informações posteriormente.  
- Facilita guardar dados persistentes de forma simples e rápida.

---

### Simulação de uso e saída:

```plaintext
Clients stored:
John Doe, johndoe@email.com
Jane Smith, janesmith@email.com
```
<br>




<br>

# 📊 Manipulador Simples de CSV – Cálculo de Médias e Totais <a id="manipulador-simples-de-csv--cálculo-de-médias-e-totais"></a>

Programa que lê dados numéricos de um arquivo `.csv` e calcula a média dos valores válidos da coluna `score`.

---

### Como o código funciona?

1. **Leitura do arquivo:**  
   - Obtém o caminho absoluto do arquivo `scores.csv`, localizado no mesmo diretório do script.  
   - Abre o arquivo com codificação UTF-8 e leitura segura usando `csv.DictReader`.

2. **Validação da estrutura:**  
   - Verifica se a coluna `score` existe no cabeçalho do CSV.  
   - Caso esteja ausente, exibe erro e finaliza o programa.

3. **Processamento das linhas:**  
   - Percorre cada linha a partir da segunda.  
   - Ignora valores vazios ou não numéricos, exibindo avisos claros para o usuário.

4. **Cálculo da média:**  
   - Se houver valores válidos, calcula a média e imprime com duas casas decimais.  
   - Se não houver valores válidos, exibe mensagem apropriada.

5. **Tratamento de exceções:**  
   - Detecta ausência do arquivo `scores.csv` e informa o caminho esperado.

---

### O que foi utilizado?

- Biblioteca `csv` com `DictReader` para leitura baseada em cabeçalho.  
- `os.path` para obter o caminho do arquivo com segurança.  
- `try/except` para lidar com arquivos ausentes ou dados inválidos.  
- Validação e limpeza de strings antes de conversão para `float`.  
- Mensagens de aviso detalhadas para auxiliar na depuração.

---

### O que o código faz, na prática?

- Lê uma planilha `.csv` com nomes e pontuações.  
- Ignora entradas inválidas ou vazias.  
- Calcula e imprime a média das pontuações válidas.  
- Garante robustez mesmo com dados imperfeitos.

---

### Simulação de uso e saída:

```plaintext
Warning: Line 5 - invalid value 'not_a_number' in 'score' column, skipping.
Warning: Line 6 - empty 'score' field, skipping.
Average score: 84.50
```
<br>




<br>

# 🌐 Consumidor de API Pública – Requisição e Exibição de Dados <a id="consumidor-de-api-pública--requisição-e-exibição-de-dados"></a>

Programa que faz requisição a uma API pública e exibe dados formatados na tela. Neste exemplo, uma piada aleatória é obtida de um serviço online.

---

### Como o código funciona?

1. **Requisição HTTP:**  
   - Utiliza a biblioteca `requests` para fazer uma chamada `GET` à URL da API de piadas.

2. **Leitura da resposta:**  
   - Converte a resposta JSON em um dicionário Python usando `.json()`.

3. **Exibição dos dados:**  
   - Extrai e imprime as chaves `setup` e `punchline`, que contêm a piada e sua resposta.

---

### O que foi utilizado?

- Biblioteca `requests` para realizar chamadas HTTP.  
- Método `.get()` para buscar dados da API.  
- `.json()` para converter a resposta em formato utilizável.  
- Impressão formatada com `f-strings` para exibir as informações de forma clara.

---

### O que o código faz, na prática?

- Acessa uma API pública de forma simples.  
- Extrai dados úteis de uma resposta JSON.  
- Mostra as informações de forma organizada para o usuário.  
- Serve como base para aplicações maiores que consomem dados externos.

---

### Simulação de uso e saída:

```plaintext
Joke: Did you hear about the guy who invented Lifesavers?
Answer: They say he made a mint.
```
<br>




<br>

# 📰 Web Scraping de Notícias – Extração e Salvamento de Títulos <a id="web-scraping-de-notícias--extração-e-salvamento-de-títulos"></a>

Programa para extrair títulos de notícias de uma página da web e salvar os resultados em um arquivo `.txt`.

---

### Como o código funciona?

1. **Requisição da página:**  
   - Utiliza `requests.get()` para buscar o conteúdo HTML da página de notícias da BBC.

2. **Análise do HTML:**  
   - Utiliza `BeautifulSoup` (comentado no exemplo) para fazer o parsing do HTML.  
   - Encontra todas as tags `<h3>`, onde os títulos costumam estar.

3. **Extração de texto:**  
   - Limita a coleta aos 5 primeiros títulos.  
   - Usa `.get_text(strip=True)` para remover espaços extras e tags HTML.

4. **Armazenamento:**  
   - Salva os títulos extraídos em um arquivo chamado `headlines.txt`.  
   - Também imprime os títulos numerados no terminal.

---

### O que foi utilizado?

- Biblioteca `requests` para obter o HTML da página.  
- Biblioteca `BeautifulSoup` (comentada no código) para processar e extrair conteúdo da estrutura HTML.  
- Escrita em arquivo com codificação UTF-8.  
- Laço `for` com `enumerate()` para limitar e numerar os títulos.

---

### O que o código faz, na prática?

- Automatiza a coleta de manchetes de uma fonte de notícias.  
- Facilita o monitoramento de conteúdo em tempo real.  
- Permite salvar os dados para uso posterior ou análise.

---

### Simulação de uso e saída:

```plaintext
1. Global markets rally on economic recovery hopes
2. Climate change report warns of extreme risks
3. New tech innovations in renewable energy
4. Sports update: local team wins championship
5. Health officials discuss vaccine rollout
```

> ⚠️ **Nota:** Este código está parcialmente comentado para evitar erros de execução em ambientes sem as dependências instaladas.  
> Para utilizar corretamente, certifique-se de instalar o `BeautifulSoup` com o comando abaixo e descomente as linhas relevantes do código:

```bash
pip install beautifulsoup4
```
<br>




<br>

# 📅 Manipulação de Datas e Dados – Cálculo e Formatação <a id="manipulação-de-datas-e-dados--cálculo-e-formatação"></a>

Programa para receber duas datas, calcular a diferença entre elas em dias e exibir a saída formatada.

---

### Como o código funciona?

1. **Entrada das datas:**  
   - As datas são definidas como strings no formato `"AAAA-MM-DD"`.

2. **Conversão para objetos `datetime`:**  
   - Usa `datetime.strptime()` para converter as strings em datas utilizáveis pelo Python.

3. **Cálculo da diferença:**  
   - Subtrai uma data da outra.  
   - Usa `.days` para obter a diferença em número de dias.

4. **Exibição formatada:**  
   - Imprime a quantidade de dias entre as duas datas.

---

### O que foi utilizado?

- Módulo `datetime` da biblioteca padrão do Python.  
- Método `strptime()` para converter strings em datas.  
- Operação de subtração entre objetos `datetime`.  
- Impressão formatada com `f-strings`.

---

### O que o código faz, na prática?

- Permite calcular quantos dias existem entre duas datas.  
- Facilita o controle de prazos e intervalos de tempo.  
- Pode ser adaptado para validações ou agendamentos.

---

### Simulação de uso e saída:

```plaintext
Days between 2025-08-01 and 2025-08-15: 14
```