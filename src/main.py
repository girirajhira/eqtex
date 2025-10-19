import typer 
import rich 
from texconverter import create_image_from_tex


app = typer.Typer()


@app.command()
def convert(expr:str):
    pass
    



if __name__ == "__main__":
    app()