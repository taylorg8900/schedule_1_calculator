
import sys

values = {}
d = open('effect_values')
for line in d:
    fields = line.split(',')
    values[fields[0]] = float(fields[1])
d.close()

if len(sys.argv) == 0:
    print(f"usage: (mixer)")
else:
    f = open('effect_list')
    for line in f:
        if sys.argv[1] in line:
            first = line.split(" + ")
            second = first[1].strip("\n").split(',')
            third = [] + [first[0].strip()] + [second[0]] + [second[2].strip()]
            list = third
            # print(f"first: {first}")
            # print(f"second: {second}")
            # print(f"third: {third}")
            # list = things.split(",")
            if (list[0] not in values) or (list[1] not in values) or (list[2] not in values):
                print(f"This line is spelled incorrectly!! : {line}")
                # print(f"list actual: .{list[0]}. .{list[1]}. .{list[2]}.")
            else:
                value = round((values[list[0]] + values[list[1]] - values[list[2]]), 2)
                print(f"{line.strip('\n')}: \033[96madded value = {value}\033[0m")
    f.close()
# for value in biglist:
#     print(f"| {value}         |")

