from math import floor


class PriorityQueue:
    def __init__(self):
        super().__init__()
        self.queue = []
        pass

    def insert(self, x):
        self.queue.append(x)
        self.sift_up(len(self.queue) - 1)

    def extract_max(self):
        max_elem, self.queue[0] = self.queue[0], self.queue[-1]
        del self.queue[-1]
        self.sift_down(0)
        return max_elem

    def sift_down(self, node_index):
        if len(self.queue) <= 1:
            return
        left_leaf_index = ((node_index + 1) * 2) - 1
        right_leaf_index = (node_index + 1) * 2
        left_leaf = None
        right_leaf = None
        lenght = len(self.queue)
        if (lenght - 1) >= left_leaf_index:
            left_leaf = self.queue[left_leaf_index]
        if (lenght - 1) >= right_leaf_index:
            right_leaf = self.queue[right_leaf_index]
        if left_leaf is None:
            return
        elif right_leaf is None:
            max_leaf_index = left_leaf_index
        else:
            if right_leaf > left_leaf:
                max_leaf_index = right_leaf_index
            else:
                max_leaf_index = left_leaf_index
        if self.queue[node_index] < self.queue[max_leaf_index]:
            self.queue[node_index], self.queue[max_leaf_index] = self.queue[max_leaf_index], self.queue[node_index]
            self.sift_down(max_leaf_index)
        else:
            return

    def sift_up(self, i):
        if i == 0:
            return
        parrent_index = int(floor((i + 1) / 2.0)) - 1
        if self.queue[i] > self.queue[parrent_index]:
            self.queue[i], self.queue[parrent_index] = self.queue[parrent_index], self.queue[i]
            self.sift_up(parrent_index)
        else:
            return

    def __repr__(self):
        return str(self.queue)


def main():
    hip = PriorityQueue()
    count_operations = int(input())
    for i in range(count_operations):
        temp = input().split()
        print(temp)
        if temp[0].lower() == 'insert':
            hip.insert(int(temp[1]))
        elif temp[0].lower() == 'extractmax':
            print()
            print(hip)
            print(hip.extract_max())


if __name__ == '__main__':
    main()
