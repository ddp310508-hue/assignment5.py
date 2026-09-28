import re

def check_string_regex(user_input):
    """
    Checks if a string contains only a-z, A-Z, and 0-9 using Regular Expressions.
    """
    # Pattern explanation: 
    # ^ ensures match starts at beginning, $ ensures match goes to the end
    # [a-zA-Z0-9]+ checks for one or more alphanumeric characters
    pattern = r"^[a-zA-Z0-9]+$"
    
    if re.match(pattern, user_input):
        return True
    else:
        return False

# Main program block
if __name__ == "__main__":
    print("--- Alphanumeric String Checker ---")
    
    # Accept input string from the user
    user_string = input("Enter a string to check: ")
    
    # Handle empty string edge case
    if not user_string:
        print("Input cannot be empty.")
    else:
        # Check using the regex function
        if check_string_regex(user_string):
            print(f"Success: The string '{user_string}' contains ONLY valid characters (a-z, A-Z, 0-9).")
        else:
            print(f"Invalid: The string '{user_string}' contains unauthorized special characters or spaces.")

  #Output:
  #Scenario 1: Valid Alphanumeric Input
  #--- Alphanumeric String Checker ---
  #Enter a string to check: Student2026
  #Success: The string 'Student2026' contains ONLY valid characters (a-z, A-Z, 0-9).
  #Scenario 2: Invalid Input (Contains Special Characters or Spaces)
  #text--- Alphanumeric String Checker ---
  #Enter a string to check: Hello @ World!
  #Invalid: The string 'Hello @ World!' contains unauthorized special characters or spaces.
  #Scenario 3: Empty Input (Pressing Enter without typing)
  #--- Alphanumeric String Checker ---
  #Enter a string to check: 
  #Input cannot be empty.
