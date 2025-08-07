import typer
import os
import json
from dotenv import load_dotenv
from mongo_crud_tool import MongoCRUD

load_dotenv()

app = typer.Typer()
crud = MongoCRUD(os.getenv("DB_NAME"))

@app.command()
def ai(natural: str):
    from ai_agent import handle_user_input
    result = handle_user_input(natural)

    if isinstance(result, list):
        for item in result:
            typer.echo(item)
    else:
        typer.echo(result)

@app.command()
def create(collection: str, data: str):
    """Create a new document. Pass JSON string as data."""
    doc = json.loads(data)
    doc_id = crud.create(collection, doc)
    typer.echo(f"Inserted with ID: {doc_id}")

import pprint
pp = pprint.PrettyPrinter(indent=2)

@app.command()
def read(collection: str, query: str = "{}"):
    """Read documents from collection. Pass JSON query string."""
    results = crud.read(collection, json.loads(query))
    for r in results:
        typer.echo(pp.pformat(r))

@app.command()
def update(collection: str, query: str, new_values: str):
    """Update documents."""
    count = crud.update(collection, json.loads(query), json.loads(new_values))
    typer.echo(f"Updated {count} document(s)")

@app.command()
def delete(collection: str, query: str):
    """Delete documents."""
    count = crud.delete(collection, json.loads(query))
    typer.echo(f"Deleted {count} document(s)")

@app.command()
def create(collection: str, data: str):
    """Create a new document. Pass JSON string as data."""
    try:
        doc = json.loads(data)
        doc_id = crud.create(collection, doc)
        typer.echo(f"Inserted with ID: {doc_id}")
    except json.JSONDecodeError:
        typer.echo("Invalid JSON data passed.")


if __name__ == "__main__":
    app()
