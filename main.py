def find_highest_bidder(bidding_dictionary):

    first_key = list(bidding_dictionary)[0]
    winner = first_key
    highest_bid = bidding_dictionary[first_key]

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    return winner, highest_bid

data = {}

again = True

while again:
    name = input('What is your name ?: ')
    price = int(input("What's your bid?: € "))
    data[name] = price
    should_continue = input('Are there another users who want to bid ? Type "Yes" if yes, or "no" if not: ').lower()

    print('\n' * 100)

    if should_continue == 'no':
        again = False

winner, amount = find_highest_bidder(data)
print(f'Winner is {winner} with {amount}€')
