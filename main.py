from drug import Drug
from dicts import create_mixer_dict
import sys

def main():
    drug_type = input("Drug type: ")
    effects = input("Effects (separate with commas): ").split(',')
    for effect in effects:
        effect = effect.strip()
    drug = Drug(drug_type, effects)
    strains = find_best_strains(drug, 2)
    strains.extend(find_worst_strains(drug, 1))


    lines = drug.small_representation()
    for line in lines:
        print(line)


    representations = []
    for strain in strains:
        representations.append(strain.large_representation())
    representations.sort(reverse=True)
    max_len = max(len(r) for r in representations)
    for i in range(max_len):
        row = ''
        for lst in representations:
            item = lst[i] if i < len(lst) else ''
            row += f'{item:<5} '
        print(row)






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