class Parent:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


reagan = Parent("Reagan", None)
g_h_bush = Parent("G. H. Bush", reagan)
clinton = Parent("Clinton", g_h_bush)
g_w_bush = Parent("G. W. Bush", clinton)
obama = Parent("Obama", g_w_bush)
trump = Parent("Trump", obama)

trump2 = Parent("Trump2", trump)
biden = Parent("Trump", trump)

print(g_w_bush.parent)

person = biden
while person.parent is not None:
    print(person.name)
    person = person.parent