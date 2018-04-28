"""
https://10xrecruit.kattis.com
Problem B
A bee larva living in a hexagonal cell of a large honeycomb decides to creep for a walk. 
In each “step” the larva may move into any of the six adjacent cells and after n steps, 
it is to end up in its original cell. Your program has to compute, 
for a given n, the number of different such larva walks.
"""

hive = []

def create_hive():
    return [[[-1 for z in range(15)] for x in range(40)] for y in range(40)]

def is_already_known_path(pos_x, pos_y, remaining_steps):
    if hive[pos_x][pos_y][remaining_steps] is not -1:
        return True
    return False

def get_successful_walk_count(pos_x, pos_y, remaining_steps):
    return hive[pos_x][pos_y][remaining_steps]

def travel(pos_x, pos_y, remaining_steps):
    
    if is_already_known_path(pos_x, pos_y, remaining_steps):
        return get_successful_walk_count(pos_x, pos_y, remaining_steps)

    if remaining_steps == 0:
        return 1 if pos_x == 20 and pos_y == 20 else 0
    
    walk_count = 0

    walk_count += travel(pos_x, pos_y - 1, remaining_steps - 1)
    walk_count += travel(pos_x, pos_y + 1, remaining_steps - 1)
    walk_count += travel(pos_x + 1, pos_y - 1, remaining_steps - 1)
    walk_count += travel(pos_x - 1, pos_y + 1, remaining_steps - 1)
    walk_count += travel(pos_x - 1, pos_y, remaining_steps - 1)
    walk_count += travel(pos_x + 1, pos_y, remaining_steps - 1)
    
    hive[pos_x][pos_y][remaining_steps] = walk_count
    return walk_count


def main(test_case):
    global hive
    hive = create_hive()
    
    steps = []
    for i in range(test_case):
        steps.append(int(input()))

    for n in steps:    
        print(travel(20, 20, n))

if __name__ == '__main__':
    test_case = int(input())
    main(test_case)