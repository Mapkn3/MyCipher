ru_alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_alphabet = ' abcdefghijklmnopqrstuvwxyz'

def crypt(text, key):
    raw = ''.join(str(key.find(i)) for i in text)[::-1]
    res = []
    while raw:
        k = 2 if raw[0] != '0' and int(raw[:2]) < len(key) else 1
        res.append(en_alphabet[int(raw[:k])])
        raw = raw[k:]
    return ''.join(res)
    

text = input('Enter text: ')
cr = crypt(text, en_alphabet)
orig = crypt(cr, en_alphabet)
print(cr, orig, sep='->')
