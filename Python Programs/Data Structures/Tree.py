class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        level = self.get_level()
        intendation = "" + (" " * level * 3) + "|__"
        print(intendation + str(self.data))
        for child in self.children:
            child.print_tree()

    def get_level(self):
        count = 0
        while self.parent:
            self = self.parent
            count += 1
        return count


if __name__ == "__main__":
    root = Tree("Electronics")

    laptop = Tree("Laptops")
    laptop.add_child(Tree("Alien Ware"))
    laptop.add_child(Tree("Predator"))
    laptop.add_child(Tree("RoG"))

    mobile = Tree("Mobiles")
    mobile.add_child(Tree("Poco"))
    mobile.add_child(Tree("Pixels"))
    mobile.add_child(Tree("Samsung"))

    tv = Tree("TV")
    tv.add_child(Tree("MI"))
    tv.add_child(Tree("One Plus"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)
    root.print_tree()
