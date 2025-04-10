from dicts import create_mixer_dict, create_typo_dict
from drug import Drug
import time


def main():
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
    drug_type = input("Drug type: ")
    effects_input = input("Effects (separate with commas!): ")
    depth = int(input("Enter a recursion depth: "))

    # Get 'effects' argument to create our drug object
    typo_dict = create_typo_dict('csv-files/typo.csv', 0, 1)
    effects = []
    for effect in effects_input.split(','):
        for key in typo_dict.keys():
            if key in effect:
                effects.append(typo_dict[key])

    drug = Drug(drug_type, effects)
    drug = Drug(drug_type, effects)
    before = time.time()
    final_value, mixer_path = find_best_strain_recursively(drug, mixer_dict, depth)
    after = time.time()
    print(f"\nDone in {after - before:.3f} seconds!")
    print(f"Best value: {final_value}")
    print(f"Best mixer path: {' -> '.join(mixer_path)}")

def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)

def find_best_strain_recursively(drug, mixer_dict, iterations, mixers=[]):
    if iterations == 0:
        return drug.get_mult(), []  # return the value and an empty path

    max_value = 0
    best_path = []
    m = [] + mixers
    m.append(drug.get_added_mixer())
    clear()
    for a in m:
        print(f'{a:<13}', end='')
    print('\n', drug.get_mult())
    for mixer in mixer_dict.keys():
        new_drug = Drug(drug.get_type(), drug.get_effects())
        new_drug.add_mixer(mixer)
        value, path = find_best_strain_recursively(new_drug, mixer_dict, iterations - 1, m)

        if value > max_value:
            max_value = value
            best_path = [mixer] + path  # prepend current mixer to the path

    return max_value, best_path


main()