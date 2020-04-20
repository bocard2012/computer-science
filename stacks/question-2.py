# sequence = input('Enter with your code: ')
sequence = '))(('
queue = []
error = []

def parentesis(character):
  if (character == ')'):
    unpacks(character)
  else:
    stacks(character)

def stacks(character):
  queue.append(character)

def unpacks(character):
  if (len(queue) != 0):
    queue.pop()
  else:
    error.append(character)

for i in sequence:
  parentesis(i)

print(error)
print(queue)

if ((len(queue) != 0) or (len(error) != 0)):
  print('false')
else:
  print('true')
