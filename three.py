import re

def advent_three_one():
    with open('three.txt', 'r') as three:
        test = three.read()
        test_update = ''.join(test)
        results = re.findall(r'mul\((\d+),(\d+)\)', test_update)
        multi = [int(x[0]) * int(x[1]) for x in results]
        return sum(multi)

# def advent_three_one_helper(case: str):
#     result = 0
#     pref = 'mul('
#     max_substr_len = 11
#     for i in range(len(case)):
#         sample = case[i:i + len(pref)]
#         if sample == pref:
#             test_case = case[i:i + max_substr_len:+1]
#             print(test_case)
#             end = test_case.find(')')
#             print(end)
#             if end == -1:
#                 continue
#             list_test_case = test_case[len(pref):end]
#             print(list_test_case)
        
#             multi = list(map(int, [x.strip() for x in test_case[len(pref):end].split(',') if x.strip()]))

#             if len(multi) > 2:
#                 print(multi)
                
#                 result += multi[0] * multi[1]
#     return result
# if __name__ == "__main__":
#     print(advent_three_one())

