
import sys

values = {}
d = open('csv-files/effect_values')
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
            fields = line.strip('\n').split(',')
            first = fields[0].strip()
            second = fields[1].strip()
            fourth = fields[3].strip()
            if (first not in values) or (second not in values) or (fourth not in values):
                print(f"This line is spelled incorrectly!! : {line}")
                print(f"list actual: .{first}. .{second}. .{fourth}.")
            else:
                value = round((values[first] + values[second] - values[fourth]), 2)
                print(f"{line.strip('\n')}: \033[96madded value = {value}\033[0m")
    f.close()


