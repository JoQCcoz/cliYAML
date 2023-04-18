# cliYAML

Create easy CLI from YAML. It will automatically construct a parser, read the arguments and launch the specified function from the specified module.

## Install

```shell-session
pip install git+https://github.com/JoQCcoz/cliYAML.git
```

## Usage

Simply import the yamlParser class, specify the yaml file containing the commands and a short description to head the help menu.

```python
from cliyaml.cliyaml import yamlParser

import sys
from pathlib import Path

def add(x, y):
    print(x+y)

if __name__ == "__main__":
    parser = yamlParser(commands_file:str|Path=Path(__file__).parent /'commands.yaml',description='My New App CLI tools')
    parser.parse(sys.argv)
```

Set up your commands in the YAML file
```yaml
commandSet1:
  add:
    help: This is what command1 does
    package: cliyaml.example.example
    method: add
    splitArgs: True
    args:
      - name: "x"
        help: This is the first argument
        type: int
        default: 'value'
      - name: "y"
        help: This is the another argument
        type: int
  command2:
    help: This is what command2 does
    args:
      - name: arg1
        help: This is the first argument
        type: str
        default: 'value'
      - name: arg2
        help: This is the another argument
        type: str
        nargs: +
commandSet2:
  command1:
    help: This is what command1 does
    args:
      - name: arg1
        help: This is the first argument
        type: str
        default: 'value'
      - name: arg2
        help: This is the another argument
        type: str
        nargs: +
```

Run the script:

```shell-session
python example/example.py

My New App CLI tools
commandSet1
       |-> add             (This is what command1 does)
       |-> command2        (This is what command2 does)

commandSet2
       |-> command1        (This is what command1 does)
```

To bring the help of a specific command:

```shell-session
python example/example.py commandSet1 add -h

usage: This is what command1 does [-h] [-x X] [-y Y]

options:
  -h, --help   show this help message and exit
  -x X, --x X  This is the first argument
  -y Y, --y Y  This is the another argument
```

Call a specific command:

```shell-session
python example/example.py commandSet1 add -x 3 -y 4
7
```

