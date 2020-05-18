# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, handler, pieceOfPath):
        # Insert the node as before
        self.children[pieceOfPath] = RouteTrieNode(handler)



# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, handler, pieceOfPath):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root

        for piece in pieceOfPath:
            if piece not in current.children:
                current.children[piece] = RouteTrieNode(None)
            current = current.children[piece]

        current.handler = handler

    def find(self, pieceOfPath):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(pieceOfPath) == 0:
            return self.root.handler

        current = self.root
        for piece in pieceOfPath:
            if piece not in current.children:
                return None
            current = current.children[piece]
        return current.handler


class Router:

    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        self.route = RouteTrie(handler)
        self.route.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pieceOfPath = self.split_path(path)
        self.route.insert(handler, pieceOfPath)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        pieceOfPath = self.split_path(path)
        result = self.route.find(pieceOfPath)
        return result

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == '/':
            return []
        pieceOfPath = path.split('/')
        return pieceOfPath



# Here are some test cases and expected outputs you can use to test your implementation


'''
Test case 1:
Test if the length of path is 1, then the result should be 'root handler'.
'''
# create the router and add a route
router = Router("root handler")
router.add_handler("/", "root handler")  # add a route

# some lookups with the expected output
print("********** Test 1 ***********")
print(router.lookup("/")) # should print 'root handler'


'''
Test case 2:
Test if the multiple paths are work, then the result should be same as the common.
'''
router2 = Router("root handler")
router2.add_handler("/home/source/hello", "hello handler")
router2.add_handler("/home/source/udacity", "udacity handler")
router2.add_handler("/home/source/hello/world", "world handler")
print("********** Test 2 ***********")
print(router2.lookup("/")) # should print root handler
print(router2.lookup("/home/source/udacity")) # should print udacity handler
print(router2.lookup("/home/source/hello")) # should print hello handler
print(router2.lookup("/home/source/hello/world")) # should print world handler
print(router2.lookup("/home/sourc")) # should print None
print(router2.lookup("/home/sour")) # should print None


'''
Test case 3:
Test if the function is work, the the result should be same as the common.
'''
# create the router and add a route
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("********** Test 3 ***********")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print None
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print None
print(router.lookup("/home/about/me")) # should print None
