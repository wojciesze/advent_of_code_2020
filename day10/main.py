import re
from scipy import special


test_input = """
16
10
15
5
1
11
7
19
6
12
4
"""

test_input2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

input = """
8
40
45
93
147
64
90
125
149
145
111
126
9
146
38
97
103
6
122
34
18
35
96
86
116
29
59
118
102
26
66
17
74
94
5
114
128
1
75
47
141
58
65
100
63
12
53
25
106
136
15
82
22
117
2
80
79
139
7
81
129
19
52
87
115
132
140
88
109
62
73
46
24
69
101
110
16
95
148
76
135
142
89
50
72
41
39
42
56
51
57
127
83
121
33
32
23
"""

data = []
diff_data = []
contingency = []


def read_input(i):
    global data
    cnt = 0
    for line in i.split("\n"):
        if re.match('\s*$', line):
            continue
        data.append(int(line))
        cnt += 1

    data = sorted(data)
    cnt = 1
    while cnt < len(data):
        diff_data.append(data[cnt] - data[cnt-1])
        cnt +=1


def part1():
    print('[Part 1] numer=', (diff_data.count(1)+1) * (diff_data.count(3)+1))


def factorial(n):
    if n > 0:
        return n*factorial(n-1)
    else:
        return 1


def part2():
    cur = 0
    prev = 0
    for x in diff_data:
        if x == 1 and prev == 1:
            if cur > 0:
                cur += 1
            else:
                cur = 2
        else:
            if cur > 0:
                contingency.append(cur)
            cur = 0
        prev = x

    cnt = 0
    res = 0
    for x in contingency:
        if cnt > 0:
            res = res + factorial(x)
        else:
            res = factorial(x)
        cnt += 1

    print(contingency)
    print(res)


if __name__ == '__main__':
    read_input(test_input2)
    print('IN', data)
    # part1()
    print(diff_data)
    part2()
    print(sum(contingency))
    print(special.binom(3, 2))






