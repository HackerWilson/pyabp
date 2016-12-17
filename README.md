# pyabp
[API Blueprint](https://apiblueprint.org/) from python docstring.

# Getting started
```
pip install pyabp
```

# Usage
```
usage: pyabp [-h] [-w [NAME [NAME ...]]] [--host HOST]

API Blueprint from python docstring.

optional arguments:
  -h, --help            show this help message and exit
  -w [NAME [NAME ...]], --write [NAME [NAME ...]]
                        Write out the API Blueprint documentation for a module
                        to a file in the current directory. If <name> contains
                        a '/', it is treated as a filename; if it names a
                        directory, documentation is written for all the
                        contents.
  --host HOST           Your host server address.
```

# Examples
```
pyabp -w /path/to/pyabp/examples/ --host https://polls.apiblueprint.org/
```

# Resources
[API Blueprint Tutorial](https://apiblueprint.org/documentation/tutorial.html)

# License
[MIT License](LICENSE)
