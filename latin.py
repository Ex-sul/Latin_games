import random

verb1 = "laudo, laudāre, laudavi, laudatum, to praise"
verb1_trans = "praise"
verb1_trans_3rd = "praises"
verb1_trans_imperf = "praising"

verb2 = "habeo, habēre, habui, habitum, to have"
verb2_trans = "have"
verb2_trans_3rd = "has"
verb2_trans_imperf = "having"


class LatinRegularVerb:
    def __init__(self, lexical_entry):
        self.lexical_entry = lexical_entry
        self.parsed_entry = self.lexical_entry.split(",", maxsplit=4)
        self.infinitive = self.parsed_entry[1]
        self.conjugation = self.identify_conj()
        self.pres_stem = self.identify_pres_stem()

    def identify_conj(self):
        if self.infinitive[-3] == "ā":
            return 1
        elif self.infinitive[-3] == "ē":
            return 2
        elif self.infinitive[-3] == "e":
            return 3
        elif self.infinitive[-3] == "ī":
            return 4
        else:
            print("Unable to identify conjugation.")

    def identify_pres_stem(self):
        if self.conjugation == 1:
            return self.infinitive[:-3] + "a"
        elif self.conjugation == 2:
            return self.infinitive[:-3] + "e"
        elif self.conjugation == 3:
            return self.infinitive[:-3]
        elif self.conjugation == 4:
            return self.infinitive[:-3] + "i"
        else:
            print("Unable to identify the present stem.")

    def conjugate_pres_tense(self):
        pres_endings = ["o", "s", "t", "mus", "tis", "nt"]
        if self.conjugation == 1:
            return [self.pres_stem[:-1] + "o"] + [self.pres_stem + e for e in pres_endings[1:]]

    def conjugate_fut_tense(self):
        pass

    def conjugate_imperf_tense(self):
        pass

verb1_obj = LatinRegularVerb(verb2)
print(verb1_obj.lexical_entry)
print("Present Stem:", verb1_obj.pres_stem)




# inf1 = "laudare"
# print(inf1[-2] + inf1[-1] == "re")

# print(verb1.split(",", maxsplit=4))
