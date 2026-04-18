data = {}

again = True

while again:
    name = input('What is your name ?: ')
    price = int(input("What's your bid?: € "))
    data[name] = price

    print('\n' * 100)

    should_continue = input('Are there another users who want to bid ? Type "Yes" if yes, or "no" if not: ').lower()
    if should_continue == 'no':
        again = False

