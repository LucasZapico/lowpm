# Installation 

## Python 


## Getting Started

```sh
git clone git@github.com:LucasZapico/lowpm.git
```

### Make Available in Shell 

The binary is `python/dist/main`, adding the path to this to your shell path will make is available to the CLI.

Add it manually by editing your `~/.bashrc` or `~/.zshrc` file... whatever shell your using. 

```sh 
echo 'alias adcvart='/path/to/dist/main'` >> ~/.bashrc
```

```sh 
echo "alias adcvart='/path/to/dist/main'" >> ~/.zshrc
```

## Principles

>lowpm is meant to be useable at the global level and completely >functional in single projects. 

Global configs are overridden by project level configs and nested projects will be overridden by the lowest `.lowpm/`

### Init Globally 

This creates a `~/.lowpm/` in your user root this is where global configs `~/.lowpm/lowpm.config.yaml` lives and global templates. `~/.lowpm/templates/`

```sh
lowpm init -g 
```

### Init Project 

In a project dir run `lowpm init`

- this will check

```sh
lowpm init
```

|flags| description| type |
|---| ----|
|-g | inits a global config and templates|  none |
| --config or -c |  if the config flag is passed `.lowpm` will be added to your project dir with `.lowpm/lowpm.config.yaml` and `.lowpm/templates` |


## Development 

Use `pipenv`

```sh
brew install pipenv
```

Let `pipenv` handle the load and start a virtual env
```sh
pipenv shell
```

Install whatever packages are needed to extend the project

```sh
pipenv install <package>
```


## Reference 

[stock adobe leather book](https://stock.adobe.com/images/old-leather-background-with-golden-floral-decoration/22198364)


