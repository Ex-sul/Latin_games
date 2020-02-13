import random

verb1 = "laudo, laudāre, laudavi, laudatum, to praise"
verb2 = "habeo, habēre, habui, habitum, to have"


class LatinVerb:
    def __init__(self, lexical_entry):
        self.lexical_entry = lexical_entry
        self.parsed_entry = self.lexical_entry.split(",", maxsplit=4)
        self.second_principal_part = self.parsed_entry[1]
        self.conjugation = self.identify_conj()

    def identify_conj(self):
        if self.second_principal_part[-3] == "ā":
            return 1
        elif self.second_principal_part[-3] == "ē":
            return 2
        elif self.second_principal_part[-3] == "e":
            return 3
        elif self.second_principal_part[-3] == "ī":
            return 4
        else:
            print("Unable to identify conjugation.")

verb1_obj = LatinVerb(verb1)
print(verb1_obj.lexical_entry)
print("Conjugation:", str(verb1_obj.conjugation))




# inf1 = "laudare"
# print(inf1[-2] + inf1[-1] == "re")

# print(verb1.split(",", maxsplit=4))
