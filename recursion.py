from dicts import create_mixer_dict
from drug import Drug

def main():
    mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)

    drug = Drug('meth', ['toxic'])
    print(type(drug))
    value = find_best_strain_recursively(drug, mixer_dict, 2)
    print(value)

def find_best_strain_recursively(drug, mixer_dict, iterations):
    if iterations == 0:
        return drug.get_mult()
    max_value = 0
    for mixer in mixer_dict.keys():
        new_drug = Drug(drug.get_type(), drug.get_effects())
        new_drug.add_mixer(mixer)
        value = find_best_strain_recursively(new_drug, mixer_dict, iterations - 1)
        if value > max_value:
            max_value = value
    return max_value

main()