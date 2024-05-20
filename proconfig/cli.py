#!/usr/bin/env python3

import os
import sys
import json
import yaml
import click

from tabulate import tabulate
from termcolor import colored

# class to implement a custom YAML loader
class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        self._headers = ['state', 'inputs', 'outputs', 'transitions', 'render', 'tasks']
        self._state = []
        super(Loader, self).__init__(stream)

    def include(self, node):
        directory_path = self.construct_scalar(node)
        base_path = os.path.dirname(self.name)
        full_directory_path = os.path.join(base_path, directory_path)

        # 读取文件夹中所有的YAML文件
        data = {}
        for filename in os.listdir(full_directory_path):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                file_path = os.path.join(full_directory_path, filename)
                with open(file_path, 'r') as f:
                    # 合并yaml文件内容
                    file_data = yaml.load(f, Loader=yaml.FullLoader)
                    if isinstance(file_data, dict) and file_data:
                        data.update(file_data)
                        self.handle_stage(file_data)
                    elif isinstance(file_data, list):
                        data[filename] = file_data
        return data

    def handle_stage(self, stages):
        for state_name in list(stages.keys()):
            state = stages[state_name]
            self.update_fields(state_name ,state)

    def oneline(self, node):
        file_path = self.construct_scalar(node)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        # 如果是 YAML 文件，合并内容
        with open(file_path, 'r') as f:
            return f.read()#.replace('\\n', '\n')

    def update_fields(self, state_name ,state_data):
        single_state = []
        for header in self._headers:
            if header in state_data:
                single_state.append(colored('Yes', 'green'))
            elif header == "state":
                single_state.append(colored(state_name, 'yellow'))
            else:
                single_state.append(colored('No', 'red'))

        self._state += [single_state]

    def print_table(self, data):
        headers_upper = [header.upper() for header in self._headers]
        colalign = ["right"] * len(headers_upper)
        print(tabulate(data, headers=headers_upper, tablefmt='plain', colalign=colalign))

    def __del__(self):
        if self._state:
            self.print_table(self._state)

Loader.add_constructor('!include', Loader.include)
Loader.add_constructor('!oneline', Loader.oneline)

def create_project_structure():
    current_dir = os.getcwd()

    project_structure = {
        "main.yaml": "# Initial main.yaml content\n",
        "state": {
            "example_state.yaml": "# Example state content\n"
        },
        "code": {
            "example_code.py": "# Example code content\n"
        }
    }

    for name, content in project_structure.items():
        if isinstance(content, dict):
            dir_path = os.path.join(current_dir, name)
            os.makedirs(dir_path, exist_ok=True)
            for sub_name, sub_content in content.items():
                sub_path = os.path.join(dir_path, sub_name)
                with open(sub_path, 'w') as f:
                    f.write(sub_content)
        else:
            file_path = os.path.join(current_dir, name)
            with open(file_path, 'w') as f:
                f.write(content)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('json_file', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default='-',
              help='Output file path. Defaults to stdout.')
def decode(json_file, output):
    """Convert JSON to YAML."""
    try:
        json_data = json.load(json_file)
    except json.JSONDecodeError:
        raise click.UsageError(f"Invalid JSON format in file: {json_file.name}")

    yaml.dump(json_data, output, default_flow_style=False)


@cli.command()
@click.argument('yaml_file', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default='-',
              help='Output file path. Defaults to stdout.')
def encode(yaml_file, output):
    """Convert YAML to JSON."""
    try:
        yaml_data = yaml.load(yaml_file, Loader)
    except yaml.YAMLError:
        raise click.UsageError(f"Invalid YAML format in file: {yaml_file.name}")

    json.dump(yaml_data, output)

@cli.command()
@click.argument('yaml_file', type=click.File('r'))
def check(yaml_file):
    try:
        yaml_data = yaml.load(yaml_file, Loader)
    except yaml.YAMLError:
        raise click.UsageError(f"Invalid YAML format in file: {yaml_file.name}")

@cli.command()
def init():
    create_project_structure()

if __name__ == '__main__':
    cli()
