# coding: utf-8

"""
Задача о покрытии множества.
В данном случае используется приближенный алгоритм для оптимального выбора радиостанций
для покрытия всех штатов.
"""

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = dict()
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print final_stations
