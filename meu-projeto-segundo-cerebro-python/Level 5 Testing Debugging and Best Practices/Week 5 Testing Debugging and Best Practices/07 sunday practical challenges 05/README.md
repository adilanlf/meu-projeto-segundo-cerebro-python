# 📚 Índice de Códigos

- [✅ Validador de Dados com Erros Tratados – Criar um sistema que valida entrada de dados e informa erros específicos ao usuário](#validador-de-dados-com-erros-tratados--criar-um-sistema-que-valida-entrada-de-dados-e-informa-erros-específicos-ao-usuário)  
- [🧮 Calculadora com Testes Automatizados – Desenvolver uma calculadora e aplicar testes com unittest](#calculadora-com-testes-automatizados--desenvolver-uma-calculadora-e-aplicar-testes-com-unittest)  
- [♻️ Refatoração de Código Antigo – Pegar um código feito anteriormente e aplicar refatoração-boas-práticas-e-comentários](#refatoração-de-código-antigo--pegar-um-código-feito-anteriormente-e-aplicar-refatoração-boas-práticas-e-comentários)  
- [📝 Simulador de Cadastro com Logs – Simular cadastro de usuários com tratamento de exceções e salvamento de logs em .txt](#simulador-de-cadastro-com-logs--simular-cadastro-de-usuários-com-tratamento-de-exceções-e-salvamento-de-logs-em-txt)  
- [📂 Sistema com Menu Modularizado – Criar um programa com menu principal dividido em funções e testar o comportamento com assert](#sistema-com-menu-modularizado--criar-um-programa-com-menu-principal-dividido-em-funções-e-testar-o-comportamento-com-assert)  







# ✅ Validador de Dados com Erros Tratados – Criar um sistema que valida entrada de dados e informa erros específicos ao usuário <a id="validador-de-dados-com-erros-tratados--criar-um-sistema-que-valida-entrada-de-dados-e-informa-erros-específicos-ao-usuário"></a>

Programa que recebe um valor de idade como entrada, valida se está dentro de um intervalo aceitável e informa mensagens de erro claras em caso de valores inválidos.

---

### Como o código funciona?

1. **Função de validação:**  
   - `validate_age(age_str)` recebe a idade como string.  
   - Tenta converter o valor para inteiro (`int()`).

2. **Tratamento de erros:**  
   - Se a conversão falhar (`ValueError`), retorna uma mensagem indicando que o valor não é numérico.  
   - Se a idade estiver fora do intervalo de 0 a 120 anos, retorna mensagem de erro específica.  
   - Caso seja válida, retorna a idade formatada.

3. **Simulação de entradas:**  
   - Testa três casos: valor válido (`"25"`), valor fora do intervalo (`"-5"`) e valor não numérico (`"abc"`).

---

### O que foi utilizado?

- Conversão de string para inteiro com `int()`.  
- Estrutura `try/except` para tratamento de exceções (`ValueError`).  
- Condicionais (`if`) para validação de intervalo numérico.  
- Retorno de mensagens claras para o usuário.

---

### O que o código faz, na prática?

- Garante que a entrada do usuário seja um número inteiro.  
- Valida se está dentro de um intervalo aceitável para idade.  
- Retorna mensagens específicas conforme o tipo de erro encontrado.  
- Facilita a detecção e correção de entradas inválidas.

---

### Simulação de uso e saída:

```plaintext
Valid age: 25
Error: Age must be between 0 and 120.
Error: Invalid input. Please enter a number.
```
<br>




<br>

# 🧮 Calculadora com Testes Automatizados – Desenvolver uma calculadora e aplicar testes com unittest <a id="calculadora-com-testes-automatizados--desenvolver-uma-calculadora-e-aplicar-testes-com-unittest"></a>

Programa que implementa operações matemáticas simples e valida seu funcionamento por meio de testes automatizados utilizando a biblioteca `unittest`.

---

### Como o código funciona?

1. **Funções da calculadora:**  
   - `add(x, y)`: soma dois números.  
   - `subtract(x, y)`: subtrai o segundo número do primeiro.

2. **Classe de testes:**  
   - `TestCalculator` herda de `unittest.TestCase`.  
   - `test_add`: verifica se a soma de `5` e `3` resulta em `8`.  
   - `test_subtract`: verifica se a subtração de `10` e `7` resulta em `3`.

3. **Execução dos testes:**  
   - O bloco `if __name__ == '__main__': unittest.main()` executa todos os testes da classe automaticamente.

---

### O que foi utilizado?

- Funções simples para operações matemáticas.  
- Biblioteca `unittest` da biblioteca padrão do Python.  
- Métodos `assertEqual` para validar resultados esperados.  
- Estrutura modular para separação de código e testes.

---

### O que o código faz, na prática?

- Realiza operações básicas de soma e subtração.  
- Executa testes automatizados para garantir que as funções funcionem corretamente.  
- Mostra um relatório claro dos testes, informando se todos passaram.

---

### Simulação de uso e saída:

```plaintext
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
<br>




<br>

# ♻️ Refatoração de Código Antigo – Pegar um código feito anteriormente e aplicar refatoração, boas práticas e comentários <a id="refatoração-de-código-antigo--pegar-um-código-feito-anteriormente-e-aplicar-refatoração-boas-práticas-e-comentários"></a>

Exemplo de código que calculava a área de retângulos de forma repetitiva e foi refatorado para aplicar boas práticas, comentários e reduzir duplicação.

---

### Como o código funciona?

1. **Código antigo:**  
   - Calculava a área de cada retângulo repetindo a fórmula `largura * altura` diretamente no corpo do programa.  
   - Repetição de código, dificultando manutenção.

2. **Código refatorado:**  
   - Criada a função `calculate_area(width, height)` para encapsular o cálculo.  
   - Comentário de documentação (`docstring`) descreve o objetivo da função.  
   - Agora basta chamar a função para diferentes valores, evitando duplicação.

3. **Benefícios:**  
   - Código mais limpo, reutilizável e fácil de manter.  
   - Redução de linhas e centralização da lógica em uma única função.

---

### O que foi utilizado?

- Funções definidas pelo usuário (`def`).  
- Comentários de documentação (`""" """`).  
- Princípios DRY (*Don't Repeat Yourself*).  
- Impressão formatada para exibir resultados.

---

### O que o código faz, na prática?

- Calcula a área de retângulos com diferentes dimensões.  
- Elimina repetições desnecessárias no código.  
- Aplica boas práticas de organização e clareza.

---

### Simulação de uso e saída:

```plaintext
Area 1: 50
Area 2: 21
```
<br>




<br>

# 📝 Simulador de Cadastro com Logs – Simular cadastro de usuários com tratamento de exceções e salvamento de logs em .txt <a id="simulador-de-cadastro-com-logs--simular-cadastro-de-usuários-com-tratamento-de-exceções-e-salvamento-de-logs-em-txt"></a>

Programa que simula o processo de cadastro de usuários, validando dados de entrada e registrando erros em um arquivo de log para consulta posterior.

---

### Como o código funciona?

1. **Função de registro de erros (`log_error`):**  
   - Abre (ou cria) o arquivo `error_log.txt` no modo de adição (`"a"`).  
   - Registra a mensagem de erro com data e hora atuais.

2. **Função de cadastro (`register_user`):**  
   - Verifica se o nome de usuário tem pelo menos 3 caracteres.  
   - Converte a idade de string para inteiro e valida se é não negativa.  
   - Em caso de erro, levanta uma `ValueError` e registra no log.  
   - Caso válido, exibe mensagem de sucesso no terminal.

3. **Simulação de cadastros:**  
   - Testa três casos: nome curto, idade negativa e cadastro bem-sucedido.

---

### O que foi utilizado?

- Manipulação de arquivos com o modo de escrita e adição.  
- Biblioteca `datetime` para gerar timestamps.  
- Estrutura `try/except` para tratamento de exceções.  
- Validações com condicionais (`if`).  
- Registro persistente de erros para auditoria.

---

### O que o código faz, na prática?

- Realiza cadastro simulado de usuários.  
- Valida campos de entrada (nome e idade).  
- Registra erros em um arquivo `.txt` com data e hora.  
- Permite manter histórico de falhas para análise futura.

---

### Simulação de uso e saída:

```plaintext
Registration failed: Username must be at least 3 characters long.
Registration failed: Age cannot be negative.
User Bob registered successfully.
```
<br>




<br>

# 📂 Sistema com Menu Modularizado – Criar um programa com menu principal dividido em funções e testar o comportamento com assert <a id="sistema-com-menu-modularizado--criar-um-programa-com-menu-principal-dividido-em-funções-e-testar-o-comportamento-com-assert"></a>

Programa que apresenta um menu interativo, com cada opção implementada em funções separadas, e valida o comportamento das funções usando `assert`.

---

### Como o código funciona?

1. **Função `menu`:**  
   - Exibe as opções do menu (1, 2 e 3).  
   - Captura a escolha do usuário e a retorna.

2. **Funções de ação:**  
   - `say_hello()`: retorna `"Hello!"`.  
   - `say_goodbye()`: retorna `"Goodbye!"`.

3. **Função principal (`main`):**  
   - Loop `while True` mantém o programa em execução até o usuário escolher `"3"`.  
   - Cada opção chama a função correspondente.  
   - Entrada inválida exibe mensagem de erro.

4. **Testes com `assert`:**  
   - Antes da execução do menu, verifica se as funções retornam exatamente as strings esperadas.

---

### O que foi utilizado?

- Estrutura de funções para modularizar o código.  
- Loop `while` para manter o menu ativo.  
- Condicionais (`if/elif/else`) para controlar o fluxo.  
- Comando `assert` para testes simples e rápidos.

---

### O que o código faz, na prática?

- Apresenta um menu interativo para o usuário.  
- Executa funções de forma modular para cada ação.  
- Valida automaticamente o comportamento básico antes de iniciar o programa.  
- Garante maior organização e clareza do código.

---

### Simulação de uso e saída:

```plaintext
1. Say Hello
2. Say Goodbye
3. Exit
Choose an option: 1
Hello!
1. Say Hello
2. Say Goodbye
3. Exit
Choose an option: 2
Goodbye!
1. Say Hello
2. Say Goodbye
3. Exit
Choose an option: 3
Exiting...
```