# sequence = 'UTA*EC**R**O**'
sequence = input('Entre com a sequência: ')

queue = []

def decipher(character):
  if (character == '*'):
    unpacks(character)

  else:
    stacks(character)


def stacks(character):
  queue.append(character)
  print(character + ' - stacked')

def unpacks(character):
  if (len(queue) == 0):
    print('Error: ueue is already empty!')
  else:
    queue.pop()
    print(character + ' - unpacked')

for i in sequence:
  decipher(i)
