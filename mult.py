

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
        mixing_dict[mixer][original_effect]
    )

    passive_effect_mult = get_effect_mult(
        values_dict,
        present_effects,
        mixer_dict[mixer]
    )

    original_effect_mult = values_dict[original_effect]

    return new_effect_mult + passive_effect_mult - original_effect_mult