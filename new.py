
import sys
#
# values = {}
# d = open('effect_values')
# for line in d:
#     fields = line.split(',')
#     values[fields[0]] = float(fields[1])
# d.close()

# if len(sys.argv) == 0:
#     print(f"usage: (mixer)")
# else:
#     f = open('effect_list')
#     for line in f:
#         if sys.argv[1] in line:
#             fields = line.strip('\n').split(',')
#             first = fields[0].strip()
#             second = fields[1].strip()
#             fourth = fields[3].strip()
#             if (first not in values) or (second not in values) or (fourth not in values):
#                 print(f"This line is spelled incorrectly!! : {line}")
#                 print(f"list actual: .{first}. .{second}. .{fourth}.")
#             else:
#                 value = round((values[first] + values[second] - values[fourth]), 2)
#                 print(f"{line.strip('\n')}: \033[96madded value = {value}\033[0m")
#     f.close()

def main():

    # create dictionary for effects and their value multipliers
    effect_values = create_dict('effect_values', 0, 1)
    #mix_values = create_dict('effect_list', 3, 4)

    drug_present = input("Enter drug (weed | meth | coke): ")
    effects_present_input = input("current effects (insert commas between effects): ")
    effects_present = effects_present_input.split(',')

    max = 0
    added_effects = []
    removed_effect = ''

    # f = open('effect_list')
    # for line in f:
    #     fields = line.split(',')
    #     for effect in effects_present:
    #         if effect in fields[3]:
    #             if effect_values[effect.strip()] > max:
    #                 max = effect_values[effect.strip()]
    #                 added_effects = [fields[0], fields[1]]
    f = open('effect_list')
    f.readline()
    for line in f:
        fields = line.split(',')

        for effect in effects_present:
            if effect == fields[3].strip():
                mult = float(fields[4].strip('\n'))
                if mult > max:
                    max = mult
                    added_effects = [fields[0].strip(), fields[1].strip()]
                    removed_effect = fields[3].strip()

    print()
    print(f"Maximum additional value multiplier found: {max}")
    print(f"\033[31mRemoved effects:{removed_effect}\033[0m")
    print(f"\033[32mAdded effects: {added_effects[0]}, {added_effects[1]}\033[0m")
    print(f"Original effects: {effects_present_input}")
    print(f"Original effects multiplier: {find_value_multiplier(effects_present, effect_values)}")

def create_dict(file, key_index, value_index):
    '''
    This file takes a csv file, and will return a dictionary with the keys and values being whichever indexes we specify.
    '''
    values = {}
    f = open(file)
    # discard header
    f.readline()
    for line in f:
        fields = line.split(',')
        values[fields[key_index].strip()] = float(fields[value_index])
    f.close()
    return values


def find_value_multiplier(list, dict):
    '''
    This function takes a list and a dict, and returns the amount total for the items in the list which are found in the dict.
    '''
    total = 0
    for item in list:
        if item in dict:
            total = total + dict[item]
    return total

def find_drug_value(drug, multiplier):
    '''
    Drugs
    Weed = 0
    Meth = 1
    Coke = 2
    '''
    values = [35, 70, 150]
    return (values[drug] * multiplier)

main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")
