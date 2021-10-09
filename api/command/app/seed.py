import click
from sys import exit

from api.api import app_cli, db
from api.model import Country

@app_cli.command("seed", help="Seeding some data to database.")
def app_cli_seed():
    click.echo("Seeding data... ", nl=False)
    country1 = Country(code="IRN", name="iran", capital="tehran", longitude=51.25, latitude=35.41)
    country2 = Country(code="GBR", name="united kingdom", capital="london", longitude=0.07, latitude=51.30)
    db.session.add(country1)
    db.session.add(country2)
    try:
        db.session.commit()
        click.secho("OK", fg="green", bold=True)
    except:
        db.session.rollback()
        click.secho("FAILED", fg="red", bold=True)
        exit(1)
