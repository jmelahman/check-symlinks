# Check Symlinks

Checks for broken symbolic links.

This script is optimized for large codebases as well as small, incremental checks.

Speed comparisons:

1,000 symlinks, 50,000 files.

```
$ fd --type symlink --exec sh -c 'test -e "$0" || echo "$0"'

real    0m0.334s

$ time check-symlinks

real    0m0.371s

$ git ls-files | xargs pre-commit/pre_commit_hooks/check_symlinks.py

real    0m1.008s

$ while read file; do test -e "$test"; done < <(git ls-files)

real    0m1.461s

$ find . -type l -not -path data ! -exec test -e {} \; -print0 | xargs --no-run-if-empty git ls-files

real    0m1.492s
```

## Install

```shell
cargo install check-symlinks
```

## Usage

By default, checks all [unignored](https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore#ignore) files recursively from the current working directory,

```shell
$ check-symlinks
"./broken_link" is not a valid symlink
```

File paths can also be passed,

```shell
$ check-symlinks broken_link doesnt_exist
"./broken_link" is not a valid symlink
```

_NOTE: file arguments which don't exist are ignored._
