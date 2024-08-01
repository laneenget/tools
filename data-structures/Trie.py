# Also known as a prefix tree, it is used for efficient
# retrieval of key-value pairs. It is commonly used for
# implementing dictionaries and autocomplete features,
# making it a fundamental componenet in many search algorithms

# A trie is more advantagous than a hash table in how
# it can efficiently do a prefix search, easily print all
# words in alphabetical order, has no overhead of hash
# functions, and searching for a string can be done in O(n)
# time.

class TrieNode:

    def __init__(self):
        self.child_node = [None] * 26
        self.word_count = 0

class Trie:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return True if self.root is None else False

    def insert(self, root, key):

        current_node = root

        for c in key:

            # Check if the node exists for the current character
            # is in the Trie
            if current_node.child_node[ord(c) - ord('a')] == None:

                newNode = TrieNode()
                current_node.child_node[ord(c) - ord('a')] = newNode

            current_node = current_node.child_node[ord(c) - ord('a')]

        current_node.word_count += 1

    def is_prefix(self, root, key):

        current_node = root

        for c in key:
            if current_node.child_node[ord(c) - ord('a')] is None:
                return False
            
            current_node = current_node.child_node[ord(c) - ord('a')]

        return True
    
    def search_key(self, root, key):

        current_node = root

        for c in key:
            if current_node.child_node[ord(c) - ord('a')] is None:
                return False
            current_node = current_node.child_node[ord(c) - ord('a')]

        return current_node.word_count > 0
    
    def delete_key(self, root, word):

        current_node = root
        last_branch_node = None
        last_branch_char = 'a'

        for c in word:
            if not current_node.child_node[ord(c) - ord('a')]:
                return False
            else:
                count = 0

                for i in range(26):
                    if current_node.child_node[i]:
                        count += 1

                if count > 1:
                    last_branch_node = current_node
                    last_branch_char = c

                current_node = current_node.child_node[ord(c) - ord('a')]

        count = 0

        for i in range(26):
            if current_node.child_node[i]:
                count += 1

        if count > 0:
            current_node.word_count -= 1
            return True
        
        if last_branch_node:
            last_branch_node.child_node[ord(last_branch_char) - ord('a')] = None
            return True
        else:
            root.child_node[ord(word[0]) - ord('a')] = None
            return True