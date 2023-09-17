import os
import stl
from stl import mesh


# Import binary STL and convert to ASCII
home = os.path.expanduser('~')
bin_mesh = mesh.Mesh.from_file(os.path.join(home, 'Downloads/Scan_the_World_-_Venus_de_Milo.stl'))
bin_mesh.save('Venus_de_Milo_ascii.stl', mode=stl.Mode.ASCII)