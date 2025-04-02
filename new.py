
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
    effect_values = create_dict('csv-files/effect_values', 0, 1)
    #mix_values = create_dict('effect_list', 3, 4)

    drug_present = int(input("Enter drug (weed = 0 | meth = 1 | coke = 2 ): "))
    effects_present_input = input("current effects (insert commas between effects): ")
    effects_present = effects_present_input.split(',')
    effects_present.sort()

    print(effects_present)
    max = 0
    added_effects = []
    removed_effect = ''

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

    original_mult = find_value_multiplier(effects_present, effect_values)
    original_value = find_drug_value(drug_present, original_mult)

    print(f"effects present = {effects_present}")
    print(f"removed effect = {removed_effect}")
    print(f"added effects = {added_effects}")
    new_effects = new_total_effects(effects_present, removed_effect, added_effects)

    new_mult = find_value_multiplier(new_effects, effect_values)
    new_value = find_drug_value(drug_present, new_mult)

    print()
    print(f"\033[36mMaximum additional value multiplier found: {max}\033[0m")
    print(f"Original effects: {effects_present_input}")
    print(f"Original effects multiplier, and value: {original_mult}, ${original_value}")
    print(f"\033[31mRemoved effects: {removed_effect}\033[0m")
    print(f"\033[32mAdded effects: {added_effects[0]}, {added_effects[1]}\033[0m")
    print(f"New effects: {list_to_str(new_effects)}")
    print(f"New effects multiplier, and value: {new_mult}, ${new_value}")

def list_to_str(list):
    str = ''
    length = len(list)
    for i in range(length):
        if i == length - 1:
            str = str + ", " + list[i]
        elif i == 0:
            str = list[0]
        else:
            str = str + ', ' + list[i]
    return str

def new_total_effects(original_effects, removed_effect, added_effects):
    og = []
    for element in original_effects:
        og.append(element.strip())
    og.remove(removed_effect.strip())
    for element in added_effects:
        if element.strip() not in og:
            og.append(element)
    og.sort()
    return og


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
    total = 1
    for item in list:
        if item.strip() in dict:
            total = total + dict[item.strip()]
    return round(total, 2)

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
