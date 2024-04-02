# GNU TeXmacs plugins implemented in Python
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Real world plugins:
+ [python](plugins/python)
+ [graphviz](plugins/graphviz)
+ [sympy](plugins/sympy)

Demo plugins:
+ `pyminimal`: minimal demo plugin
+ `pycomplete`: demo plugin for completion
+ `pymarkup`: demo plugin for GNU TeXmacs markup
+ `pyprompt`: demo plugin for changing the session prompt

## Cheatsheat
``` bash
pants run cli:install -- pyminimal
pants run cli:install -- pyminimal win

bin/lint

bin/format

# For other GNU TeXmacs distributions like Mogan Research
# you can make a symbol link

# macOS
ln -s $HOME/.TeXmacs/plugins $HOME/Library/Application\ Support/XmacsLabs/
# Linux
ln -s $HOME/.TeXmacs/plugins $HOME/.local/share/XmacsLabs/
```
## Contributing
Please report bugs to the GNU TeXmacs [forum](http://forum.texmacs.cn/c/devel/pluginsinpython) for this project.

Issues are managed inside this repo (eg. [docs/issues.tm](docs/issues.tm), [docs/001.tm](docs/001.tm), [docs/002.tm](docs/002.tm)). Please create pull requests to create issues!

Pull requests can be made against:
+ [Github](https://github.com/texmacs/plugins-in-python/pulls)
+ [Gitee](https://gitee.com/texmacs/plugins-in-python/pulls)
+ More to come ...

