# Final Exam AIDI 2004 - Hamza-El-Hilali

class InventoryTracker:
    def addItem(self, name, quantity):
        """Add an item to the inventory"""
        print(f"Added {quantity} of {name} to inventory")

    def updateStock(self, item_name, new_quantity):
        """Update the quantity of an existing item in the inventory"""
        print(f"Updated {item_name} quantity to {new_quantity}")
