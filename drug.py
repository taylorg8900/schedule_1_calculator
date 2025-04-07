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

        self._value_dict = {}
        self._mixer_dict = {}
        self._modify_dict = {}

        self.__create_dicts()

        for effect in effects:
            self._effects[effect] = self._value_dict[effect]

        self.__calc_mult()
        self.__calc_value()

    def __create_dicts(self):
        self._value_dict = create_values_dict('csv-files/values.csv', 0, 1)
        self._mixer_dict = create_mixer_dict('csv-files/mixer.csv', 0, 1)
        self._modify_dict = create_modify_dict('csv-files/modify.csv', 2, 0, 1)

    def __calc_mult(self):
        total = 1
        for effect in self._effects:
            total += self._effects[effect]
        self._mult = total

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

    def get_mult(self):
        return self._mult