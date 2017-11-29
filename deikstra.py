# coding: utf-8


def find_lowest_cost_node(costs):
    min_cost = float('inf')
    min_cost_node = None
    for node, cost in costs.items():

        if cost < min_cost and node not in processed:
            min_cost = cost
            min_cost_node = node
    return min_cost_node


# graph = dict()
# graph['start'] = dict()
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# graph['a'] = dict()
# graph['a']['fin'] = 1
# graph['b'] = dict()
# graph['b']['fin'] = 5
# graph['b']['a'] = 3
# graph['fin'] = dict()
#
# costs = dict()
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = float('inf')
#
# parents = dict()
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = dict()
graph['a']['d'] = 2
graph['a']['c'] = 4
graph['b'] = dict()
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = dict()
graph['c']['fin'] = 3
graph['c']['d'] = 6
graph['d'] = dict()
graph['d']['fin'] = 1
graph['fin'] = dict()

costs = dict()
costs['a'] = 5
costs['b'] = 2
costs['c'] = float('inf')
costs['d'] = float('inf')
costs['fin'] = float('inf')

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None

processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

node = 'fin'
while True:
    print node
    if node == 'start':
        break
    node = parents[node]
