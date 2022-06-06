from pyfiglet import figlet_format
import sys
from io import StringIO

input1 = """Hello World!"""

input2 = """Python 3.10"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def print_art(msg):
    print_msg = figlet_format(msg)
    print(print_msg)


print_art(input())