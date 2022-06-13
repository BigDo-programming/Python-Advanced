import sys
from io import StringIO

input1 = """abc@abv.bg
End"""
input2 = """peter@gmail.com
petergmail.com
End"""
input3 = """peter@gmail.hotmail
End"""
input4 = """peter@hotmail.com
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


def is_domain_invalid(domain, valid_domains):
    result = True
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            result = False
            break
    return result


valid_domains = ["com", "bg", "org", "net"]

while True:
    data = input()
    if data == "End":
        break

    if "@" not in data:
        raise MustContainAtSymbolError("Email must contain @")

    email_parts = data.split("@")
    username, domain = email_parts
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if is_domain_invalid(domain, valid_domains):
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
