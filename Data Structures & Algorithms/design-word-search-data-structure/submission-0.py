class TreeNode:
    def __init__(self) -> None:
        self.childrens = defaultdict(TreeNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.childrens[char]
        node.is_word = True        

    def search(self, word: str) -> bool:
        curr_nodes = [self.root]

        for char in word:
            next_nodes = []

            for node in curr_nodes:
                if char == ".":
                    next_nodes.extend(node.childrens.values())
                elif char in node.childrens:
                    next_nodes.append(node.childrens[char])
                
            curr_nodes = next_nodes

            if not curr_nodes:
                return False
        
        return any(node.is_word for node in curr_nodes)
        
