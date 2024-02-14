# This program stores information about reagents in a lab

# Define a dictionary to hold the information about each reagent
reagents = {}

# Define a function to add a new reagent to the dictionary
def add_reagent(name, amount, temperature):
  # Add a new entry to the dictionary, using the reagent name as the key
  reagents[name] = {
    "amount": amount,
    "temperature": temperature
  }

# Define a function to retrieve the information about a reagent
def get_reagent(name):
  if name in reagents:
    # If the reagent exists, print its information
    r = reagents[name]
    print(f"Reagent '{name}':")
    print(f"  Amount: {r['amount']}")
    print(f"  Temperature: {r['temperature']}")
  else:
    # If the reagent does not exist, print an error message
    print(f"Error: Reagent '{name}' not found.")

# Test the program by adding some reagents and printing their information
add_reagent("PBS", 1000, 4)
add_reagent("Triton X-100", 100, -20)
get_reagent("PBS")
get_reagent("Triton X-100")
