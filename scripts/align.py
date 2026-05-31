from modeller import *

env = Environ()
aln = Alignment(env)

mdl = Model(env, file='4V82.cif', model_segment=('FIRST:AA', 'LAST:AA'))
aln.append_model(mdl, align_codes='4V82', atom_files='4V82.cif')

aln.append(file='target.ali', align_codes='ABV45437')
aln.align2d()
aln.write(file='alignment.pir', alignment_format='PIR')
