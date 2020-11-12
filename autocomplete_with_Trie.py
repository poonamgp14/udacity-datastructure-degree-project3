## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        pass

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffix_list = []

        self._suffix_recursive(suffix,suffix_list)
        return suffix_list

    def _suffix_recursive(self, suffix, suffix_list):

        for char in self.children:
            if self.children[char].is_word:
                suffix_list.append(suffix+char)
                if len(self.children[char].children) > 0:
                    suffix += char
                    self.children[char]._suffix_recursive(suffix, suffix_list)
            else:
                self.children[char]._suffix_recursive(suffix+char, suffix_list)



## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod", "victory"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('String is empty.Please provide a string with atleast one character')
f('f');
# actory
# un
# unction
f('v')
# ictory
f('')
# String is empty.Please provide a string with atleast one character
f('u')
# u not found
