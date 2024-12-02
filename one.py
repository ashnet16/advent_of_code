import heapq
from collections import Counter

def advent_one_one():
    with open('one.txt', 'r') as file:
        left_heap, right_heap = [], []
        for line in file:
            left, right = map(int, line.split())
            heapq.heappush(left_heap, left)
            heapq.heappush(right_heap, right)
        return sum(abs(heapq.heappop(left_heap) - heapq.heappop(right_heap))
                   for _ in range(len(left_heap)))


def advent_one_two():
    with open('one.txt', 'r') as file:
        left_list = []
        right_counts = Counter()

        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_counts[right] += 1

        return sum(left * right_counts.get(left, 0) for left in left_list)


if __name__ == "__main__":
    print(advent_one_one())
    print(advent_one_two())

