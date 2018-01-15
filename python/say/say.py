#!/usr/bin/env python
#encoding=utf8

ONES = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

TENS = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

TEENS = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

def under_1k(number):
    """say a number from 1 to 999"""
    output = ""
    hundreds, remains = divmod(number, 100)
    output = ONES[hundreds] + " hundred " if hundreds else ""
    tens, ones = divmod(remains, 10)
    if tens == 0:
        if ones:
            if output:
                return output + "and " + ONES[ones]
            else:
                return ONES[ones]
        else:
            return output
    elif tens == 1:
        if output:
            return output + "and " + TEENS[remains]
        else:
            return output + TEENS[remains]
    else:
        if output:
            output = output + "and "
        if ones:
            return output + TENS[tens * 10] + "-" + ONES[ones]
        else:
            return output + TENS[tens * 10]

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("bad number specified")
    elif number == 0:
        return 'zero'

    billions, b_modular = divmod(number, 1000000000)
    output = under_1k(billions) + " billion " if billions else ""

    millions, m_modular = divmod(b_modular, 1000000)
    if millions:
        output += under_1k(millions) + " million "

    kilos, k_modular = divmod(m_modular, 1000)
    if kilos:
        if billions and not under_1k(millions) and under_1k(kilos):
            output += "and "
        output += under_1k(kilos) + " thousand "

    if (billions or millions) and not under_1k(kilos) and under_1k(k_modular):
        output += "and "
    output += under_1k(k_modular)

    return output.strip()
