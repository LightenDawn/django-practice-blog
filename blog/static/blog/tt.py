def change(txt):
    tmpline = []
    for line in txt.split('\n'):
        if len(line) < 1: continue
        tmpline.append(line)
        print(line)
    print(''.join(tmpline))

control_code = '''
    47, 210, [2, 1, 5], 0
    150, 210, [1.5, 1.5], 1
    109, 210, [1.5, 1], 1
'''

change(control_code)