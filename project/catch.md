## Project 

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

? should templates dir be flat `templat-board.md` `template-page.md` or nested `board/template-1.md` `page/template.1.md`?