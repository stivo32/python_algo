import random, time


def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [element for element in list[1:] if element <= pivot]
        greater = [element for element in list[1:] if element > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


list = [random.randint(1, 10000) for i in xrange(1, random.randint(1000, 10000))]
start = time.time()
print quick_sort(list)
print time.time() - start


