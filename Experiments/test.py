def calculate(years_of_birth , current_year = 2023):
    """Calculate age of people"""
    if years_of_birth > current_year:
        return "enter older year"
    return current_year - years_of_birth

def num_of_list(list_name):
    return len(list_name)

mylist = input("Enter the list").split(" ")
print(num_of_list(mylist))
