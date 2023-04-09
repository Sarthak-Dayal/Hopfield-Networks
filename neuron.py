class Neuron:
  def __init__(self, init_state):
    self.v = init_state
  def update(self, new_state):
    self.v = new_state
  def __str__(self):
    return str(self.v)