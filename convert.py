#!/usr/bin/env python

import os
import json
import yaml
import click

# class to implement a custom YAML loader
class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
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
                    # 合并YAML文件内容
                    file_data = yaml.load(f, Loader=yaml.FullLoader)
                    if isinstance(file_data, dict):
                        data.update(file_data)
                    elif isinstance(file_data, list):
                        data[filename] = file_data

        return data

Loader.add_constructor('!include', Loader.include)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('json_file', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default='-',
              help='Output file path. Defaults to stdout.')
def j2y(json_file, output):
    """Convert JSON to YAML."""
    json_data = json.load(json_file)
    yaml.dump(json_data, output, default_flow_style=False)


@cli.command()
@click.argument('yaml_file', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default='-',
              help='Output file path. Defaults to stdout.')
def y2j(yaml_file, output):
    """Convert YAML to JSON."""
    yaml_data = yaml.load(yaml_file, Loader)
    json.dump(yaml_data, output)


if __name__ == '__main__':
    cli()
