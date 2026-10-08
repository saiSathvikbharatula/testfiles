class Application:
    def connect_database(self): print("database connected")
    def create_user(self, name): print("creating user", name)
    def send_email(self, address): print("sending email", address)
    def generate_report(self): print("generating report")
    def save_report(self, report): print("saving report")
    def export_csv(self, report): print("exporting csv")
    def calculate_salary(self, salary): return salary * 12
    def render_html(self, title): return "<h1>" + title + "</h1>"
    def log_event(self, message): print("LOG:", message)
    def backup_database(self): print("backup complete")
    def authenticate(self, username, password): return username == "admin" and password == "admin"

def helper(): return "helper"

app = Application()
print(app.render_html("Dashboard"))
print(app.calculate_salary(50000))
