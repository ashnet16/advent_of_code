import re

def advent_three_one():
    with open('three.txt', 'r') as three:
        test = three.read()
        test_update = ''.join(test)
        results = re.findall(r'mul\((\d+),(\d+)\)', test_update)
        multi = [int(x[0]) * int(x[1]) for x in results]
        return sum(multi)

def avent_three_one_two():
    caluclate = True
    result = 0
    pattern = r"((mul\(\d+\,\d+\))|(do\(\))|(don\'t\(\)))"
    with open('three.txt', 'r') as three:
        test = three.read()
        results = re.findall(pattern, test)
        for match in results:
            match_test = match[0]
            if match_test == "don't()":
                caluclate = False
                continue
            if match_test == "do()":
                caluclate = True
                continue
            if match_test.startswith("mul(") and caluclate:
                pre_result =  match_test[4:len(match_test) - 1].split(',')
                result += int(pre_result[0]) * int(pre_result[1])
            
    return result

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

