# use python3
from collections import Counter, namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(input_str):
    h = []
    for ch, freq in Counter(input_str).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _coun1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, __count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, s):
    pass


def main():
    input_str = input()
    code = huffman_encode(input_str)
    encoded = "".join(code[ch] for ch in input_str)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


def test(n_iter=100):
    import random
    import string
    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s


if __name__ == '__main__':
    main()
