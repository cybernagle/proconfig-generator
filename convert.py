#!/usr/bin/env python

import json
import yaml
import click

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
    yaml_data = yaml.safe_load(yaml_file)
    json.dump(yaml_data, output)


if __name__ == '__main__':
    cli()
