# Day one solution

import os

def read_input_file(filename: str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    instructions = []
    with open(full_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            dir_char = line[0]
            steps = int(line[1:])
            instructions.append((dir_char, steps))

    return instructions

def turn_dial(dir: str, steps: int, start = 50, upper=99, lower=0):
    size = (upper - lower ) + 1 
    if dir == 'R':
        turn_dial_lock = lower + (start - lower + steps) % size
    else:
        turn_dial_lock = lower + (start - lower - steps) % size
    return turn_dial_lock



def main():
    password = 0
    input = read_input_file('one.txt')
    current = 50
    for dir, step in input:
        current = turn_dial(dir=dir, steps=step, start=current)
        if current == 0:
            password+=1
    return password



if __name__ == "__main__":
    print(main())