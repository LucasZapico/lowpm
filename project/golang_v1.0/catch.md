a page, board, or list can be defined from the cli, or created by using markdown link syntax [new page](./path/to/new-page.md)


## Overview 

Lowpm short for "Low level Project Management" is meant is born from the idea that we as user should be able to see and control our data and relationships rules that data adheres to. 

## Who Can Enjoy Lowpm 

- Developers 
- Authors
- Business Developers 
- Tinkers 
- Anyone who manages projects of suficient complexity 

### Philosophy 

A project can be well managed with a few core methods for viewing and managing information. 

- **board**
- **list** 
- **page**

Document can be created from the cli, in line with lowpm syntax (extended frontmatter), or by creating a file form the file manager, text editor or terminal. 

> Document created in the file manager, text editor, or terminal will not be "watched" without the expected frontmatter. 

### Recommended Workflow 

- init lowpm in some project 
- create epics, projects, tasks, 
- use the frontmatter to relate document

In a project run `lowpm init` this will create a `.lowpm` in the project root where a config can be tailored to the project. 


## Board 

The board is kanban board. That can be customized from the board template. 

## Config 

lowpm can be defined at the user root with `.lowpm` or in a project directory with `.lowpm` the the lower configs take priority over higher configs. 

```
user-root/
├─ .lowpm/
├─ development/
│  ├─ project-alpha/
|  |  |-- .lowpm/ <-- config will override user root
│  ├─ project-beta/
|  |  |-- .lowpm/ <-- config will override user root
|  |  ├─ project-gamma/
|  |  |─- .lowpm/ <-- config will override config in `project-beta`

```

### Config Structure 

```
.lowpm/
|-- templates/
|   |-- template.frontmatter.y[a]ml
|   |-- template.board.md
|   |-- template.page.md
|   |-- template.list.md
|-- lowpm.config.y[a]ml
```

### Config Templates 

The config templates define what a document (`board`, `list`, `page`) looks like when defined from the `new` command in the the cli

```
lowpm new board --title "Contact form for project alpha" --path ./features
```

If path defines the document as well the document will have the path defined title, and `title` will be use in the frontmatter title only. 

```
lowpm new board --title "Contact form for project alpha" --path ./features
```

This 👆 command results in 

```
project-alpha
|   |--.lowpm/
|   |--features/
|   |   |contact-form-for-project-alpha.board.md
```

> Document with out the expected front matter are ignored by lowpm.

## Behavior 

Document names can be defined, by creating the document in the file system, or from the cli, or by defining a document in a board, page, or list document in a lowpm managment project. 

### Document Name Cohersion Behavior 

#### Cli 

```
lowpm new board --title "dark mode toggle" 
```

This will result in `dark-mode-toggle.board.md` in the directory where the command was executed. If lowpm was init at the user level it will create the doc in the given directory regardless. This is not recommended. 



```
project-alpha
|   |--.lowpm/
|   |--features/
|   |   |contact-form-for-project-alpha.board.md
```


Document names are pulled from titles, 

- [] address special characters

#### Defaults 



title definitions are cohersed to `lowercase` and 

# Template Syntax 

## Paths

### Simple Examples

> if title is not followed by `*.page.md`, `*.board.md`, `*.list.md` the document is assumed to be a page.

`[foo page](/absolute/path/form/project/root/foo.page.md)`


`[bar list](./relative/path/from/link/bar.list.md)`



## Page

`<page title>.md` 

`<page title>.page.md`



## Board 


## List 

`<list title>.list.md`




