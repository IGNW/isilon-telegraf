#! /usr/bin/env python3
import click

@click.group()
def cli():
    pass

@cli.group()
def system():
    pass

@cli.group()
def nodepool():
    pass

@cli.group()
def drive():
    pass

@system.command()
def cpu():
    click.echo("display cpu stats")

@nodepool.command("percent_used")
def node_percent_used():
    click.echo("display percent drive used")

@drive.command("percent_used")
def drive_percent_used():
    click.echo("display drive percent used")

cli.add_command(system)
cli.add_command(nodepool)
cli.add_command(drive)


if __name__ == '__main__':
    cli()

