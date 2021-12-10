



def check(prompt='', type=int):
    Incorrect = True
    while Incorrect:
        try:
            user_input = type(input(prompt))
        except ValueError:
            print(f'Invalid! Input should be {type}. Please Re-enter.')
            continue
        else:
            return user_input