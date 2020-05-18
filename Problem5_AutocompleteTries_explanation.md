Problem:

Given a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Explanation:

For this problem, I use the codes from class to build Trie. Then
I use recursion method for suffixes part in TrieNode class. Thus, the time
complex is O(nlog(n)) and the space complex is O(n).

