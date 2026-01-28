from typing import Annotated
import typer

from .models import run_migrations
from .models import add_log
from .models import list_logs

app = typer.Typer()


@app.command()
def add(
    date: Annotated[str, typer.Option("--d", prompt="Date (YYYY-MM-DD)")],
    time_in: Annotated[str, typer.Option("--in", prompt="Time in (HH:MM)")],
    time_out: Annotated[str, typer.Option("--out", prompt="Time out (HH:MM)")],
    remarks: Annotated[str, typer.Option("--r", prompt="Remarks")],
):
    add_log(date, time_in, time_out, remarks)
    typer.echo("✅ OJT log added successfully.")
    typer.echo("➡️  Check progress with `ojt summary`.")


@app.command()
def list():
    logs = list_logs()

    typer.echo(
        f"{'ID':<4} {'Date':<12} {'Time In':<10} {'Time Out':<10} {'Total Hours':<15} {'Remarks':<20}"
    )
    typer.echo("-" * 80)

    for log in logs:
        typer.echo(
            f"{log[0]:<4} {log[1]:<12} {log[2]:<10} {log[3]:<10} {log[5]:<15} {log[4]:<20}"
        )


@app.command()
def migrate():
    run_migrations()
    typer.echo("✅ Database migrations completed successfully.")
    typer.echo("➡️  You can now start logging with `ojt add`.")


if __name__ == "__main__":
    app()
