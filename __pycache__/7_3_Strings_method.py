# find() and index()

name = "Nadun Prabhasha"

print(name.find('o'))

print(name.find('a'))

print(name.rfind('a'))

print(name.find('ra'))

print(name.index('a'))

#print(name.index('o'))

# Center

print(name.center(20))
print(name.ljust(20))
print(name.rjust(20))

print(name.center(20,"-"))
print(name.ljust(20,"-"))
print(name.rjust(20,"-"))

# strip()

n = "    nadun "

print(n)
print(n.strip())
print(n.lstrip())
print(n.rstrip())


N = "------prabhasha-----"

print(N)
print(N.strip('-'))
print(N.lstrip('-'))
print(N.rstrip('-'))



