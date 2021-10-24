# Loading .ph files

import argparse
from commands import ask_, send_

parser = argparse.ArgumentParser(description='loads .ph file')

parser.add_argument(
    '-l',
    '--load',
    type=str,
    help='Enter the name of the .ph file.'
)

args = parser.parse_args()
file = args.load

try:
 code = open(args.load, 'r')
 text = code.read()
except:
 code = input('') 
 text = code.read()  

try:
    send_(text)
    ask_(text)
except:
    pass    
