import argparse
import yaml
import sys
import importlib
import asyncio
from collections import OrderedDict
from typing import Dict

def load_commands(cli_file):
    with open(cli_file) as f:
        return yaml.safe_load(f)

def create_parser_from_yaml(command):
    parser = argparse.ArgumentParser(command['help'])
    for arg in command['args']:
        name = arg.pop('name')
        if 'required' in arg and arg.pop('required'):
            names = [name]
        else:
            names = [f"-{name}",f"--{name}"]
        if 'type' in arg:
            arg['type'] =  eval(arg['type'])
        parser.add_argument(*names, **arg)

    return parser

def general_parser(commands, description):
    print(description)
    commands = OrderedDict(sorted(commands.items()))
    for k,v in commands.items():
        print(f'{k:>10}')
        v = OrderedDict(sorted(v.items()))
        for k,v in v.items():
            print(f"{'|->':>10} {k:<15} ({v['help']})")
        print()

class yamlParser:

    def __init__(self,commands_file:str, description:str='Welcome to yamlCLI'):
        self._commands:Dict = load_commands(commands_file)
        self._description = description

    def parse(self, args):
        if len(args) == 1 or 'help' in args:
            general_parser(self._commands, self._description)
            sys.exit(0)
        command = self._commands[args[1]][args[2]]
        parser = create_parser_from_yaml(command)
        parsed_args = vars(parser.parse_args(args[3:]))

        module = importlib.import_module(command['package'])
        method = getattr(module, command['method'])
        # logger.info(f"Command received: {command['package']}.{command['method']} Arguments: {parsed_args}")
        if 'async' not in command or not command['async']:
            if command['splitArgs']:
                method(**parsed_args)
                sys.exit(0)
            method(parsed_args)
            sys.exit(0)
        asyncio.run(method(**parsed_args))