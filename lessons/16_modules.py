from foo import hi
import foo as f

f.hi()

print(f.greetings['morning'])
print(f.greetings['afternoon'])
print(f.greetings['evening'])
print(f.greetings['night'])

print(dir(f))

hi()
