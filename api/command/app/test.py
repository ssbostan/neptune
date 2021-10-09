import click
from sys import exit

from api.api import app_cli, db

@app_cli.command("test", help="Testing application backing services.")
def app_cli_test():
    result = test_database_connection()
    if result is False:
        exit(1)

def test_database_connection():
    click.echo("Testing database connection... ", nl=False)
    try:
        result = db.engine.execute("SELECT 1;").first()
    except:
        click.secho("FAILED", fg="red", bold=True)
        return False
    assert result[0] == 1
    click.secho("OK", fg="green", bold=True)
    return True
