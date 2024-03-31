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

