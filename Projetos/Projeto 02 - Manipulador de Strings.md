---
tipo: projeto
status: nao-iniciado
tags:
  - javascript
  - projeto
  - strings
---

# Projeto 02 - Manipulador de Strings

## Objetivo

Praticar métodos de string em um pequeno fluxo de limpeza e formatação de texto.

## Requisitos

- [ ] Receber uma frase em uma variável.
- [ ] Remover espaços extras com `trim()`.
- [ ] Mostrar a frase em maiúsculas.
- [ ] Verificar se contém uma palavra específica com `includes()`.
- [ ] Extrair uma parte da frase com `slice()`.

## Exemplo inicial

```js
const entrada = "  aprendendo JavaScript com Obsidian  ";
const limpa = entrada.trim();

console.log(limpa.toUpperCase());
console.log(limpa.includes("JavaScript"));
console.log(limpa.slice(0, 10));
```
