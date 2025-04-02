values = {
    'anti gravity': .54,
    'athletic': .32,
    'balding': .30,
    'bright eyed': .40,
    'calming': .10,
    'calorie dense': .28,
    'cyclopean': .56,
    'disorienting': .00,
    'electrifying': .50,
    'energizing': .22,
    'euphoric': .18,
    'explosive': .00,
    'focused': .16,
    'foggy': .36,
    'gingeritis': .20,
    'glowing': .48,
    'jennerising': .42,
    'laxative': .00,
    'long faced': .52,
    'munchies': .12,
    'paranoia': .00,
    'refreshing': .14,
    'schizophrenia': .00,
    'sedating': .26,
    'seizure inducing': .00,
    'shrinking': .60,
    'slippery': .34,
    'smelly': .00,
    'sneaky': .24,
    'spicy': .38,
    'thought provoking': .44,
    'toxic': .00,
    'tropic thunder': .46,
    'zombifying': .58
}
import sys

f = open(sys.argv[1])
biglist = []
for line in f:
    if 'viagra' in line:
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
            biglist.append(value)
# for value in biglist:
#     print(f"| {value}         |")
f.close()
