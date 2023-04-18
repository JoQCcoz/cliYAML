from cliyaml.cliyaml import yamlParser

import sys
from pathlib import Path

def add(x, y):
    print(x+y)

if __name__ == "__main__":
    parser = yamlParser(Path(__file__).parent /'commands.yaml', description='My New App CLI tools')
    parser.parse(sys.argv)