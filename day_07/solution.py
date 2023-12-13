from collections import defaultdict, Counter
from functools import cmp_to_key


f = [x for x in open("input.txt").read().strip().split("\n")]

# 5 / 4 / full house / 3 of a kind / 2 pair / one pair / high card

card_ordering = "AKQJT98765432"
p2_card_ordering = "AKQT98765432J"

hand_ordering = ["5", "4", "fh", "3", "2p", "2", "1"]

# print()

hand_bid_map = {}

def ordering_cmp(a, b):
    for la, lb in zip(a,b):
        if la != lb:
            return -1 if card_ordering.index(la) < card_ordering.index(lb) else 1

def ordering_cmp_p2(a, b):
    for la, lb in zip(a,b):
        if la != lb:
            return -1 if p2_card_ordering.index(la) < p2_card_ordering.index(lb) else 1




def solve_part_1():
    hands = defaultdict(list)
    for line in f:
        cards, bid = line.split(" ")
        bid = int(bid)
        c = Counter(cards)
        classify_hand(c, cards, hands)
        hand_bid_map[cards] = bid
    print(sort_and_process_hands(1, hands))

def solve_part_2():
    hands = defaultdict(list)
    for line in f:
        cards, bid = line.split(" ")
        bid = int(bid)
        c = Counter(cards)
        if all(k != "J" for k,v in c.items()):
            classify_hand(c, cards, hands)
        else:
            # there is a J, so just add Jcount to the highest count or the highest value card remaining
            handle_joker(c)
            classify_hand(c, cards, hands)
        hand_bid_map[cards] = bid
    print(sort_and_process_hands(2, hands))


def handle_joker(c):
    # sort by count and then secondary sort by highest value card remaining
    vals_in_desc_order = sorted(c.items(), key=lambda x: (x[1], p2_card_ordering[::-1].index(x[0])), reverse=True)
    index_of_J = [index for index, (first, _) in enumerate(vals_in_desc_order) if first == 'J'][0]
    if len(vals_in_desc_order) != 1: #if it's 1 then it's just Jokers.... so we don't need to do anything
        del vals_in_desc_order[index_of_J]
        first_elem = vals_in_desc_order[0]
        new_first_elem = (first_elem[0], first_elem[1] + c["J"])
        del vals_in_desc_order[0]
        vals_in_desc_order.insert(0, new_first_elem)
        c.clear()
        for k, v in vals_in_desc_order:
            c[k] = v


def classify_hand(c, cards, hands):
    if any(v == 5 for k, v in c.items()):
        hands["5"].append(cards)
    elif any(v == 4 for k, v in c.items()):
        hands["4"].append(cards)
    elif any(v == 3 for k, v in c.items()) and any(v == 2 for k, v in c.items()):
        hands["fh"].append(cards)
    elif any(v == 3 for k, v in c.items()) and not any(v == 2 for k, v in c.items()):
        hands["3"].append(cards)
    elif sum(v == 2 for k, v in c.items()) == 2:
        hands["2p"].append(cards)
    elif sum(v == 2 for k, v in c.items()) == 1 and not any(v == 3 for k, v in c.items()):
        hands["2"].append(cards)
    elif all(v == 1 for k, v in c.items()):
        hands["1"].append(cards)


def sort_and_process_hands(part, hands):
    if part == 1:
        for k in hands.keys():
            hands[k].sort(key=cmp_to_key(ordering_cmp), reverse=True)
    else:
        for k in hands.keys():
            hands[k].sort(key=cmp_to_key(ordering_cmp_p2), reverse=True)

    ret = []
    for hand in hand_ordering[::-1]:
        if hand in hands:
            ret.extend(hands[hand])

    ans = 0
    for index, hand in enumerate(ret):
        rank = index + 1
        b = hand_bid_map[hand]
        ans += (b * rank)
    return ans

solve_part_1()
solve_part_2()