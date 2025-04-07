from dicts import create_modify_dict, create_mixer_dict, create_values_dict

class Drug:
    def __init__(self, drug_type, effects):
        self._type = drug_type
        self._mult = 0
        self._value = 0
        self._effects = {}
        self._added_mixer = ''
        self._added_effect = ''
        self._added_mult = 0
        self._modified_effects = {}

        self._value_dict = {}
        self._mixer_dict = {}
        self._modify_dict = {}

        self.__create_dicts()

        for effect in effects:
            self._effects[effect] = self._value_dict[effect]

        self.__calc_mult()
        self.__calc_value()

    def add_mixer(self, mixer):
        self._added_mixer = mixer.lower()
        self._added_effect = self._mixer_dict[self._added_mixer]
        self._added_mult = self._value_dict[self._mixer_dict[self._added_mixer]]

        self.__create_modified_effects_dict(mixer)
        self.__modify_effects(mixer)

        self.__calc_mult()
        self.__calc_value()


    def __create_modified_effects_dict(self, mixer):
        dict = {}
        for effect in self._effects:
            if effect in self._modify_dict[mixer]:
                dict[effect] = self._modify_dict[mixer][effect]
        self._modified_effects = dict

    def __modify_effects(self, mixer):
        new_effects = {}
        for effect in self._effects:
            if effect in self._modify_dict[mixer]:
                new_effects[self._modify_dict[mixer][effect]] = self._value_dict[self._modify_dict[mixer][effect]]
            else:
                new_effects[effect] = self._effects[effect]

        # We include this because if that effect already exists, we don't want to add it a second time.
        new_effects[self._added_effect] = self._value_dict[self._mixer_dict[self._added_mixer]]
        self._effects = new_effects


    def __create_dicts(self):
        self._value_dict = create_values_dict('csv-files/values.csv', 0, 1)
        self._mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
        self._modify_dict = create_modify_dict('csv-files/modify.csv', 2, 0, 1)

    def __calc_mult(self):
        total = 1
        for effect in self._effects:
            total += self._effects[effect]
        self._mult = round(total, 2)

    def __calc_value(self):
        drug_name = self._type.lower().strip()
        if drug_name.startswith('we'):
            self._value = self._mult * 35
        elif drug_name.startswith('me'):
            self._value = self._mult * 70
        elif drug_name.startswith('co'):
            self._value = self._mult * 150
        else:
            self._value = 0
        self._value = round(self._value, 2)

    def get_type(self):
        return self._type

    def get_mult(self):
        return self._mult

    def get_value(self):
        return self._value

    def get_effects(self):
        return list(self._effects.keys())

    def get_added_mixer(self):
        return self._added_mixer
