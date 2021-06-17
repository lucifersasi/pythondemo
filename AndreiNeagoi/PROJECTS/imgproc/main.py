import sys
import os
import matplotlib
from PIL import Image

# grab 1st and second argument
source = sys.argv[1]
# print(source)
dest = sys.argv[2]
# print(dest)

# with open(source, 'r') as f:
#     data = f.read()


# check is new/exists, if not create
# if not os.path.exists(dest):
#     os.makedirs(dest)

# loopthrough pokedex

for filename in os.listdir(source):
    if filename.endswith('.jpg'):
        with open(os.path.join(source , filename)) as f:
            content = f.read()
# convertjpg to png
        content.save(f'{dest}{filename}'+'.png', 'png')
        dir = dest
        if not os.path.isdir(dir): os.makedirs(dir)
        fname = 'forcing' + str(forcing) + 'damping' + str(damping) + 'omega' + str(omega) + 'set2.png'
        content.savefig(os.path.join(dir, fname))
# save to new folder
