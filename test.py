import sys
from io import StringIO

input1 = """>Invalid<<!5
>Invalid<<!5
>Invalid<<!5
Purchase"""

sys.stdin = StringIO(input1)

import re

text = input()
regex = r"(?P<Day>\d{2})(?P<separator>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
valid_data = re.finditer(regex, text)
for date in valid_data:
    current_date = data.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}", )

