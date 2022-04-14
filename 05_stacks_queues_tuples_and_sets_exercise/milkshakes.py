import sys
from io import StringIO

input1 = """6 3 - 2 1 * 5 /"""

input2 = """2 2 - 1 *"""

input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)