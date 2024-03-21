import argparse
from pathlib import Path
import os



parser = argparse.ArgumentParser()

parser.add_argument('path')

args = parser.parse_args()

path = 'obj/' + str(args.path)

mtlpath = path.rsplit('.', 1)[0] + '.mtl'

if Path(mtlpath).exists(): os.remove(mtlpath)

if not Path(path).exists(): print(f'file "{path}" does\'t exist!'); raise SystemExit()


with open(path, 'rt') as objin: objfile = objin.read().split('\n')

out = ''

jump = False
for l in objfile:
    if l.startswith('usemtl ') and not jump: jump = True

    if l.startswith('o ') and jump: jump = False
    if jump: continue
    out += l + '\n'


with open(path, 'wt') as objout: objout.write(out.strip())