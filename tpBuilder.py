import os

texFileTemplate = """\\documentclass[../practica_{:02d}.tex]{{subfiles}}

\\begin{{document}}

    $ $

\\end{{document}}
"""

prTexFileTemplate = """\\documentclass{{book}}
\\usepackage{{subfiles}}
\\usepackage[margin=0.5in]{{geometry}}
\\usepackage{{physics}}
\\usepackage{{tikz}}
\\usepackage{{amssymb}}
\\usepackage{{amsmath}}
\\usepackage[makeroom]{{cancel}}
\\usepackage[spanish]{{babel}}
\\usepackage{{graphics}}
\\usepackage{{bbding}}
\\usepackage{{pifont}}
\\usepackage{{wasysym}}

\\begin{{document}}

    \\pagestyle{{plain}}

    \\begin{{enumerate}}
        {0}
    \\end{{enumerate}}

\\end{{document}}
"""

def build(path, tpNumber, quantity):
    tpFolder = os.path.join(path, 'tp')
    os.mkdir(tpFolder)
    prTexName = 'practica_{:02d}.tex'.format(tpNumber)
    texFile = open(os.path.join(tpFolder,prTexName), 'w')
    texFile.write(getPrTexName(tpNumber, quantity))
    texFile.close()

    for n in range(1, quantity + 1):
        ej = 'ej{:02d}'.format(n)
        ejFolder = os.path.join(tpFolder, ej)
        os.mkdir(ejFolder)
        newResourcesFolder = os.path.join(ejFolder, 'resources')
        os.mkdir(newResourcesFolder)
        texName = 'p{:02d}_ej{:02d}.tex'.format(tpNumber, n)
        texFile = open(os.path.join(ejFolder, texName), 'w')
        texFile.write(texFileTemplate.format(tpNumber))
        texFile.close()


def getPrTexName(tpNumber, quantity):
    text = ''
    for n in range(1, quantity + 1):
        text = text + '\n        \\item \\subfile{' + getSubfile(tpNumber, n) + '} $ $'

    return prTexFileTemplate.format(text)

def getSubfile(tpNumber, n):
    return 'ej{:02d}'.format(n) + '/' + 'p{:02d}_ej{:02d}.tex'.format(tpNumber, n)
