# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes_helper(self, prefix):
        # Recursive help function gets all complete words with prefix
        results = []
        if self.is_word:
            results.append(prefix)
        for (value, child) in self.children.items():
            results.extend(child.suffixes_helper(prefix + value))
        return results

    def suffixes(self, prefix):
        # function to remove prefixes from complete words
        r = self.suffixes_helper(prefix)
        result = []
        for item in r:
            result.append(item[len(prefix):])
        return result

    # Recursive function that collects the suffix for
    # all complete words below this point


# Add a child node in this Trie

# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Initialize this Trie (add a root node)

    def insert(self, word):
        if word is None:
            return -1

        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    # Add a word to the Trie

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children.keys():
                return None
            current_node = current_node.children[char]

        return current_node


# Find the Trie node that represents this prefix


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes(prefix)))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')


print(MyTrie.find('an').suffixes('an'))
'''
Test case 1:
Test if the word is None, then the result should be -1.
'''
print(MyTrie.insert(None))

'''
Test case 2:
Test if the find function is work, then the result should return the node that contains the last character of this prefix.
'''
print(MyTrie.find('an'))


'''
Test case 3:
Test if the suffixes function is work, then the result should be ["t", "thology", "tagonist", "tonym"].
'''
print(MyTrie.find('an').suffixes('an'))