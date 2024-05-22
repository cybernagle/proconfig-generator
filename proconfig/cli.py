#!/usr/bin/env python3

import os
import sys
import json
import yaml
import click

import jsonschema
from jsonschema import validate
from tabulate import tabulate
from termcolor import colored

from . import MAIN_YAML_CONTENT, HOME_PAGE_STATE_CONTENT, QUESTIONS_JSON_CONTENT, LEVEL1_JS_CONTENT
from . import schema

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
                    elif isinstance(file_data, list):
                        data[filename] = file_data
        return data


    def oneline(self, node):
        file_path = self.construct_scalar(node)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        with open(file_path, 'r') as f:
            return f.read()#.replace('\\n', '\n')


    def print_table(self, data):
        headers_upper = [header.upper() for header in self._headers]
        colalign = ["right"] * len(headers_upper)
        print(tabulate(data, headers=headers_upper, tablefmt='plain', colalign=colalign),file=sys.stderr)

Loader.add_constructor('!include', Loader.include)
Loader.add_constructor('!oneline', Loader.oneline)

def visualize(states):
    headers = ['state', 'inputs', 'outputs', 'transitions', 'render', 'tasks']
    data = []
    for state_name in list(states.keys()):
        single_state = []
        state_data = states[state_name]

        for header in headers:
            if header in state_data:
                single_state.append(colored('Yes', 'green'))
            elif header == "state":
                single_state.append(colored(state_name, 'yellow'))
            else:
                single_state.append(colored('No', 'red'))
        data += [single_state]

    headers_upper = [header.upper() for header in headers]
    colalign = ["right"] * len(headers_upper)
    print(tabulate(data, headers=headers_upper, tablefmt='plain', colalign=colalign),file=sys.stderr)

def load_file(file_path):
    _, file_extension = os.path.splitext(file_path)

    try:
        if file_extension.lower() == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_extension.lower() in ['.yaml', '.yml']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.load(f, Loader)
        else:
            raise click.UsageError(f"Unsupported file extension: {file_extension}")

    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise click.UsageError(f"Invalid file format: {e}")

def validate_proconfig(json_data):
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.ValidationError as e:
        error_message = (
            f"Validation error: {e.message}\n"
            f"Path to error: {list(e.path)}\n"
            f"Schema path: {list(e.schema_path)}"
        )
        raise click.UsageError(f"Invalid JSON content: {error_message}")
    print("DATA validation successful: The provided ProConfig Code is valid.")
    if 'states' in json_data:
        visualize(json_data['states'])

def create_project_structure():
    """Initialize the project structure."""
    current_dir = os.getcwd()

    if (os.path.exists(os.path.join(current_dir, 'main.yaml')) or
        os.path.exists(os.path.join(current_dir, 'state')) or
        os.path.exists(os.path.join(current_dir, 'code'))):
        click.echo("Project has already been initialized. No changes made.")
        return

    # Create main.yaml
    with open(os.path.join(current_dir, 'main.yaml'), 'w') as f:
        f.write(MAIN_YAML_CONTENT)

    # Create state directory and home_page_state.yaml
    os.makedirs(os.path.join(current_dir, 'state'), exist_ok=True)
    with open(os.path.join(current_dir, 'state', 'home_page_state.yaml'), 'w') as f:
        f.write(HOME_PAGE_STATE_CONTENT)

    # Create code directory and files
    os.makedirs(os.path.join(current_dir, 'code'), exist_ok=True)
    with open(os.path.join(current_dir, 'code', 'questions.json'), 'w') as f:
        f.write(QUESTIONS_JSON_CONTENT)
    with open(os.path.join(current_dir, 'code', 'level1.js'), 'w') as f:
        f.write(LEVEL1_JS_CONTENT)

    click.echo("Project structure initialized successfully.")

from .__version__ import __version__


@click.group(invoke_without_command=True)
@click.version_option(__version__, '-v', '--version', message='%(version)s')
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@cli.command()
@click.argument('json_file', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default='output.yaml',
              help='Output file path. Defaults to output.yaml.')
def decode(json_file, output):
    """Convert JSON to YAML."""
    json_data = load_file(json_file.name)
    yaml.dump(json_data, output, default_flow_style=False)

    validate_proconfig(json_data)

@cli.command()
@click.argument('yaml_file', type=click.File('r'), default='main.yaml')
@click.option('--output', '-o', type=click.File('w'), default='output.json',
              help='Output file path. Defaults to output.json.')
def encode(yaml_file, output):
    """Convert YAML to JSON."""
    yaml_data = load_file(yaml_file.name)
    json.dump(yaml_data, output)

    validate_proconfig(yaml_data)

@cli.command()
@click.argument('yaml_file', type=click.File('r'))
def check(yaml_file):
    """Check the state for missing part."""
    yaml_data = load_file(yaml_file.name)
    validate_proconfig(yaml_data)

@cli.command()
def init():
    """Init a whole simple project."""
    create_project_structure()

if __name__ == '__main__':
    cli()
