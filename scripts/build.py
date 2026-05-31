from modeller import *
from modeller.automodel import *

env = Environ()
# Tell MODELLER to look in the data folder for the .cif file
env.io.atom_files_directory = ['.', './data']
# Force MODELLER to read the terbutryn ligand
env.io.hetatm = True

# Updated path to point to the data folder
a = AutoModel(env, alnfile='data/alignment.pir',
              knowns='4V82', sequence='ABV45437',
              assess_methods=(assess.DOPE, assess.GA341))

a.starting_model = 1
a.ending_model = 5
a.make()
