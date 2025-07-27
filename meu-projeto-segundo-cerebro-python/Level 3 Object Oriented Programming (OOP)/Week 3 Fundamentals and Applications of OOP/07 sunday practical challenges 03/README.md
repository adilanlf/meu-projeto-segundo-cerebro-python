# 📚 Índice de Códigos

- [🎓 Student and Teacher Registry – OOP, Inheritance, Encapsulation](#student-and-teacher-registry--oop-inheritance-encapsulation)  
- [🗡️ RPG Characters – Inheritance and Methods](#rpg-characters--inheritance-and-methods)  
- [🏦 Simple Bank System – No Negative Balance](#simple-bank-system--no-negative-balance)  
- [📅 Date Handler Class – Validation and Formatting](#date-handler-class--validation-and-formatting)  
- [🐾 Polymorphism Exercise – Method Override](#polymorphism-exercise--method-override)  








# 🎓 Student and Teacher Registry – OOP, Inheritance, Encapsulation <a id="student-and-teacher-registry--oop-inheritance-encapsulation"></a>

Este código implementa um registro simples de estudantes e professores usando **programação orientada a objetos (OOP)**, com herança e encapsulamento básico.

---

### Como o código funciona?

1. **Classe base `Person`:**  
   - Possui atributos privados `_name` e `_age` com getters via `@property`.  
2. **Subclasse `Student`:**  
   - Herda de `Person`.  
   - Adiciona atributo `grade`.  
3. **Subclasse `Teacher`:**  
   - Herda de `Person`.  
   - Adiciona atributo `subject`.  
4. **Criação de instâncias:**  
   - Um estudante e um professor são criados e seus dados exibidos.

---

### O que foi utilizado?

- Herança para reutilizar código entre `Student` e `Teacher`.  
- Encapsulamento com atributos privados e propriedades getter.  
- Construtores para inicializar objetos com parâmetros personalizados.  
- Impressão formatada com f-strings.

---

### O que o código faz, na prática?

- Representa pessoas, estudantes e professores de forma estruturada.  
- Permite acessar dados importantes de forma controlada.  
- Demonstra princípios básicos de OOP em Python.

---

### Simulação de uso e saída:

```plaintext
Student: Anna, Age: 20, Grade: 10th Grade
Teacher: Mr. Smith, Age: 40, Subject: Mathematics
```
<br>




<br>

# 🗡️ RPG Characters – Inheritance and Methods <a id="rpg-characters--inheritance-and-methods"></a>

Este código cria personagens de RPG com atributos e métodos usando herança para diferenciar tipos de personagens (guerreiro e mago).

---

### Como o código funciona?

- **Classe base `Character`:**  
  - Define nome, vida (`health`), ataque e defesa.  
  - Método `hit` calcula dano e aplica ao alvo.

- **Subclasses `Warrior` e `Mage`:**  
  - Inicializam personagens com estatísticas específicas.

- **Teste de batalha:**  
  - Dois personagens atacam um ao outro.

---

### O que foi utilizado?

- Herança para especializar personagens.  
- Método para ações entre objetos (`hit`).  
- Uso do `max()` para evitar dano negativo.  
- Impressão das ações em tempo real.

---

### O que o código faz, na prática?

- Simula ataques entre personagens com atributos distintos.  
- Demonstra interação entre objetos via métodos.  
- Pode ser base para um jogo simples de RPG.

---

### Simulação de uso e saída:

```plaintext
Thor hits Merlin for 15 damage.
Merlin hits Thor for 20 damage.
```
<br>




<br>

# 🏦 Simple Bank System – No Negative Balance <a id="simple-bank-system--no-negative-balance"></a>

Sistema bancário simples com validação para evitar saldo negativo em saques.

---

### Como o código funciona?

- **Classe `SimpleAccount`:**  
  - Atributos para dono e saldo inicial.

- **Método `deposit`:**  
  - Aceita apenas valores positivos.  
  - Atualiza o saldo.

- **Método `withdraw`:**  
  - Permite saque somente se saldo for suficiente.  
  - Atualiza saldo ou mostra erro.

---

### O que foi utilizado?

- Validação simples em métodos para manter consistência.  
- Impressão de mensagens para feedback do usuário.  
- Encapsulamento simples via métodos públicos.

---

### O que o código faz, na prática?

- Permite depósitos e saques com segurança básica.  
- Evita que o saldo fique negativo.  
- Fornece mensagens claras sobre operações.

---

### Simulação de uso e saída:

```plaintext
50 deposited. New balance: 150
30 withdrawn. New balance: 120
Withdrawal failed: insufficient funds.
```
<br>




<br>

# 📅 Date Handler Class – Validation and Formatting <a id="date-handler-class--validation-and-formatting"></a>

Classe para manipular datas com validação simples e formatação.

---

### Como o código funciona?

- **Classe `DateHandler`:**  
  - Armazena dia, mês e ano.

- **Método `is_valid`:**  
  - Verifica se dia está entre 1 e 31 e mês entre 1 e 12.

- **Método `format_date`:**  
  - Retorna a data formatada como `DD/MM/AAAA`.

- **Teste de validade e exibição.**

---

### O que foi utilizado?

- Validação básica com operadores relacionais.  
- Formatação com f-strings e preenchimento com zeros.  
- Métodos para encapsular comportamento.

---

### O que o código faz, na prática?

- Verifica se uma data tem valores possíveis.  
- Formata a data para visualização amigável.  
- Pode ser base para manipulação de datas simples.

---

### Simulação de uso e saída:

```plaintext
Date is valid: 05/07/2025
```
<br>




<br>

# 🐾 Polymorphism Exercise – Method Override <a id="polymorphism-exercise--method-override"></a>

Exercício de polimorfismo demonstrando sobrescrita de métodos em classes derivadas.

---

### Como o código funciona?

- **Classe base `Animal`:**  
  - Método `speak` padrão retorna `"Some sound"`.

- **Subclasses `Dog` e `Cat`:**  
  - Sobrescrevem `speak` para retornarem sons específicos.

- **Lista de animais com tipos diferentes.**  
- **Iteração e chamada de método para cada objeto.**

---

### O que foi utilizado?

- Polimorfismo via sobrescrita de método.  
- Lista heterogênea de objetos.  
- Loop para demonstrar comportamento dinâmico.

---

### O que o código faz, na prática?

- Demonstra como objetos diferentes respondem de forma distinta ao mesmo método.  
- Facilita extensibilidade do código para novas classes.  
- Ajuda a entender conceitos fundamentais de OOP.

---

### Simulação de uso e saída:

```plaintext
Woof!
Meow!
Some sound
```