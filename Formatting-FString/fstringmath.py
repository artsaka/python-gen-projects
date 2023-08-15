import math

number_n = math.pi

print(type(number_n))
print(f"Using Numeric {number_n = }")
print(f"|{number_n:25}|")
print(f"|{number_n:<25}|") # "<" forces to be left-aligned with 25 spaces after pi's value
print(f"|{number_n:>25}|") # ">" forces to be right-aligned
print(F"|{number_n:^25}|")
print("\n")


# fill character in the alignment of f-strings
number_n = "Python 3.10"
print(type(number_n))
print(f"Using = to filled in the alignment of the f-strings")
print(f"Using Numeric {number_n = }")
print(f"|{number_n:=<25}|")
print(f"|{number_n:=>25}|")
print(f"|{number_n:^25}|")
print("\n")

# represent strings and numbers:- s, d, n, e, f, %

number_n = 10
print(type(number_n))
print(f"Using Numeric {number_n = }")
print(f"This prints without formatting {number_n}")
print(f"This prints with formatting {number_n:d}")
print(f"This prints also with formatting {number_n:n}")
print(f"This prints with spacing {number_n:10d}\n")

number_n = math.pi
print(type(number_n))
print(f"Using Numeric {number_n = }")
print(f"This prints without formatting {number_n}")
print(f"This prints with formatting {number_n:f}")
print(f"This prints also with formatting {number_n:n}")
print(f"This prints with spacing {number_n:10f}\n")

# using f-strings to display exponent notations and the percentage notations
variable = 5
print(type(variable))

