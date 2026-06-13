---
tipo: recurso
tags:
  - obsidian
  - plugins
  - recursos
---

# Plugins Recomendados

| Plugin | Para que serve |
|---|---|
| Dataview | Criar dashboards automáticos com metadados das notas. |
| Templater | Inserir templates inteligentes em novas notas. |
| Tasks | Gerenciar exercícios, revisões e checklists. |
| Spaced Repetition | Transformar perguntas em flashcards com repetição espaçada. |
| Calendar | Planejar estudos por dia. |
| QuickAdd | Criar notas rapidamente com fluxos personalizados. |
| Excalidraw | Fazer mapas mentais e desenhos. |
| Omnisearch | Melhorar a busca dentro do vault. |
| Canvas | Criar mapas visuais de conceitos. |

## Configuração mínima sugerida

- Ative backlinks.
- Ative graph view.
- Configure a pasta `Templates/` como pasta de templates.
- Configure notas diárias se quiser registrar rotina de estudo.

## Spaced Repetition - configuração dos flashcards

Para os cartões aparecerem em **Abrir uma nota para revisar**, use a tag padrão plural `#flashcards` ou uma subtag como `#flashcards/javascript/strings` antes dos cartões.

Formatos usados neste vault:

```md
#flashcards/javascript/strings
O que é uma string?:: Um tipo de dado usado para representar texto.
JavaScript usa ==tipagem dinâmica==.
```

Se a tela continuar mostrando que não há notas para revisar, confira nas configurações do plugin se a tag de flashcards está definida como `#flashcards`.

> Importante: a tela **Abrir uma nota para revisar** é a fila de revisão de notas inteiras e procura notas com `#review`. Para ver baralhos, use o comando **Review Flashcards from all notes** ou **Select a deck to cram**. Este vault agora usa `#review` nas aulas e `#flashcards` nos cartões para cobrir os dois fluxos.
