from lex import lex
from parse import parse
# Opening JSON file
f1 = open('tests/step1/invalid.json').read()
f2 = open('tests/step1/valid.json').read()
f3 = open('tests/step2/invalid.json').read()
f4 = open('tests/step2/valid.json').read()
f5 = open('tests/step2/invalid2.json').read()
f6 = open('tests/step2/valid2.json').read()
f7 = open('tests/step3/invalid.json').read()
f8 = open('tests/step3/valid.json').read()
f9 = open('tests/step4/invalid.json').read()
f10 = open('tests/step4/valid.json').read()
f11 = open('tests/step4/valid2.json').read()

for i in range(1, 12):
    print('Test case', i)
    try:
        tokens=lex(eval('f'+str(i)))
        parse(tokens)[0]
        print('Passed')
    except Exception as e:
        print(f'Error: {e} for test case {i}')


# tokens = lex(f11)
# print(tokens)
# print(parse(tokens)[0])