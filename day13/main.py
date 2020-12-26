import re
from multiprocessing import Process

test_input = """
939
7,13,x,x,59,x,31,19
"""

test_input2 = """
123
1789,37,47,1889
"""

test_input3 = """
123
8,16,32,64,x,x,x,128
"""

input = """
1015292
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23
"""

ts = 0
buses = {}
max_offset = 0
max_bus = 0
second_max_bus = 0
third_max_bus = 0
safe_step = 1


def read_input(i):
    global buses, ts, max_offset, max_bus, second_max_bus, third_max_bus, safe_step
    lines = []
    for line in i.split("\n"):
        if re.match('\s*$', line):
            continue
        lines.append(line)

    ts = int(lines[0])
    cnt = 0
    for bus in lines[1].split(','):
        if cnt == 0:
            safe_step = int(bus)
        if bus != 'x':
            buses[int(bus)] = cnt
        cnt += 1
    max_offset = cnt-1
    _t = sorted([x for x in buses])
    max_bus = _t[-1]
    second_max_bus = _t[-2]


def part1():
    loop_end = 0
    cnt = ts-1
    while loop_end == 0:
        cnt += 1
        for bus in buses:
            if cnt % bus == 0:
                print(f'[Part 1] bus={bus}, ts={cnt}, minutes={cnt-ts}, number={(cnt-ts)*bus}')
                break
        else:
            continue
        break


def gcd():
    cnt = max_bus
    while cnt > 0:
        cnt2 = 0
        for x in buses:
            if x % cnt == 0:
                cnt2 += 1
        if cnt2 == len(args):
            return cnt
        cnt -= 1
    return None


def part2(start=0, new_step=1):
    print(f'START-- start={start}, step={new_step}')
    loop_end = 0
    cnt = start
    step = 1
    while loop_end == 0:
        allign = set()
        for bus in buses:
            if (cnt + buses[bus]) % bus == 0:
                allign.add(bus)
            else:
                continue

        if max_bus in allign and second_max_bus in allign and step == 1:
            print('New step is set at cnt=', cnt)
            step = max_bus * second_max_bus

        if len(allign) == len(buses):
            print('Found it: ',cnt)
            break
        if cnt % 10000000 == 0 and cnt > 0:
            print(cnt)
        cnt += step

    print(f'END--start={start}')


if __name__ == '__main__':
    read_input(test_input)
    a = set(buses)
    print('INPUT:', set(buses), 'max bus: ', max_bus, 'max_bus_offset=', buses[max_bus])
    print('      ', [buses[x] for x in a])
    args = [bus for bus in buses]
    g = gcd()
    print(safe_step)
    # part2()





