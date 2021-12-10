def check(prompt='', type=int):
    Incorrect = True
    while Incorrect:
        try:
            user_input = type(input(prompt))
        except ValueError:
            print(f'Invalid! --- Should be {type}.')
            continue
        else:
            return user_input