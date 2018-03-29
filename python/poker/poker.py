#!/usr/bin/env python
#encoding=utf8

ORDERS = {str(i): i for i in range(2, 11)}

ORDERS.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})


class Card(object):
    def __init__(self, desc):
        self.desc = desc
        self.order = ORDERS[desc[:-1]]
        self.suit = desc[-1]

    def __repr__(self):
        return '<Card: {}>'.format(self.desc)


class Hand(object):
    def __init__(self, desc):
        self.cards = [Card(c) for c in desc.split()]
        self._rating = None
        self.rank = None
        self.desc = desc

    def __lt__(self, hand):
        if self.rating == hand.rating:
            return self.rank > hand.rank
        return self.rating < hand.rating

    def __eq__(self, hand):
        return self.rating == hand.rating and self.rank == hand.rank

    def __repr__(self):
        return '<Hand: {}>'.format(self.desc)

    @property
    def rating(self):
        if self._rating is None:
            self._rating, self.rank = self.get_rating()
            self._rating = int(self._rating)
        return self._rating

    def get_rating(self):
        tests = [attr for attr in dir(self) if attr.startswith("rate")]
        tests.sort()
        for test in tests:
            status, rank = getattr(self, test)()
            if status:
                return (test.split("_")[1], rank)
        return "999.99"

    # Helpers
    @property
    def orders(self):
        return list(sorted([c.order for c in self.cards], reverse=True))

    @property
    def suits(self):
        return list(sorted(c.suit for c in self.cards))

    @property
    def is_flush(self):
        return len(set(self.suits)) == 1

    def is_straight(self):
        has_A = 14 in self.orders
        min_ = min(self.orders)
        if not has_A:
            return all((min_ + i) in self.orders for i in range(5)), min_

        if all((min_ + i) in self.orders for i in range(5)):
            return True, min_
        elif set(self.orders) == set([2, 3, 4, 5, 14]):
            return True, 1
        else:
            return False, None

    # Raters
    def rate_1_straight_flush(self):
        if not self.is_flush:
            return False, None

        is_straight, min_ = self.is_straight()
        if not is_straight:
            return False, None
        else:
            return True, [min_]

    def rate_2_four_of_a_kind(self):
        if len(set(self.orders)) != 2:
            return False, None
        order = self.orders[0]
        order_count = len([c for c in self.cards if c.order == order])
        if order_count == 1:
            return True, [self.orders[-1], order]
        elif order_count == 4:
            return True, [order, self.orders[-1]]
        else:
            return False, None

    def rate_3_full_house(self):
        if len(set(self.orders)) != 2:
            return False, None
        order = self.orders[0]
        order_count = len([c for c in self.cards if c.order == order])
        if order_count == 2:
            return True, [self.orders[-1], order]
        elif order_count == 3:
            return True, [order, self.orders[-1]]
        else:
            return False, None

    def rate_4_flush(self):
        return self.is_flush, self.orders

    def rate_5_straight(self):
        is_straight, min_ = self.is_straight()
        if not is_straight:
            return False, None
        else:
            return True, [min_]

    def rate_6_three_of_a_kind(self):
        if len(set(self.orders)) != 3:
            return False, None
        for order in self.orders:
            if len([c for c in self.cards if c.order == order]) == 3:
                return True, [order] + list(set(self.orders) - set([order]))
        return False, None

    def rate_7_two_pairs(self):
        if len(set(self.orders)) != 3:
            return False, None
        pairs = set([
            order for order in self.orders
            if len([c for c in self.cards if c.order == order]) == 2
        ])
        single = [
            order for order in self.orders
            if len([c for c in self.cards if c.order == order]) != 2
        ]
        return len(pairs) == 2, [max(pairs), min(pairs), single[0]]

    def rate_8_one_pair(self):
        if len(set(self.orders)) != 4:
            return False, None
        pairs = set([
            order for order in self.orders
            if len([c for c in self.cards if c.order == order]) == 2
        ])
        single = [
            order for order in self.orders
            if len([c for c in self.cards if c.order == order]) != 2
        ]
        return len(pairs) == 1, [list(pairs)[0], sorted(single, reverse=True)]

    def rate_9_high_card(self):
        return True, self.orders


def best_hands(hands):
    hands = [Hand(hand) for hand in hands]
    hands.sort()
    bests = [hands[0]]
    for hand in hands[1:]:
        if hand == bests[0]:
            bests.append(hand)
    return [hand.desc for hand in bests]
