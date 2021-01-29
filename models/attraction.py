class Attraction:

    def __init__(self, name, category, city, entry_fee = False, id = None):
        self.name = name 
        self.category = category 
        self.city = city 
        self.entry_fee = entry_fee
        self.id = id  

    
    def mark_paid_entry(self):
        self.entry_fee = True