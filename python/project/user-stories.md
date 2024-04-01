## Init project - story

## feat:story - make new task

When I make a new item in a board I want the element to be created automagiclly.

**before**
```txt
--| project
  --|templates
    --| template.md
    --| template.board.md
    --| template.list.md
  --|a.board.md
```

```md:a.board.md
//....
## TODO

- foo.md

//...
```
**after**
```txt
--| project
  --|templates
    --| template.md
    --| template.board.md
    --| template.list.md
  --|a.board.md
  --|foo.md
```

`foo.md` is created from the template `template.md`