import random

num_neurons = 8
memories_to_store = [[-1, 1, 1, -1, 1, -1, -1, -1], [1, 1, 1, 1, 1, 1, 1, 1]]
current_network = []
weights = []

# Initialize all neurons RANDOMLY (add controls later??)
for i in range(num_neurons):
  current_network.append(random.choice([-1,1]))
# Initialize weights based on memory pattern
for i in range(num_neurons):
  weight_row = []
  for j in range(num_neurons):
    # The neuron does not connect to itself
    if i == j:
      weight_row.append(0)
    else:
      mem_sum = 0
      for memory in memories_to_store:
        vi = memory[i]
        vj = memory[j]
        mem_sum += vi * vj
        weight_row.append(mem_sum / len(memories_to_store))
        weights.append(weight_row)
      
# Weighted sum function for some random neuron
def update():
  # pick a random neuron
  random_index = random.randint(0, num_neurons - 1)

  # compute the weighted sum of all connections
  sum = 0
  for j in range(num_neurons):
    if j is not random_index:
        sum += weights[j][random_index] * current_network[j]
    # set number to set the neuron to to either 1 or -1
    threshold = 0
    if sum >= threshold:
      current_network[random_index]=1
    else:
      current_network[random_index]=-1


for i in range(50):
  print(current_network)
  update()


# Very simplified, later make ways to add multiple memories and more
num_neurons = 7
memories_to_store = [[1, 1, -1, 1, -1, -1, -1], [1, 1, 1, 1, 1, 1, 1]]
current_network = []
weights = []

# Initialize all neurons RANDOMLY (add controls later??)
for i in range(num_neurons):
  current_network.append(random.choice([-1,1]))
# Initialize weights based on memory pattern
for i in range(num_neurons):
  weight_row = []
  for j in range(num_neurons):
    # The neuron does not connect to itself
    if i == j:
      weight_row.append(0)
    else:
      mem_sum = 0
      for memory in memories_to_store:
        vi = memory[i]
        vj = memory[j]
        mem_sum += vi * vj
        weight_row.append(mem_sum / len(memories_to_store))
        weights.append(weight_row)
      
# Weighted sum function for some random neuron
def update():
  # pick a random neuron
  random_index = random.randint(0, num_neurons - 1)

  # compute the weighted sum of all connections
  sum = 0
  for j in range(num_neurons):
    if j is not random_index:
        sum += weights[j][random_index] * current_network[j]
    # set number to set the neuron to to either 1 or -1
    threshold = 0
    if sum >= threshold:
      current_network[random_index]=1
    else:
      current_network[random_index]=-1


for i in range(50):
  print(current_network)
  update()