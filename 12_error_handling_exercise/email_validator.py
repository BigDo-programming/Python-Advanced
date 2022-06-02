import sys
from io import StringIO

input1 = """abc@abv.bg
End"""
input2 = """peter@gmail.com
petergmail.com
End"""
input3 = """peter@gmail.hotmail
End"""
input4 = """peter@hotmail.jsd
End"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
sys.stdin = StringIO(input4)


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    data = input()
    if data == "End":
        break

    if "@" not in data:
        raise MustContainAtSymbolError("Email must contain @")

    email_parts = data.split("@")
    username = email_parts[0]
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    mail_server_and_domain = email_parts[1].split(".")
    domain = mail_server_and_domain[1]
    if domain not in "com, bg, org, net":
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
