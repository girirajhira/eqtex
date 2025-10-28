import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path
from eqtex.texconverter import create_image_from_tex

app = typer.Typer(
    name="eqtex",
    help="Generate images from LaTeX expressions",
    add_completion=False
)
console = Console()

@app.command()
def convert(
    expr: str = typer.Argument(
        ...,
        help="LaTeX expression to convert (e.g., 'E = mc^2' or r'\\int_0^\\infty e^{-x^2} dx')"
    ),
    output: str = typer.Option(
        "output.png",
        "--output", "-o",
        help="Output filename for the generated image"
    ),
    dpi: int = typer.Option(
        300,
        "--dpi", "-d",
        help="Resolution in DPI (dots per inch)"
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose", "-v",
        help="Show detailed output"
    )
):
    """
    Convert a LaTeX expression to an image.
    
    Example:
        eqtex "E = mc^2" -o equation.png
        eqtex "\\frac{a}{b}" -o fraction.png --dpi 600
    """
    try:
        if verbose:
            console.print(f"[cyan]Converting LaTeX expression...[/cyan]")
            console.print(f"[dim]Expression:[/dim] {expr}")
            console.print(f"[dim]Output:[/dim] {output}")
            console.print(f"[dim]DPI:[/dim] {dpi}")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            if not verbose:
                progress.add_task(description="Generating image...", total=None)
            
            create_image_from_tex(expr, output, dpi=dpi)
        
        console.print(f"[green]✓[/green] Successfully created: [bold]{output}[/bold]")
        
    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] Required dependency not found: {e}", style="bold red")
        console.print("\n[yellow]Please ensure pdflatex and ImageMagick are installed.[/yellow]")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", style="bold red")
        if verbose:
            console.print_exception()
        raise typer.Exit(code=1)

@app.command()
def version():
    """Show the version of eqtex."""
    console.print("[cyan]eqtex[/cyan] version [bold]0.1.0[/bold]")

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        help="Show version and exit"
    )
):
    """
    eqtex - Generate images from LaTeX expressions
    """
    if version:
        console.print("[cyan]eqtex[/cyan] version [bold]0.1.0[/bold]")
        raise typer.Exit()
    
    if ctx.invoked_subcommand is None:
        console.print("[yellow]No command specified. Use --help for usage information.[/yellow]")

if __name__ == "__main__":
    app()

# Example usage (for testing):
# convert(r'\[ \int \frac{f(z)}{z-z_0} dz = 2\pi i f(z_0) \]', 'cauchy.png')