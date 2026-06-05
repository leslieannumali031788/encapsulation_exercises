from pet_run import Pet
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

if __name__ == "__main__":


    print(f"{CYAN} Pet Profile")
    input_name = input("Enter your pet's name: ")
    input_type = input("Enter your pet's type: ")
    input_age = input("Enter your pet's age: ")

    my_pet = Pet()