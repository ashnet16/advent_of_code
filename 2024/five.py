def build_holder():
    holder = {}
    with open('five_one.txt') as five:
        input = five.readlines()
        for i in input:
            element = list(map(int, i.strip().split('|')))
            if element[0] in holder:
                holder[element[0]].add(element[1])
            else:
                holder[element[0]] = set([element[1]])
        return holder

def build_list():
    list_val = []
    with open('five_two.txt') as five:
        input = five.readlines()
        for element in input:
            list_val.append(list(map(int, element.strip().split(','))))
        return list_val

def advent_five_one():
    total = 0
    test_map = build_holder()
    value_list = build_list()
    for sublist in value_list:
        is_valid = True
        sublist_length = len(sublist)
        
        for idx, value in enumerate(sublist):
            if idx == 0:
                continue
            if value in test_map:
                for prev_idx in range(idx - 1, -1, -1):
                    if sublist[prev_idx] in test_map[value]:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            mid_index = sublist_length // 2
            total += sublist[mid_index]
    return total


# def build_holder_2():
#     holder = {}
#     for element in input_vals:
#         if element[0] in holder:
#             holder[element[0]].add(element[1])
#         else:
#             holder[element[0]] = set([element[1]])
#     return holder


# input_vals = [(47, 53), (97, 13), (97, 61), (97, 47), (75, 29), (61, 13), (75, 53), (29, 13), 
#  (97, 29), (53, 29), (61, 53), (97, 53), (61, 29), (47, 13), (75, 47), (97, 75), 
#  (47, 61), (75, 61), (47, 29), (75, 13), (53, 13)]

# list_val = [
#     [75, 47, 61, 53, 29],
#     [97, 61, 53, 29, 13],
#     [75, 29, 13],
#     [75, 97, 47, 61, 53],
#     [61, 13, 29],
#     [97, 13, 75, 29, 47]
# ]

holder =  build_holder()


def is_valid(sublist: list):
    seen = set()
    for i in range(len(sublist)):
        if sublist[i] in holder:
            if any(x in holder[sublist[i]] for x in seen):
                return False
        seen.add(sublist[i])
    return True
   

def fix_list(broken: list) -> list:
    for i in range(len(broken)-1, -1, -1):
        if broken[i] in holder:
            test_cases = holder[broken[i]]
            for j in range(i-1, -1, -1):
                if broken[j] in test_cases:
                    broken[i], broken[j] = broken[j], broken[i]
                    break
    return broken


def advent_five_two():
    value_list = build_list()
    total = 0
    for sublist in value_list:
        if not is_valid(sublist):
            mid_index = len(sublist) // 2
            valid = False
            list_transform = sublist[:]
            while not valid:
                fix_list(list_transform)
                if is_valid(list_transform):
                    total += list_transform[mid_index]
                    valid = True
                    continue
    return total
if __name__ == "__main__":     
   print(advent_five_one())
   print(advent_five_two())