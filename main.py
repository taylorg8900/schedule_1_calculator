from drug import Drug
from dicts import create_mixer_dict

def main():
    drug = Drug('weed', ['athletic', 'calming', 'focused', 'shrinking'])
    drug.add_mixer('mega bean')
    print(drug.get_effects())
    strains = find_best_strains(drug, 4)
    print(drug.get_mult())
    print(drug.get_effects())

    for strain in strains:
        print()
        print(strain.get_mult())
        print(strain.get_effects())


def find_best_strains(drug_object, amount):
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
    strains = []
    best_strains = []

    # Create a new strain from every possible mixer in the game
    for mixer in mixer_dict:
        new_drug = Drug(drug_object.get_type, drug_object.get_effects)
        new_drug.add_mixer(mixer)
        strains.append(new_drug)

    # Compare all new strains to find which ones have the best value
    for i in range(amount):
        max = 0
        best = strains[0]
        for strain in strains:
            if strain.get_mult() > max:
                best = strain
        strains.remove(best)
        best_strains.append(best)
    return best_strains


main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")


