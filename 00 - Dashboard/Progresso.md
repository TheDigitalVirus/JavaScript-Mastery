---
tipo: dashboard
tags:
  - javascript
  - progresso
---

# Progresso

## Aulas não iniciadas

```dataview
TABLE modulo, topico, dificuldade
FROM "01 - Variáveis e Strings"
WHERE status = "nao-iniciado"
SORT file.name ASC
```

## Aulas em estudo

```dataview
TABLE modulo, topico, dificuldade, revisao
FROM "01 - Variáveis e Strings"
WHERE status = "em-estudo"
SORT revisao ASC
```

## Aulas concluídas

```dataview
TABLE modulo, topico, dificuldade
FROM "01 - Variáveis e Strings"
WHERE status = "concluido"
SORT file.name ASC
```

## Revisões pendentes

```dataview
TABLE modulo, topico, revisao
FROM "01 - Variáveis e Strings"
WHERE revisao <= date(today) AND status != "concluido"
SORT revisao ASC
```

## Exercícios abertos

```dataview
TASK
FROM "Exercícios"
WHERE !completed
```
