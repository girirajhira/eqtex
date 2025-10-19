import typer 
import rich 
from src.texconverter import create_image_from_tex


app = typer.Typer()


# @app.command()
def convert(expr:str, filename:str):
    create_image_from_tex(expr, filename)


if __name__ == "__main__":
    app()


# convert(r'\[ \int \frac{f(z)}{z-z_0} dz = 2\pi i f(z_0) \]', 'cauchy.png')
