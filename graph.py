# coding: utf-8

from collections import deque


graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom_mango', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom_mango'] = []
graph['jonny'] = []


def person_is_seller(name):
    if 'mango' in name:
        return True
    else:
        return False


# Поиск по графу в ширину
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print person + ' is seller'
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


print search('you')
