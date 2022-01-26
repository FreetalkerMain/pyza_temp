# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
"""#<input patern>
N

x_R x_G x_B

t_1 c_1

t_2 c_2

...

t_N c_N

"""

input_line = int(input())
rgb = input().rstrip().split(' ')
print(rgb[0]+","+rgb[1]+","+rgb[2])
s = [""]*input_line
for i in range(input_line):
    s[i] = input().rstrip().split(' ')
    print(s[i][0]+" ,"+s[i][1])



