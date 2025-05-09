class PokemonBinderManager:
    

    def __init__(self):
        """Initialize an empty binder."""
        self.pokemon_binder = {}  
        self.total_slots_per_page = 64  
        self.max_pokedex = 1025  

    def add_pokemon(self):
        
        try:
            pokedex_num = int(input(f"Enter Pokedex number (1-{self.max_pokedex}): "))
            
            if pokedex_num < 1 or pokedex_num > self.max_pokedex:
                print(f"Invalid! Enter a number between 1 and {self.max_pokedex}.")
                return
            
            if pokedex_num in self.pokemon_binder:
                print(f"Pokedex #{pokedex_num} is already in the binder!")
                return

        
            page = (pokedex_num - 1) // self.total_slots_per_page + 1
            position_within_page = (pokedex_num - 1) % self.total_slots_per_page
            row = (position_within_page // 8) + 1
            col = (position_within_page % 8) + 1

            self.pokemon_binder[pokedex_num] = (page, row, col)
            print(f"\nPage: {page}")
            print(f"Position: Row {row}, Column {col}")
            print(f"Status: Added Pokedex #{pokedex_num} to binder\n")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def view_binder(self):
        """Display all Pokémon in the binder."""
        print("\nCurrent Binder Contents:")
    

        if not self.pokemon_binder:
            print("The binder is empty.")
        else:
            for pokedex_num, (page, row, col) in sorted(self.pokemon_binder.items()):
                print(f"Pokedex #{pokedex_num}:")
                print(f"Page: {page}")
                print(f"Position: Row {row}, Column {col}\n")

    def reset_binder(self):
        """Reset all entries in the binder."""
        confirm = input("WARNING: This will DELETE all Pokémon! Type 'CONFIRM' to reset, or 'EXIT' to cancel: ")
        if confirm.upper() == "CONFIRM":
            self.pokemon_binder.clear()
            print("\nThe binder reset was successful! All cards have been removed.\n")
        elif confirm.upper() == "EXIT":
            print("\nReturning to the Main Menu.\n")
        else:
            print("\nInvalid input.\n")

    def run(self):
        """Main menu loop."""
        while True:
            print("\nMain Menu:")
            print("1. Enter Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")

            choice = input("Select option: ")

            if choice == "1":
                self.add_pokemon()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.view_binder()
            elif choice == "4":
                print("Exiting Pokemon Card Binder Manager.")
                break
            else:
                print("Invalid choice! Please try again.")
def run_game():
    pokemon = PokemonBinderManager()
    pokemon.run()

if __name__ == "__main__":
    run_game()
      
