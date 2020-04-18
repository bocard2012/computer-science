open_sym = ['{', '(', '[']
close_sym = ['}', ')', ']']

# success = '{(([]{}))}{}'
# fail = '{(([]{}))}{[}'

sequence = input('Enter with your code: ')

queue = []
error = []

def parentesis(character):
  if (character in open_sym):
    stacks(character)
  elif (character in close_sym):
    unpacks(character)

def stacks(character):
  queue.append(character)

def unpacks(character):
  if ((len(queue) != 0) and (queue[-1] == get_reveres(character))):
    queue.pop()
  else:
    error.append(character)

def get_reveres(character):
  if (character in close_sym):
    return (open_sym[close_sym.index(character)])
  elif (character in open_sym):
    return(close_sym[open_sym.index(character)])

for i in sequence:
  parentesis(i)

if ((len(error) == 0) and (len(queue) == 0)):
  print('success')
else:
  print('fail')
