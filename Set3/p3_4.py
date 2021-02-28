debt_dict = {
    'Joe': [5, 7],
    'Denny': [20],
    'Nick': [8, 20],
    'Bryson': [10]
}

def lend_money(debts, person, amount):
    if person in debts:
        debts[person].append(amount)
    else:
        debts[person] = [amount]
    return None

def amount_owed_by(debts, person):
    amount_from_person = 0

    if person not in debts:
        return 0
    else:
        for values in debts[person]:
            amount_from_person += values
        return amount_from_person

def total_amount_owed(debts):
    amount = 0

    for i in debts:
        for j in debts[i]:
            amount += j
    return amount