from os import remove

WEED_VALUE = 35
METH_VALUE = 70
COCAINE_VALUE = 150

def main():
    # create all of our dictionaries
    values_dict = create_values_dict('csv-files/effect_values')
    mixing_dict = create_mixing_dict('csv-files/mixing.csv')
    mixer_dict = create_mixer_dict('csv-files/mixer.csv')

    # get input from user, and create our present effects list
    drug = int(input("Which drug are you using? ( 0 = Weed | 1 = Meth | 2 = Cocaine): "))
    effects_input = input("Which effects are present? (Separate names with commas!): ").split(',')
    present_effects = []
    for e in effects_input:
        present_effects.append(e.strip())
    present_effects.sort()

    # find maximum mult value able to be added using mixing_dict
    max = 0
    removed_effect = ''
    new_effect = ''
    passive_effect = ''
    m = ''
    for effect in present_effects:
        for mixer in mixing_dict:
            if effect in mixing_dict[mixer]:
                mult = get_total_mult(values_dict, mixer_dict, mixing_dict, present_effects, effect, mixer)
                if mult > max:
                    max = round(mult, 2)
                    removed_effect = effect
                    new_effect = mixing_dict[mixer][effect]
                    passive_effect = mixer_dict[mixer]
                    m = mixer



    # Get information required for printing
    initial_mult = 1
    initial_value = 0
    new_effects = [] + present_effects
    new_mult = 1
    new_value = 0

    new_effects.remove(removed_effect)
    new_effects.append(new_effect)
    new_effects.append(passive_effect)
    new_effects.sort()

    for effect in present_effects:
        initial_mult = initial_mult + values_dict[effect]

    for effect in new_effects:
        new_mult = new_mult + values_dict[effect]

    if drug == 0:
        initial_value = WEED_VALUE * initial_mult
        new_value = WEED_VALUE * new_mult
    elif drug == 1:
        initial_value = METH_VALUE * initial_mult
        new_value = METH_VALUE * new_mult
    elif drug == 2:
        initial_value = COCAINE_VALUE * initial_mult
        new_value = COCAINE_VALUE * new_mult

    initial_mult = round(initial_mult, 2)
    initial_value = round(initial_value, 2)
    new_mult = round(new_mult, 2)
    new_value = round(new_value, 2)


    # print information
    print("Best value found!")
    print(f"Initial effects: {present_effects}")
    print(f"Initial effects mult: {initial_mult}\nInitial value: {initial_value}")
    print(f"\033[31mRemoved {removed_effect}\033[0m")
    print(f"\033[32mAdded {new_effect}, {passive_effect} with {m} for an extra {round(new_mult - initial_mult, 2)} multiplier\033[0m")
    print(f"New effects: {new_effects}")
    print(f"New effects mult: {new_mult}\nNew value: {new_value}")


main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")


