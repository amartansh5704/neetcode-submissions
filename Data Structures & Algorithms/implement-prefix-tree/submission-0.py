class PrefixTree:

    def __init__(self):
        self.children = defaultdict(PrefixTree)        

    def insert(self, word: str, i: int = 0) -> None:
        if i < len(word):
            self.children[word[i]].insert(word, i+1)
        else:
            self.children['']

    def search(self, word: str, i: int = 0) -> bool:
        if i < len(word):
            return word[i] in self.children and self.children[word[i]].search(word, i+1)
        else:
            return '' in self.children        

    def startsWith(self, prefix: str, i: int = 0) -> bool:
        if i < len(prefix):
            return prefix[i] in self.children and self.children[prefix[i]].startsWith(prefix, i+1)
        else:
            return len(self.children) > 0
        
        