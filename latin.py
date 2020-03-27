

class LatinRegularVerb:
    subjects = ['I', 'you', 'he', 'we', 'you all', 'they']
    person = ['first', 'second', 'third'] * 2
    number = ['singular'] * 3 + ['plural'] * 3

    def __init__(self, lexical_entry, verb_trans, verb_trans_3rd, verb_trans_imperf):
        # PARSING
        self.lexical_entry = lexical_entry
        self.parsed_entry = self.lexical_entry.split(", ", maxsplit=4)
        s = ", "
        self.principal_parts = s.join(self.parsed_entry[:-1])
        self.infinitive = self.parsed_entry[1]
        self.conjugation = self.identify_conj()
        self.pres_stem = self.identify_pres_stem()
        # TRANSLATION
        self.verb_trans = verb_trans
        self.verb_trans_3rd = verb_trans_3rd
        self.verb_trans_imperf = verb_trans_imperf
        # PRESENT SYSTEM
        self.pres_act_inf = ("infinitive", "", "", self.infinitive, self.parsed_entry[-1])
        self.imp_sg = ("imperative", "", "singular", self.pres_stem, self.verb_trans)
        self.imp_pl = ("imperative", "", "plural", self.pres_stem + "te", self.verb_trans)
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


class SumLatinIrregularVerb():
    def __init__(self):
        self.lexical_entry = "sum, esse, fui, futurum, to be"
        self.parsed_entry = self.lexical_entry.split(", ", maxsplit=4)
        s = ", "
        self.principal_parts = s.join(self.parsed_entry[:-1])
        self.infinitive = self.parsed_entry[1]
        # PRESENT SYSTEM
        self.pres_act_inf = ("infinitive", "", "", self.infinitive, self.parsed_entry[-1])
        self.pres_tense = (("present", "first", "singular", "sum", "I am"),
                           ("present", "second", "singular", "es", "you are"),
                           ("present", "third", "singular", "est", "he is"),
                           ("present", "first", "plural", "sumus", "we are"),
                           ("present", "second", "plural", "estis", "you all are"),
                           ("present", "third", "plural", "sunt", "they are"))
        self.fut_tense = (("future", "first", "singular", "ero", "I will be"),
                           ("future", "second", "singular", "eris", "you will be"),
                           ("future", "third", "singular", "erit", "he will be"),
                           ("future", "first", "plural", "erimus", "we will be"),
                           ("future", "second", "plural", "eritis", "you all will be"),
                           ("future", "third", "plural", "erunt", "they will be"))
        self.imperf_tense = (("imperfect", "first", "singular", "eram", "I was"),
                           ("imperfect", "second", "singular", "eras", "you were"),
                           ("imperfect", "third", "singular", "erat", "he was"),
                           ("imperfect", "first", "plural", "eramus", "we were"),
                           ("imperfect", "second", "plural", "eratis", "you all were"),
                           ("imperfect", "third", "plural", "erant", "they were"))


class PossumLatinIrregularVerb:
    def __init__(self):
        self.lexical_entry = "possum, posse, potui, to be able"
        self.parsed_entry = self.lexical_entry.split(", ", maxsplit=3)
        s = ", "
        self.principal_parts = s.join(self.parsed_entry[:-1])
        self.infinitive = self.parsed_entry[1]
        # PRESENT SYSTEM
        self.pres_act_inf = ("infinitive", "", "", self.infinitive, self.parsed_entry[-1])
        self.pres_tense = (("present", "first", "singular", "possum", "I am able"),
                           ("present", "second", "singular", "potes", "you are able"),
                           ("present", "third", "singular", "potest", "he is able"),
                           ("present", "first", "plural", "possumus", "we are able"),
                           ("present", "second", "plural", "potestis", "you all are able"),
                           ("present", "third", "plural", "possunt", "they are able"))
        self.fut_tense = (("future", "first", "singular", "potero", "I will be able"),
                          ("future", "second", "singular", "poteris", "you will be able"),
                          ("future", "third", "singular", "poterit", "he will be able"),
                          ("future", "first", "plural", "poterimus", "we will be able"),
                          ("future", "second", "plural", "poteritis", "you all will be able"),
                          ("future", "third", "plural", "poterunt", "they will be able"))
        self.imperf_tense = (("imperfect", "first", "singular", "poteram", "I was able"),
                             ("imperfect", "second", "singular", "poteras", "you were able"),
                             ("imperfect", "third", "singular", "poterat", "he was able"),
                             ("imperfect", "first", "plural", "poteramus", "we were able"),
                             ("imperfect", "second", "plural", "poteratis", "you all were able"),
                             ("imperfect", "third", "plural", "poterant", "they were able"))


class LatinNoun:
    def __init__(self, lexical_entry):
        pass