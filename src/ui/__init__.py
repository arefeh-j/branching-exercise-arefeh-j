class ConsoleUI:
    def display_menu(self):
        print("=== Branching Exercise App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def get_user_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(f"[INFO] {message}")