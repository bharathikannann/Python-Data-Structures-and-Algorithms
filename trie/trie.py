# Trie Node
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")   # Root node 
    
    # Add words to trie
    def add(self, word):
        curr_node = self.root   # Keep track of current node
        for letter in word:   # Add every letter if current node children doesn't have that letter
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node =  curr_node.children[letter]
        curr_node.is_end_of_word = True   # Mark as end of word
    
    # Search elements in trie
    def search(self, word):
        if word == "":   # Empty string always exists
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:   # If letter is not present
                return False
            curr_node = curr_node.children[letter] # Update current node
        return curr_node.is_end_of_word
    
    # TO display all words in trie
    def show(self, node, word):
        if node.is_end_of_word:   # If end of word print the word
            print(word, end =" ")
        for l,n in node.children.items():   # Traverse for all the children in the node
            self.show(n, word + l)          # L -> Current letter, N -> Next node

if __name__ == "__main__":
    trie = Trie()
    words = ["wait", "waiter", "shop", "shopper"]
    for word in words:
        trie.add(word)
    print(trie.search("wait"))
    print(trie.search("waiter"))
    print(trie.search(""))
    print(trie.search("wai"))
    trie.show(trie.root, "")
    '''
    Output
    True
    True
    True
    False
    wait waiter shop shopper 
    '''