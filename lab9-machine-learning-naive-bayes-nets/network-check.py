from numbers import Number


network = {
  'Y': {
    'Parents': [],
    'CPT': {
      (): (4 + 2) / (7 + 2) / ((7 + 2 * 2)/(7 + 2)),
    }
  },
  'X1': {
    'Parents': ['Y'],
    'CPT': {
      (True,): (1 + 2) / (4 + (2 * 2)), # P(X1=True | Y=True)
      (False,): (3 + 2) / (3 + (2 * 2)), # P(X1=True | Y=False)
    }
  },
  'X2': {
    'Parents': ['Y'],
    'CPT': {
      (True,): (1 + 2) / (4 + (2 * 2)), #  P(X2=True | Y=True)
      (False,): (2 + 2) / (3 + (2 * 2)),  # P(X2=True | Y=False)
    }
  },
  'X3': {
    'Parents': ['Y'],
    'CPT': {
      (True,): (0 + 2) / (4 + (2 * 2)), # P(X3=True | Y=True)
      (False,):(0 + 2) / (3 + (2 * 2)), # P(X3=True | Y=False)
    }
  },
}

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")


for assignment, prob in sorted(network['Y']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))

for assignment, prob in sorted(network['X1']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))