import sys
import numpy as np

if (len(sys.argv) > 1) and (sys.argv[1] == "debug"):
    import ptvsd
    print("waiting...")
    ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))
    ptvsd.wait_for_attach()

print('hello python!')

for i in range(10 ** 5):
    print("") #nop
    pass

print('python version:' + str(sys.version_info))
## i = ?

print('numpy version:' + np.version.full_version)
