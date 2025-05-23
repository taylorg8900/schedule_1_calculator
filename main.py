from drug import Drug
from dicts import create_mixer_dict, create_typo_dict
import sys
import os

# TODO: Create some way for algorithm to search recursively n amount of times for best value strain, then print it out

def main():
    drug_type = input("Drug type: ")
    effects_input = input("Effects (separate with commas!): ")
    amount_strains = int(input("Amount of strains: "))

    # Get 'effects' argument to create our drug object
    typo_dict = create_typo_dict('csv-files/typo.csv', 0, 1)
    effects = []
    for effect in effects_input.split(','):
        for key in typo_dict.keys():
            if key in effect:
                effects.append(typo_dict[key])

    drug = Drug(drug_type, effects)
    drugs = []
    mixers = []
    drugs.append(drug)
    strain_tracker = []

    while True:
        clear()
        strains = find_best_strains(drugs[-1], amount_strains)

        # Create names for each strain
        reps = []
        counter = 1
        for strain in strains:
            representation = strain.large_representation()
            representation.insert(0, f'STRAIN {counter}')
            reps.append(representation)
            counter += 1

        # Print all information to screen
        print('\nCURRENT STRAIN:', drugs[0].get_effects(), end='')
        for d in range(len(mixers)):
            print(' + ' + mixers[d], end='')
        print('\nCurrent strain', end='')
        for strain in strain_tracker:
            print(' + ' + str(strain), end='')
        print()

        for line in drugs[-1].small_representation():
            print(line)
        print('\n')

        print_lists_horizontally(reps)

        choice = input("Enter a strain number to repeat (Q to quit) (press Enter to go back by one strain): ")

        if choice.isdigit():
            if int(choice) < 1:
                continue
            elif int(choice) > len(strains):
                choice = len(strains)
            drug = Drug(strains[int(choice) - 1].get_type(), strains[int(choice) - 1].get_effects())
            drugs.append(drug)
            mixers.append(strains[int(choice) - 1].get_added_mixer())
            strain_tracker.append(int(choice))
        else:
            if choice == '':
                if len(drugs) == 1:  # Never let user get rid of first drug in drugs
                    continue
                drugs.pop(-1)
                mixers.pop(-1)
                strain_tracker.pop(-1)
                continue
            break


def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)


def print_lists_horizontally(superlist):
    """
    Prints each element of each list next to each other, horizontally in groups.
    Dynamically sizes based on terminal width.
    """
    PADDING = 2
    terminal_width = os.get_terminal_size().columns
    list_lengths = [len(l) for l in superlist]
    line_lengths = [max((len(item) for item in l), default=0) for l in superlist]

    amount_horizontal_rep = get_fitting_column_groups(line_lengths, terminal_width, PADDING)

    index = 0
    for group_size in amount_horizontal_rep:
        current_lists = superlist[index: index + group_size]
        current_line_lengths = line_lengths[index : index + group_size]
        current_list_lengths = list_lengths[index: index + group_size]
        max_lines = max(current_list_lengths)

        for line in range(max_lines):
            for i in range(group_size):
                if line < len(current_lists[i]):
                    print(f'{current_lists[i][line]:<{current_line_lengths[i] + PADDING}}', end='')
                else:
                    print(' ' * (current_line_lengths[i] + PADDING), end='')
            print()

        print()
        index += group_size

def get_fitting_column_groups(widths, max_width, padding):
    """
    Returns a list of group sizes that fit within the terminal width,
    using the actual widths of each column.
    """
    groups = []
    current_width = 0
    current_group_size = 0

    for w in widths:
        col_width = w + padding
        if current_width + col_width <= max_width:
            current_width += col_width
            current_group_size += 1
        else:
            if current_group_size > 0:
                groups.append(current_group_size)
            current_width = col_width
            current_group_size = 1

    if current_group_size > 0:
        groups.append(current_group_size)

    return groups





def find_best_strains(drug_object, amount):
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
    strains = []
    best_strains = []
    worst_strain = 0

    # Create a new strain from every possible mixer in the game
    for mixer in mixer_dict:
        new_drug = Drug(drug_object.get_type(), drug_object.get_effects())
        new_drug.add_mixer(mixer)
        strains.append(new_drug)

    # Compare all new strains to find which ones have the best value
    for i in range(amount):
        if i < len(mixer_dict.keys()): # Never let user ask for more strains than mixers in the game
            max = 0
            best = strains[0]
            for strain in strains:
                if strain.get_mult() > max:
                    max = strain.get_mult()
                    best = strain
            strains.remove(best)
            best_strains.append(best)
    return best_strains


def find_worst_strains(drug_object, amount):
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
    strains = []
    worst_strains = []

    # Create a new strain from every possible mixer in the game
    for mixer in mixer_dict:
        new_drug = Drug(drug_object.get_type(), drug_object.get_effects())
        new_drug.add_mixer(mixer)
        strains.append(new_drug)

    # Compare all new strains to find which ones have the best value
    for i in range(amount):
        min = 100_000
        worst = strains[0]
        for strain in strains:
            if strain.get_mult() < min:
                min = strain.get_mult()
                worst = strain
        strains.remove(worst)
        worst_strains.append(worst)
    return worst_strains

def split_amount(amount, divisor):
    result = [divisor] * (amount // divisor)
    remainder = amount % divisor
    if remainder:
        result.append(remainder)
    return result

main()