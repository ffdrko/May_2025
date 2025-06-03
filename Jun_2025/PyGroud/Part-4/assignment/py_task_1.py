def get_age(year_of_birth, current_year=2025):
    user_age = current_year - year_of_birth
    return user_age

user_main_age =  get_age(1998)

print(f"The user age is {user_main_age}")