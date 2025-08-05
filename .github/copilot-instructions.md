# GitHub Copilot Instructions

## Project Overview

This is a Python learning repository with practice exercises and study notes from the "Python 3+ completo Course by Luiz Otávio Miranda". It contains standalone Python scripts demonstrating core concepts and practical applications.

## Project Structure & Organization

- **Root level**: Complete, runnable Python exercises and projects
- **`notasEstudo/`**: Study notes with detailed comments explaining Python concepts (lists, dicts, sets)
- **`projetoTest/`**: Package structure template with `src/` and `tests/` directories
- **No external dependencies**: All scripts use only Python standard library

## Coding Patterns & Conventions

### Input/Output Patterns

- **Interactive CLI apps**: Most scripts use `input()` for user interaction with validation loops
- **Menu-driven interfaces**: Use numbered options with input validation (see `calculadora.py`, `listaDeCompras.py`)
- **Error handling**: Wrap user input in try-except blocks with specific exception types

Example pattern from `calculadora.py`:

```python
try:
    numero1 = float(input("Digite o primeiro numero: "))
except ValueError:
    print("Por favor, digite apenas números válidos!")
    continue
```

### Algorithm Implementation Style

- **Step-by-step logic**: Complex algorithms broken into clear steps (see `verificadorCPF.py`, `geradorCPF.py`)
- **Educational comments**: Code includes Portuguese comments explaining mathematical/logical steps
- **Duplicate variable patterns**: Use descriptive names like `contador_regressivo_1`, `resultado_digito_1`

### Data Structure Usage

- **Sets for uniqueness**: Use `set()` to find duplicates efficiently (`encontreDuplicado.py`)
- **List comprehensions**: Prefer `[int(n) for n in numeros.split()]` for input parsing
- **Dictionary-driven logic**: Structure quiz/menu systems using dicts (`perguntasComDics.py`)

### Function Design

- **Closure patterns**: Use nested functions for configurability (`criandofucoes.py`)
- **Single responsibility**: Functions do one thing well (`exercicioFuncoes.py`)
- **Validation functions**: Separate validation logic into dedicated functions

## Development Workflow

### Running Scripts

- Execute directly: `python script_name.py`
- All scripts are standalone and don't require installation
- Use `os.system('cls')` for Windows console clearing (update for cross-platform if needed)

### Testing Approach

- Manual testing through CLI interaction
- Use predefined test data for algorithms (see `lista_de_listas_de_inteiros` in `encontreDuplicado.py`)
- No formal test framework currently used

### Brazilian Portuguese Context

- User-facing text in Portuguese
- Variable names in Portuguese for educational clarity
- Comments explain concepts in Portuguese

## Key Implementation Details

### CPF Algorithm Pattern

Both `geradorCPF.py` and `verificadorCPF.py` implement the Brazilian CPF validation algorithm:

- 9 base digits + 2 calculated check digits
- Uses modular arithmetic with decreasing multipliers
- Pattern: `((sum * 10) % 11)` with special case for values > 9

### Game Logic Pattern

`jogoPalavraSecreta.py` demonstrates:

- State tracking with string concatenation
- Character-by-character reveal logic
- Game loop with win condition checking

### Interactive Menu Pattern

Standard pattern for user interaction:

1. Display options with single-letter commands
2. Input validation with `continue` for invalid input
3. Clear screen between operations
4. Graceful exit option

When adding new features, follow these established patterns for consistency with the learning-focused, interactive nature of this codebase.

## Git Commit Message Conventions

When generating commit messages, follow these patterns:

### Format

```
tipo(escopo): descrição breve em português

Corpo da mensagem opcional explicando o que foi feito
e por que foi feito (não como foi feito).

Closes #issue-number (se aplicável)
```

### Tipos

- **feat**: nova funcionalidade ou exercício
- **fix**: correção de bug ou erro
- **docs**: documentação (README, comentários, notas de estudo)
- **style**: formatação, organização de código
- **refactor**: refatoração sem mudar funcionalidade
- **test**: adição ou correção de testes
- **chore**: tarefas de manutenção (configuração, etc.)

### Escopos Comuns

- **estoque**: sistema de controle de estoque
- **cpf**: gerador/verificador de CPF
- **calculadora**: aplicação calculadora
- **jogo**: jogo da palavra secreta
- **lista**: exercícios com listas
- **estudos**: notas de estudo
- **notas**: arquivos na pasta notasEstudo/

### Exemplos

```
feat(estoque): adicionar validação de produtos duplicados
fix(cpf): corrigir algoritmo de verificação do segundo dígito
docs(notas): adicionar exemplos de uso de sets
style(calculadora): melhorar formatação da interface
refactor(lista): simplificar lógica de validação de entrada
```

### Mensagens em Ingles

- Use Ingles para descrições
- Seja claro e direto sobre o que foi alterado
- Foque no **o quê** e **por quê**, não no **como**
