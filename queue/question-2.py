
def get_queue():
  queue = []
  persons = int(input('Enter with number of persons: '))
  print('Enter with number of pages peer person')
  for x in range(persons):
    get = int(input())
    queue.append(get)

  return queue

queue = get_queue()

def printer():
  if (queue[0] - 10) <= 0:
    print(str(queue[0]) + ' done')

    queue.pop(0)
  else:
    queue.append(queue[0] - 10)
    print(str(queue[0] - 10) + ' moved to the end of the queue')
    queue.pop(0)

while(len(queue) != 0):
  printer()