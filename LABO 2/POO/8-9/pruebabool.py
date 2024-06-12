class Casa():
    def __init__(self, num):
        self.num = num
        self.pile = True

    def change(self):
        self.pile = not self.pile
    
    def __str__(self):
        return f"Casa numero {self.num}, tiene pile?: {self.pile}"
    
casa1 = Casa(1)
casa1.change()
print(casa1)