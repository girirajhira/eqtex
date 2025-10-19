# eqtex

A command-line tool to generate images from LaTeX expressions. Perfect for creating high-quality mathematical notation images for scientific presentations, documentation, and educational materials.

## Features

- Convert LaTeX expressions to images via command line
- Simple and intuitive interface
- Ideal for scientific presentations and documentation

## Installation

Install eqtex using pip:

```bash
pip install eqtex
```

## Example Usage

```bash
# Generate an image from a LaTeX expression
eqtex "E = mc^2" -o equation.png

# Generate with custom resolution
eqtex "\frac{a}{b} = \sqrt{c}" -o fraction.png --dpi 300

# Inline math mode
eqtex "$\int_0^\infty e^{-x^2} dx$" -o integral.png
```

## Dependencies

This project requires the following to be installed locally:

- **pdflatex** - Part of a TeX distribution (e.g., TeX Live, MiKTeX)
- **ImageMagick** - For image conversion and processing

### Installing Dependencies

**On Ubuntu/Debian:**
```bash
sudo apt-get install texlive imagemagick
```

**On macOS (with Homebrew):**
```bash
brew install --cask mactex
brew install imagemagick
```

**On Windows:**
- Install [MiKTeX](https://miktex.org/)
- Install [ImageMagick](https://imagemagick.org/script/download.php)

## Requirements

- Python 3.6+
- pdflatex
- ImageMagick

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the project repository.