from drug import Drug
from dicts import create_mixer_dict, create_typo_dict
import sys

# TODO: be able to handle more than 3 strains printed out. Probably have them come in groups of 3? Define this with a global, or figure out the width of the shell during runtime
MAX_HORIZONTAL_REPRESENTATIONS = 5

def main():
    drug_type = input("Drug type: ")
    effects_input = input("Effects (separate with commas!: ")
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
        print(drugs[0].get_effects(), end='')
        for d in range(len(mixers)):
            print(' + ' + mixers[d], end='')
        print()

        for line in drugs[-1].small_representation():
            print(line)

        print_lists_horizontally(reps)

        choice = input("Enter a strain number to repeat (Q to quit) (0 to go back by one strain): ")

        if choice.isdigit():
            if int(choice) < 1:
                drugs.pop(-1)
                mixers.pop(-1)
                continue
            elif int(choice) > len(strains):
                choice = len(strains)
            drug = Drug(strains[int(choice) - 1].get_type(), strains[int(choice) - 1].get_effects())
            drugs.append(drug)
            mixers.append(strains[int(choice) - 1].get_added_mixer())
        else:
            break


def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)

def print_lists_horizontally(superlist):
    """
    Used to print each element of each list next to each other, in a horizontal fashion.
    """
    PADDING = 2
    amount_horizontal_rep = split_amount(len(superlist), MAX_HORIZONTAL_REPRESENTATIONS)
    line_lengths = []
    list_lengths = []
    for l in superlist:
        line_lengths.append(max(len(item) for item in l))
        list_lengths.append(len(l))

    for line in range(max(list_lengths)):
        for representation in range(len(superlist)):
            if line < len(superlist[representation]):
                print(f'{superlist[representation][line]:<{line_lengths[representation] + PADDING}}', end='')
            else:
                print(f'{' ':<{line_lengths[representation] + PADDING}}', end='')
        print()


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