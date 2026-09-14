class Product:
    def __init__(self, product_id, name, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Category: {self.category} | Price: ${self.price:.2f} | Stock: {self.stock_quantity}")

    def update_stock(self, quantity):
        if self.stock_quantity + quantity >= 0:
            self.stock_quantity += quantity
            print(f"Stock updated for {self.name}. New stock: {self.stock_quantity}")
        else:
            print(f"Error: Not enough stock for {self.name}. Available: {self.stock_quantity}, Requested reduction: {-quantity}")

    def calculate_total_price(self, quantity):
        if quantity > 0:
            return self.price * quantity
        return 0

    @staticmethod
    def is_valid_price(price):
        return price > 0

if __name__ == "__main__":
    print("Creating products...")
    product1 = Product(101, "Laptop", 1200.00, "Electronics", 15)
    product2 = Product(102, "Smartphone", 800.00, "Electronics", 50)
    product3 = Product(103, "Coffee Maker", 80.00, "Home Appliances", 30)
    product4 = Product(104, "Desk Chair", 150.00, "Furniture", 20)
    product5 = Product(105, "Notebook", 5.50, "Stationery", 200)

    products = [product1, product2, product3, product4, product5]

    for p in products:
        p.display_product()
        
    print("\n--- Testing Price Validation ---")
    print(f"Is 1200 a valid price? {Product.is_valid_price(1200)}")
    print(f"Is -50 a valid price? {Product.is_valid_price(-50)}")
    print(f"Is 0 a valid price? {Product.is_valid_price(0)}")

    print("\n--- Buying/Updating Stock Demonstration ---")
    # Buy 2 Laptops
    quantity_to_buy = 2
    if product1.stock_quantity >= quantity_to_buy:
        total = product1.calculate_total_price(quantity_to_buy)
        print(f"Buying {quantity_to_buy} {product1.name}(s) for ${total:.2f}")
        product1.update_stock(-quantity_to_buy)
    
    # Restock Smartphones
    print(f"\nRestocking {product2.name}s by 20 units.")
    product2.update_stock(20)

    # Try to buy more Notebooks than available
    quantity_to_buy = 250
    print(f"\nAttempting to buy {quantity_to_buy} {product5.name}s...")
    product5.update_stock(-quantity_to_buy)

    print("\n--- Final Product States ---")
    for p in products:
        p.display_product()
