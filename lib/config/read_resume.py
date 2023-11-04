from pylatexenc.latex2text import LatexNodes2Text


def read_resume():
    with open('resume.tex', 'r') as f:
        resume = f.read()
    return LatexNodes2Text().latex_to_text(resume)
