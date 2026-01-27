from typing import Annotated
import typer

from .models import run_migrations

app = typer.Typer()


@app.command()
def add(
    date: Annotated[str, typer.Option("--d", prompt="Date (YYYY-MM-DD)")],
    time_in_str: Annotated[str, typer.Option("--in", prompt="Time in (HH:MM)")],
    time_out_str: Annotated[str, typer.Option("--out", prompt="Time out (HH:MM)")],
    remarks: Annotated[str, typer.Option("--r", prompt="Remarks")],
):
    print(f"Date: {date}")
    print(f"Time in: {time_in_str}")
    print(f"Time out: {time_out_str}")
    print(f"Remarks: {remarks}")


@app.command()
def migrate():
    run_migrations()
    typer.echo("Migrations done successfully!")


if __name__ == "__main__":
    app()
