from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False

class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, character):
        return ord(character) - ord('a')

    def insert(self, word):
        root = self.root
        word_length = len(word)
        for i in range(word_length):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        root.terminating = True

    def search(self, word):
        root = self.root
        word_length = len(word)
        for i in range(word_length):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)
        return True if root and root.terminating else False     

if __name__ == '__main__':
    data = ['imran', 'rakib', 'imon', 'Iran', 'Rasel', 'Remon']
    trie = Trie()
    for datum in data:
        # inset datum into trie data structure.
        trie.insert(datum)
    
    print(trie.search('rakib'))
    print(trie.search('ashik'))
