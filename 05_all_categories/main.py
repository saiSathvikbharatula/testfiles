class StoreManager:
    def save(self, item): print("saving", item)
    def send_email(self, email): print("email sent", email)
    def calculate(self, price, qty):
        if price < 0: return 0
        if qty < 0: return 0
        return price * qty

def process_order(price, qty):
    if price < 0: return 0
    if qty < 0: return 0
    return price * qty

def process_cart(price, qty):
    if price < 0: return 0
    if qty < 0: return 0
    return price * qty

try:
    value = open("config.txt").read()
except:
    value = ""

manager = StoreManager()
print(manager.calculate(10, 2))
