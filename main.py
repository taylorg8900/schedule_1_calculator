from drug import Drug

def main():
    drug = Drug('weed', ['athletic', 'calming', 'focused', 'shrinking'])
    drug.add_mixer('mega bean')
    print(drug.get_mult())
    print(drug.get_effects())


main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")


