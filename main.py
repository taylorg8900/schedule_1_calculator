from drug import Drug
from dicts import create_mixer_dict
import sys

def main():
    drug = Drug('weed', ['athletic', 'calming', 'energizing', 'focused', 'jennerising', 'laxative', 'seizure inducing', 'thought provoking'])
    drug.add_mixer('mega bean')
    # best_strains = find_best_strains(drug, 3)
    # worst_strains = find_worst_strains(drug, 2)
    # strains = [] + best_strains + worst_strains
    # print(drug.get_mult())
    # print(drug.get_effects())
    drug.large_representation()

    # for strain in strains:
    #     print()
    #     print(strain.get_mult())
    #     print(strain.get_added_mixer())
    #     print(strain.get_effects())



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


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")


