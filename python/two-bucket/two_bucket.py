#!/usr/bin/env python
#encoding=utf8

def check_forbidden(state, **kwargs):
    if kwargs['start'] == "one":
        return state if state != (0, kwargs['size_two']) else False
    else:
        return state if state != (kwargs['size_one'], 0) else False

def fill_one(*args, **kwargs):
    if kwargs['one'] == kwargs['size_one']:
        return False
    return check_forbidden((kwargs['size_one'], kwargs['two']), **kwargs)

def fill_two(*args, **kwargs):
    if kwargs['two'] == kwargs['size_two']:
        return False
    return check_forbidden((kwargs['one'], kwargs['size_two']), **kwargs)

def empty_one(**kwargs):
    if kwargs['one'] == 0:
        return False
    return check_forbidden((0, kwargs['two']), **kwargs)

def empty_two(**kwargs):
    if kwargs['two'] == 0:
        return False
    return check_forbidden((kwargs['one'], 0), **kwargs)

def one_to_two(*args, **kwargs):
    if kwargs['one'] == 0 or kwargs['two'] == kwargs['size_two']:
        return False

    if kwargs['size_two'] - kwargs['two'] >= kwargs['one']:
        state = (0, kwargs['one'] + kwargs['two'])
    else:
        state = (
            kwargs['one'] + kwargs['two'] - kwargs['size_two'],
            kwargs['size_two'],
        )
    return check_forbidden(state, **kwargs)

def two_to_one(*args, **kwargs):
    if kwargs['two'] == 0 or kwargs['one'] == kwargs['size_one']:
        return False

    if kwargs['size_one'] - kwargs['one'] >= kwargs['two']:
        state = (kwargs['two'] + kwargs['one'], 0)
    else:
        state = (
            kwargs['size_one'],
            kwargs['one'] + kwargs['two'] - kwargs['size_one'],
        )
    return check_forbidden(state, **kwargs)


def measure(size_one, size_two, goal, start):
    start_state = (size_one, 0) if start == "one" else (0, size_two)
    cache = {start_state: ["init"]}

    operations = [
        fill_one, fill_two, two_to_one, one_to_two, empty_one, empty_two,
    ]

    while True:
        new_states = {}
        for state in cache:
            kwargs = {
                "one": state[0], "two": state[1], "start": start,
                "size_one": size_one, "size_two": size_two,
            }
            #print("state", state)
            for operation in operations:
                new_state = operation(**kwargs)
                if (not new_state) or (new_state in cache):
                    #print("bad new state", operation.__name__, new_state)
                    continue
                #print("good new state", operation.__name__, new_state)
                new_states[new_state] = cache[state] + [operation.__name__]
        if not new_states:
            raise ValueError("no solution found")
        cache.update(new_states)
        if any(goal in item for item in cache):
            item = [item for item in cache if goal in item][0]
            if item[0] == goal:
                return len(cache[item]), "one", item[1]
            else:
                return len(cache[item]), "two", item[0]
