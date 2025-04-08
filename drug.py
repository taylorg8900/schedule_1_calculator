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

    def large_representation(self):

        first_block = [
            f'| Drug type:    {self._type} |',
            f'| Drug mult:    {self._mult} |',
            f'| Drug value: $ {self._value} |'
        ]
        second_block = [
            f'| Added Mixer: {self._added_mixer} |',
            f'| Added effect: {self._added_effect} |',
            f'| Added mult: {self._added_mult} |',
        ]
        third_block = []

        c = 0
        d = 0
        for effect in self._modified_effects:
            if len(str(effect)) > c:
                c = len(str(effect))
            if len(self._modified_effects[effect]) > d:
                d = len(self._modified_effects[effect])

        for effect in self._modified_effects:
            string = f'| {effect:<{c}} -> {self._modified_effects[effect]:<{d}} |'
            third_block.append(string)


        max_amount_chars = 0
        all_lines = [] + first_block + second_block + third_block
        for line in all_lines:
            if max_amount_chars < len(line):
                max_amount_chars = len(line)

        a = 0
        for element in [self._type, self._mult, self._value]:
            if len(str(element)) > a:
                a = len(str(element))

        first_block_representation = [
            f'{'-' * max_amount_chars}',
            f'| Drug type:    {self._type:<{max_amount_chars - 16}} |',
            f'| Drug mult:    {self._mult:<{max_amount_chars - 16}} |',
            f'| Drug value: $ {self._value:<{max_amount_chars - 16}} |',
            f'|{' ' * max_amount_chars}|'
        ]

        b = 0
        for element in [self._added_mixer, self._added_effect, self._added_mult]:
            if len(str(element)) > b:
                b = len(str(element))

        second_block_representation = [
            f'| Added mixer:  {self._added_mixer:<{max_amount_chars - 16}} |',
            f'| Added effect: {self._added_effect:<{max_amount_chars - 16}} |',
            f'| Added mult:   {self._added_mult:<{max_amount_chars - 16}} |',
            f'|{' ' * max_amount_chars}|'
        ]

        c = 0
        d = 0
        for effect in self._modified_effects:
            if len(str(effect)) > c:
                c = len(str(effect))
            if len(self._modified_effects[effect]) > d:
                d = len(self._modified_effects[effect])

        third_block_representation = [
            f'| Modified effects{' ' * (max_amount_chars - 18)} |'
        ]

        e = max_amount_chars - c - d
        print(f'c: {c}')
        print(f'd: {d}')
        print(f'e: {e}')

        for effect in self._modified_effects:
            # print(f"c={c} ({type(c)}), e={e} ({type(e)})")
            string = f'| {effect:<{c}} -> {self._modified_effects[effect]}'
            string = string + (' ' * (max_amount_chars - len(string) - 1)) + '|'

            third_block_representation.append(string)

        f = 0
        for effect in self._effects:
            if len(str(effect)) > f:
                f = len(str(effect))

        fourth_block_representation = [
            f'|{' ' * max_amount_chars}|',
            f'| {'Effects':<{f}}  Mult{' ' * (max_amount_chars - f - 8)} |'
        ]

        for effect in self._effects:
            string = f'| {effect:<{f}}  {self._effects[effect]}{' ' * (max_amount_chars - 2 - f - 2 - len(str(self._effects[effect])))}|'
            fourth_block_representation.append(string)
        fourth_block_representation.append(f'{'-' * max_amount_chars}')

        print(max_amount_chars)
        lines = [] + first_block_representation + second_block_representation + third_block_representation + fourth_block_representation
        for line in lines:
            print(line)





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
        new_effects = dict(sorted(new_effects.items()))
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
        l = list(self._effects.keys())
        l.sort()
        return l

    def get_added_mixer(self):
        return self._added_mixer
