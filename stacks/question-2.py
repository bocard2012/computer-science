sequence = input('Enter with your code: ')

queue = []

def parentesis(character):
  if (character == ')'):
    unpacks(character)
  else:
    stacks(character)

def stacks(character):
  queue.append(character)

def unpacks(character):
  try:
    queue.pop()
  except:
    print('error')

for i in sequence:
  parentesis(i)

if (len(queue) != 0):
  print('error')
