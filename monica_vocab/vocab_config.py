class Vocab_Obj:
    def __init__(self, vocab, chinese = None, pos = None, familiarity = None):
        self.vocab = vocab
        self.chinese = chinese
        self.pos = pos
        self.familiarity = familiarity
    def print_info(self):
        print("word: "+ (self.vocab if self.vocab is not None else "None"))
        print("chinese: "+ (self.chinese if self.chinese is not None else "None"))
        print("part-of-speech: "+ (self.pos if self.pos is not None else "None"))
        print("familiarity: "+ (self.familiarity if self.familiarity is not None else "None"))
        return