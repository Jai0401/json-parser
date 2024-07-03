from constants import *

def lex_string(string):
    if string[0] != '"':
        return None, string

    string = string[1:]
    json_string = ''
    while string[0] != '"':
        json_string += string[0]
        string = string[1:]

    return json_string, string[1:]

def lex_number(string):
    number_chars=['0','1','2','3','4','5','6','7','8','9','.','e','+','-']
    number = ''
    while string[0] in number_chars:
        number += string[0]
        string = string[1:]
    if not len(number):
        return None, string
    if '.' in number:
        return float(number), string
    return int(number), string

def lex_bool(string):
    string_len = len(string)
    if string_len >= TRUE_LEN and \
       string[:TRUE_LEN] == 'true':
        return True, string[TRUE_LEN:]
    elif string_len >= FALSE_LEN and \
         string[:FALSE_LEN] == 'false':
        return False, string[FALSE_LEN:]

    return None, string

def lex_null(string):
    string_len = len(string)
    if string_len >= 4 and \
       string[:4] == 'null':
        return True, string[4:]
    return None, string


def lex(string):
    tokens = []

    while len(string):
        json_string, string = lex_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue
        json_bool, string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue
        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue
        
        if string[0] in JSON_WHITESPACE:
            string = string[1:]
        elif string[0] in JSON_SYNTAX:
            tokens.append(string[0])
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(string[0]))

    return tokens
