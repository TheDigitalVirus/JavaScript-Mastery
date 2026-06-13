# JavaScript Mastery

Vault de estudos para Obsidian focado em JavaScript, organizado para aprendizado progressivo com notas interligadas, tags, templates, flashcards, revisões e dashboards.

## Como usar

1. Abra esta pasta como um vault no Obsidian.
2. Comece por [[00 - Dashboard/Home|Home]].
3. Siga a ordem de [[00 - Dashboard/Roadmap|Roadmap]].
4. Use os templates em `Templates/` para criar novas aulas, exercícios, projetos e flashcards.
5. Instale os plugins recomendados em [[Recursos/Plugins Recomendados|Plugins Recomendados]].

## Estrutura

- `00 - Dashboard/`: página inicial, roadmap, progresso e glossário.
- `01 - Variáveis e Strings/`: módulo inicial seguindo a ordem das imagens fornecidas.
- `Exercícios/`: práticas guiadas por tema.
- `Projetos/`: projetos pequenos para consolidar conceitos.
- `Flashcards/`: cartões para revisão espaçada.
- `Recursos/`: links, documentação e plugins.
- `Templates/`: modelos reutilizáveis de notas.


## Validação

Antes de abrir ou atualizar um PR, rode:

```bash
python3 scripts/validate_vault.py
```

O script verifica conflitos não resolvidos no Git, conflict markers em Markdown/Canvas, JSON do Canvas, code fences, frontmatter e tags necessárias para o plugin Spaced Repetition descobrir baralhos e notas de revisão.
