#!/usr/bin/env python
#encoding=utf8

ACTIONS = {
    "wink": 1,
    "double blink": 2,
    "close your eyes": 4,
    "jump": 8,
}


def handshake(code):
    if code < 0 or code > 32:
        raise ValueError("Won't work.")

    reverse = False
    if code > 15:
        code -= 16
        reverse = True

    actions = []
    while code:
        if code >= 8:
            actions.append("jump")
            code -= 8
        elif code >= 4:
            actions.append("close your eyes")
            code -= 4
        elif code >= 2:
            actions.append("double blink")
            code -= 2
        elif code:
            actions.append("wink")
            code -= 1

    if reverse:
        return actions
    return list(reversed(actions))


def secret_code(actions):
    numbers = [ACTIONS[action] for action in actions]
    reverse = sorted(numbers) != numbers
    sum_ = sum(ACTIONS[action] for action in actions)
    if reverse:
        sum_ += 16
    return sum_
