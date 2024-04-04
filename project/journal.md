I was thinking about the project last night and I realized that if a task like `foo.md` is made in a board view that will be made but their is now way to determine if it is a page, list, or board. 

```md

## TODO

- foo.md
```

So what I'm thinking is `foo.board.md` `foo.list.md` this will let the app know what type of view it is and what template to use. 

From a given board the app will use the default template at the global level or the project level... .honestly just putting ideas down here, but might be the play to, 

```
--|project
----|template
----|alpha.board.md
----|a.md
----|b.md
----|a.list.
----|sub-project
------|beta.board.md
```

?should every element be there own dir?

### TODO

- generate new board
- cli init project

## Apr 1 

So I'm running into a odd issue. I am working on the configs and I don't know if I want to have something like this 

```yml
frontmatter:
  title: "foo"
  description: ""
  date_created: '04/02/2024'
  last_modified: '2024/03/31'
  status: "" # backlog, todo, doing, done, archive 
```

```yml
board:
  frontmatter:
    title: "foo"
    description: ""
    date_created: '04/02/2024'
    last_modified: '2024/03/31'
page:
  frontmatter:
    title: "foo"
    description: ""
    date_created: '04/02/2024'
    last_modified: '2024/03/31'
    status: "" # backlog, todo, doing, done, archive 
```

```yml

```

....
I think I should do global > board/page/list > custom template and have each override and or extend

> should we make the template naming convention configureable. 
>

Right now it is `template.board.md` `template.pgae.md` `template.list.md`

## floating tasks

Should we allow orphan pages...pages that are not attached to a given board or list? 

This would mean that when we created a page, a parent board would be required. 

This would also mean that when we init the app project name would have to be created with a starter board. 

## Watching for changes 

ok starting the watch functionality. Setting up a dir watcher was very easy. Thank you python. Now I need to think about how I want to watch for changes. 

I'm thinking, start with page changes...or board changes...idk.

### Stories 

A user adds a page to a board. The board column should update with the page backlink as a list item and be added to the column that matches status. 

- If status is empty, the board adds a column for empty?
- Or strict, through and error that status has to match. 
- default status is required?

### naming and uniqueness issues

An issue I can forsee is in regards to uniqueness. 

Suppose, we have a board named foo.board.md, if foo is added to the associated boards array in a page the boar will then have the page added to the defined column. 

Board names should be unique under projects, no spaces, no uppercase. 

?let the user define the naming rules?

### question: Freedom 

I want to allow the users to manually make markdown files in all the ways someone might. But this increases the risk of user error, the type that comes to mind is missing front matter fields. Their are a few ways to handle this. 

- add a watcher checker that lints frontmatter for required fields, "boards", "status", "date_created", "last_modified", "title"


#### question: User feild remap custom naming of required fields?

Should we let the user remap the frontmatter fields to their own naming?

## allow ophan pages or not? 

Should all the pages be attached to a board? Then I would want to have a default board in the config as well as be able to pass --board name to the cli new method


## Project path 

I want to support both absolute paths and relative path from where the app is initialized

## Gotchas 

The doc title must match the file prefix label,

**example**
title: foo --> foo.md or foo.board.md or foo.list.md

**Example**
title: The Lazy Lizard --> the-lazy-lizard.md or the-lazy-lizard.board.md

### Feature: handle whitespace and capitals in doc titles 

or have the title and another properties that matches the file name

### Descriptions in Board view

it would be nice if there was a way to have descriptions in the board view. Maybe something like this. 

- [some task](.md)::"some task description"

## Changing Doc names

The issue is that if a doc name changes in either the doc or the board there is no way to know which doc has been changed because their is no tracker or mapper. No look up. We might need to have a little sqlite db to handle this. 