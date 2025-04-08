from drug import Drug
from dicts import create_mixer_dict
import sys

def main():
    # drug_type = input("Drug type: ")
    # effects_input = input("Effects (separate with commas): ").split(',')
    # effects = []
    # for effect in effects_input:
    #     effect = effect.strip()
    #     effects.append(effect)

    drug = Drug('cocaine', ['athletic', 'foggy', 'bright eyed'])
    strains = find_best_strains(drug, 2)
    strains.extend(find_worst_strains(drug, 1))


    reps = []
    counter = 1
    for strain in strains:
        representation = strain.large_representation()
        representation.insert(0, f'STRAIN {counter}')
        reps.append(representation)
        counter += 1

    print_lists_horizontally(reps)

def print_lists_horizontally(superlist):
    """
    Used to print each element of each list next to each other, in a horizontal fashion.
    """
    PADDING = 2
    line_lengths = []
    list_lengths = []
    for l in superlist:
        line_lengths.append(max(len(item) for item in l))
        list_lengths.append(len(l))

    for line in range(max(line_lengths)):
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

main()