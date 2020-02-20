import random

verb1_lex = "laudo, laudāre, laudavi, laudatum, to praise"
verb1_trans = "praise"
verb1_trans_3rd = "praises"
verb1_trans_imperf = "praising"
verb1 = [verb1_lex, verb1_trans, verb1_trans_3rd, verb1_trans_imperf]

verb2_lex = "habeo, habēre, habui, habitum, to have"
verb2_trans = "have"
verb2_trans_3rd = "has"
verb2_trans_imperf = "having"
verb2 = [verb2_lex, verb2_trans, verb2_trans_3rd, verb2_trans_imperf]


class LatinRegularVerb:
    subjects = ['I', 'you', 'he', 'we', 'you all', 'they']
    person = ['first', 'second', 'third'] * 2
    number = ['singular'] * 3 + ['plural'] * 3

    def __init__(self, lexical_entry, verb_trans, verb_trans_3rd, verb_trans_imperf):
        # PARSING
        self.lexical_entry = lexical_entry
        self.parsed_entry = self.lexical_entry.split(", ", maxsplit=4)
        self.infinitive = self.parsed_entry[1]
        self.conjugation = self.identify_conj()
        self.pres_stem = self.identify_pres_stem()
        # TRANSLATION
        self.verb_trans = verb_trans
        self.verb_trans_3rd = verb_trans_3rd
        self.verb_trans_imperf = verb_trans_imperf
        # PRESENT SYSTEM
        self.pres_tense = self.conjugate_pres_tense()
        self.fut_tense = self.conjugate_fut_tense()
        self.imperf_tense = self.conjugate_imperf_tense()

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
        tense = ["present"] * 6
        if self.conjugation == 1:
            conjugated_forms = [self.pres_stem[:-1] + "o"] + \
                               [self.pres_stem + e for e in pres_endings[1:]]
            translations = [f"{s} {self.verb_trans}" for s in self.subjects[:2]] + \
                           [f"he {self.verb_trans_3rd}"] + \
                           [f"{s} {self.verb_trans}" for s in self.subjects[3:]]
            return list(zip(tense, self.person, self.number, conjugated_forms, translations))
        elif self.conjugation == 2:
            conjugated_forms = [self.pres_stem + e for e in pres_endings]
            translations = [f"{s} {self.verb_trans}" for s in self.subjects[:2]] + \
                           [f"he {self.verb_trans_3rd}"] + \
                           [f"{s} {self.verb_trans}" for s in self.subjects[3:]]
            return list(zip(tense, self.person, self.number, conjugated_forms, translations))

    def conjugate_fut_tense(self):
        first_second_fut_endings = ['bo', 'bis', 'bit', 'bimus', 'bitis', 'bunt']
        tense = ["future"] * 6
        if self.conjugation == 1 or self.conjugation == 2:
            conjugated_forms = [self.pres_stem + e for e in first_second_fut_endings]
            translations = [f"{s} will {self.verb_trans}" for s in self.subjects]
            return list(zip(tense, self.person, self.number, conjugated_forms, translations))

    def conjugate_imperf_tense(self):
        imperf_endings = ['bam', 'bas', 'bat', 'bamus', 'batis', 'bant']
        tense = ["imperfect"] * 6
        if self.conjugation == 1 or self.conjugation == 2:
            conjugated_forms = [self.pres_stem + e for e in imperf_endings]
            translations = [f"I was {self.verb_trans_imperf}", f"you were {self.verb_trans_imperf}",
                            f"he was {self.verb_trans_imperf}"] + \
                           [f"{s} were {self.verb_trans_imperf}" for s in self.subjects[3:]]
            return list(zip(tense, self.person, self.number, conjugated_forms, translations))


verb1_obj = LatinRegularVerb(*verb2)
print(verb1_obj.lexical_entry)
print("Present Stem:", verb1_obj.pres_stem)
for x in verb1_obj.imperf_tense:
    print(x)




# inf1 = "laudare"
# print(inf1[-2] + inf1[-1] == "re")

# print(verb1.split(",", maxsplit=4))
