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


### Board

I want to go into a given board and start adding a list of tasks

```md:foo.board.md
<!-- ... -->
## todo

- [enhance service content](.md)
- [write post on react 19 features](.md)
- [set up selfhosted analyic solution](.md)
- [new web app](.board.md)

<!-- ... -->
```

#### Configuration concern

- the global or app level configuration should allow the user to define how they want these list to name their files. 

The above example `[enhance service content](.md) -> enhance-service-content.md`

```
[new web app](.board.md) --> new-web-app.board.md
```

#### linters

- project should lint the dirs it is watching 
- if a filename has unsupported charas it should log and warn user

## Removing and moving tasks/docs between boards

if a user removed a task from a board prompting the user before we remove the associated doc
The a doc can be orphan but still workable and can be added to another project if the user wants.

### Verbose links vs shorthand

If a markdown title is;

```
title: My amAzing project --> [My amAzing project](my-amazing-project.md)

```

if a title is;

```
title: my-amazing-project --> [my-amazing-project](.md)
```

### hanlde nested project structures 

As a user I want to be able to leverage lowpm config from any level of a project. I should be able to create docs and dirs where ever I am. 

### when In list view I want a way to related tasks


I was writing some task down in list view and I had some child task or sibiing tasks 




