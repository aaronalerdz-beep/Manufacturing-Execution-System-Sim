import re
def validation(var_valid = list):
       # here is the name
    for va in var_valid:
        print(va)
        if isinstance(va, str):
            MIN_LEN = 2
            MAX_LEN = 50
            if len(va) < MIN_LEN or len(va) > MAX_LEN:
                print(f"Error:  must be between {MIN_LEN} and {MAX_LEN} characters.")
                return False
            NAME_REGEX = r"^[.A-Za-z0-9\s'-]+$"
            if not re.fullmatch(NAME_REGEX, va):
                print("Error:  contains invalid characters (only letters, spaces, -, ' allowed).")
                return False
            if not va or not va.strip():
                print("Error:  cannot be empty.")
                return False
    return True        

    