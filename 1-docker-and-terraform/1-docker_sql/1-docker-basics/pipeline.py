import sys

import pandas as pd

print(sys.argv)

# sys.argv[0] is name of the file
# e.g. 
# winpty docker run -it test:pandas 2024-01-13 
# (winpty on windows)
# ['pipeline.py', '2024-01-13']
# job finished successfully for day = 2024-01-13

day = sys.argv[1]

print(f'job finished successfully for day = {day}')
