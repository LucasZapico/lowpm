
## Syntax 

- title
- description 
- date_created
- last_modified
- tags
- categories 

### List frontmatter 

This list syntax our fundamental building block of this project. The behavior here is consistant throughout all recognized docs, boards, lists, pages, 

#### This is a task 

This is our base element 

```md
- Feed the cat 
```

#### This is will become a page 

```md
- [feed the cat](.md)
```

```md 
--|project 
----|feed-the-cat.md
```

This is a page with a custom filename 

```md
- [feed the cat](pet-stuff.md)
```

```md 
--|project 
----|pet-stuff.md
```

### This is a page with frontmatter in a list 


```md 
- [feed the cat](chores/pet-stuff.md)
  - description: The stuff my animals need to be happy and healthy
  - tags: ["pets", "chore", "todo"]
  - note: I'm some more stuff that will be appened to the body of the doc
```

```md 
--|project 
----|chores
------|pet-stuff.md
```

```md:pet-stuff.md
---
title: feed the cat
description: The stuff my animals need to be happy and healthy
tags: ["pets", "chore", "todo"]
---

I'm some more stuff that will be appened to the body of the doc
```





### List 


