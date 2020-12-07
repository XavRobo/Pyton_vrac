bags = {}

for l in open("inputs/input7.txt", "r").readlines():
    l2 = l.split(' contain ')
    bags.update({l2[0][:-5]: (l2[1][:-2].split(", "))})


def add_bag(col):
    sum = 0
    for bag in bags.items():
        if(bag[0]==col):
            for e in bag[1]:
                s = e.split()
                if(s[0]=='no'):
                    sum += 0
                else:
                    f = int(s[0])
                    color = s[1] + ' ' + s[2]
                    sum += add_bag(color) * f
    return sum+1

print(add_bag('shiny gold')-1)