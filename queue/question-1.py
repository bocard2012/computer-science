import random

people = int(input('Enter with number of participants: '))

x = random.randint(1, people)

queue = []

def potato():
  for x in range(1, people + 1):
    print('Participant number ' + str(x))
    get = input('Enter with her name: ')
    queue.append(get)

potato()


def skip():
  queue.append(queue[0])
  queue.pop(0)

def peek():
  print(queue[0] + ' eliminated')
  queue.pop(0)

def play():
  changes = 0
  while(changes <= x):
    skip()
    changes = changes + 1

  peek()


while(len(queue) != 1):
  play()

print(queue[0] + " wins!")
