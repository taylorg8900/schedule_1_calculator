from dicts import create_mixer_dict
from drug import Drug
import time

def main():
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)

    drug = Drug('meth', ['toxic'])
    before = time.time()
    final_value, mixer_path = find_best_strain_recursively(drug, mixer_dict, 5)
    after = time.time()
    print(f"\nDone in {after - before:.3f} seconds!")
    print(f"Best value: {final_value}")
    print(f"Best mixer path: {' -> '.join(mixer_path)}")


def find_best_strain_recursively(drug, mixer_dict, iterations):
    if iterations == 0:
        return drug.get_mult(), []  # return the value and an empty path

    max_value = 0
    best_path = []

    for mixer in mixer_dict.keys():
        new_drug = Drug(drug.get_type(), drug.get_effects())
        new_drug.add_mixer(mixer)
        value, path = find_best_strain_recursively(new_drug, mixer_dict, iterations - 1)

        if value > max_value:
            max_value = value
            best_path = [mixer] + path  # prepend current mixer to the path

    return max_value, best_path


main()