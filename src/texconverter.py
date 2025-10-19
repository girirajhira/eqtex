

# Import the defaul template
with open('defaults/default_preamble.tex') as file:
    default_latex_template =  file.read()


def generate_pdf_from_tex(expression, outfile, tempfolder = False, usepackages=None,
             preamble=None, colour = None, cur_dir=None):
    '''
    :param expression: Latex expression to be rendered (string)
    :param outfile: location of output file (string)
    :param tempfolder: whether a temperorary folder should be made (bool)
    :param usepackages
    :param preamble:
    :param colour:
    :return:
    '''
    with open(outfile, 'w') as file:
        file.write(default_latex_template)
        if usepackages is not None:
            for pack in usepackages:
                file.write(r"\usepackage{" + pack +"}")
        if preamble is not None:
            file.write(preamble + " \n")
        if colour is not None:
            if isinstance(colour, list) or isinstance(colour, (np.ndarray, np.generic)):
                file.write(r"\usepackage{xcolor}")
                file.write(r"\definecolor{custcolour}{RGB}{" + f'{colour[0]}, {colour[1]}, {colour[2]}' + r"}" )
                expression = (r"\textcolor{custcolour}{" + expression + r"}")
            else:
                file.write(r"\usepackage{xcolor}")
                expression = (r"\textcolor{" + colour + "}{" + expression + r"}")

        file.write(r"\begin{document}")
        file.write(expression)
        file.write(r"\end{document}")

    # Compiling
    if tempfolder:
        command = f"pdflatex -output-format=pdf -interaction=batchmode -output-directory=tempfolder {outfile}"
    else:
        command = f"latex {outfile}"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return None


def dvi_to_svg(infile, outfile):
    command = f'pdf2svg {infile} {outfile}'
    # --verbosity = 0
    os.system(command)


def create_image_from_tex(expression: str, filename: str):
    generate_pdf_from_tex(expression, filename)
    
    if filename.endswith('.png'):
        pass 
    elif filename.endswith('.svg'):
        pass 

    elif filename.endswith('.pdf'):
        pass 
    # elif filename == '':
    #     filename = (expression.replace(" ", "")).replace(r"\", "")
    # pass







