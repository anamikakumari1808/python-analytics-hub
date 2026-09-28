a = 31
t = type(a) # classs <int>
print(t)

a = 31.2
t = type(a) # classs <int>
print(t)

a = "31"
t = type(a) # classs <int>
print(t)

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) # classs <int>

print(t)