## Project 



## Init - Out of the box 

- templates/
  - board/index.md
  - list/index.md
  - page/index.md
  - table/index.md

## structure 

The app will init a set of default templates that can be edited within the expected config.

# Markdown Todo 

The idea behind this project is to make a low level todo/project manager 

## Core

- init
- watch or run manually

### CLI action 

### File system 

### Template 

set templates 

### App 

- web
- electron 
- mobile 
  - ios
  - android
  
### Accessible api

## Challenges and function 

- how do we handle showing related tasks and dependent tasks
- how do we handle task and projects that can appear on multiple projects, epics, etc

## Stories and Use Cases 

Be able to directly edit files in a human readable format. Edit and add task, projects, epcs from the text editor or file system. 


## References 

[zettelcon - backlink](https://github.com/whateverforever/zettelcon)
[python frontmatter - waylonwalker.com](https://waylonwalker.com/python-frontmatter/)
[python frontmatter docs](https://python-frontmatter.readthedocs.io/en/latest/)
[working with frontmatter in python - raymondcamden.com](https://www.raymondcamden.com/2022/01/06/working-with-frontmatter-in-python)
 

### Features 

- cli init new (board, list, page) from template 
- in a board doc, create new-todo.md this creates a new page from template page

----

### Templates 

The default template is the first template of a type found in templates. 

If `low-project` is a global package templates are looked for at the global config path. Templates at the project level override templates at the global level. 

#### Specific templates 

Can be defined by; 

```sh 
lowpm --template <path/to/template> <file-name>
```

```sh 
lowpm -t <path/to/template> <file-name>
```

**Example**

```sh 
lowpm --template ./templates/template-board.v2.0.md --name project-foo.md
```

```sh 
lowpm --template ./templates/template-board.v2.0.md --n project-foo.md
```

### Challenges 

? should templates dir be flat `template-board.md` `template-page.md` or nested `board/template-1.md` `page/template.1.md`?



?should list be csv? I feel like they should but, this requires some different thinking.

### Idea - Feature

It would be nice to some how config the board column, which then populated, status, in page and list