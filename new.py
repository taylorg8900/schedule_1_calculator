
def main():
    # create all of our dictionaries
    values_dict = create_values_dict('csv-files/effect_values')
    mixing_dict = create_mixing_dict('csv-files/mixing.csv')
    mixer_dict = create_mixer_dict('csv-files/mixer.csv')



    # # UNCOMMENT WHEN TESTING IS DONE
    # # get input from user, and create our present effects list
    # drug = int(input("Which drug are you using? ( 0 = Weed | 1 = Meth | 2 = Cocaine): "))
    # effects_input = input("Which effects are present? (Separate names with commas!): ").split(',')
    # present_effects = []
    # for e in effects_input:
    #     present_effects.append(e.strip())




def create_values_dict(filename):
    '''
    Takes a file and creates a dictionary which contains float values for each effect in the game
    '''
    f = open(filename)
    f.readline()
    d = {}
    for line in f:
        fields = line.split(',')
        key = fields[0].strip()
        value = float(fields[1].strip().strip('\n'))
        d[key] = value
    f.close()
    return d

def create_mixing_dict(filename):
    '''
    Takes a file and creates a dictionary of dictionaries, with the following example structure:
    mixes = {
        chili: {
            'shrinking': 'refreshing',
            'athletic': 'euphoric',
            'munchies': 'toxic',
            'anti gravity': 'tropic thunder',
            'sneaky': 'bright eyed',
            'laxative': 'long faced' },
        addy: {
            'glowing': 'refreshing',
            'foggy': 'energizing',
            'sedating': 'gingeritis',
            'long faced': 'electrifying',
            'explosive': 'euphoric'}
    }

    The key in each sub-dictionary is an original effect, and the value is what the effect turns into when combined with the mixer which has the name of the sub-dictionary.
    '''
    f = open(filename)
    f.readline()
    d = {}
    for line in f:
        fields = line.split(',')
        og_effect = fields[0].strip()
        new_effect = fields[1].strip()
        mixer = fields[2].strip().strip('\n')
        if mixer not in d:
            d[mixer] = {}
        d[mixer][og_effect] = new_effect
    f.close()
    return d

def create_mixer_dict(filename):
    '''
    Takes a file and creates a dictionary, where the key is a mixer and the value is the effect it passively adds to a drug.
    For example, 'chili' will add 'spicy'.
    mixers = {
        'chili': 'spicy',
        'viagra': 'tropic thunder'
    }
    '''
    f = open(filename)
    f.readline()
    d = {}
    for line in f:
        fields = line.split(',')
        mixer = fields[0].strip()
        effect = fields[1].strip().strip('\n')
        d[mixer] = effect
    f.close()
    return d

def get_effect_mult(values_dict, present_effects, effect):
    '''
    Returns the value of an effect, as long as it is not already present.
    '''
    if effect not in present_effects:
        return values_dict[effect]
    return 0

def get_total_mult(values_dict, mixer_dict, mixing_dict, present_effects, original_effect, mixer):
    '''
    Finds the total mult value that can be added to our drug, for the specified original effect and mixer.
    '''
    new_effect_mult = get_effect_mult(
        values_dict,
        present_effects,
        mixing_dict[mixer[original_effect]]
    )

    passive_effect_mult = get_effect_mult(
        values_dict,
        present_effects,
        mixing_dict[mixer[original_effect]]
    )

    original_effect_mult = values_dict[original_effect]

    return new_effect_mult + passive_effect_mult - original_effect_mult

main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")
