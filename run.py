from flask_package import create_app, db

import click

app = create_app()


@click.group()
def cli():
    pass


@cli.command()
def run():
    app.run()


@cli.command()
def migrate():
    db.create_all()


if __name__ == '__main__':
    cli()
