"Проект для 'ЯМП'а: компактный кодировщик шифра цезаря"

ru_alphabet ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def ceasar_ciper(text:str, shift:int):
    "Шифрование и расшифрование(для дешифровки передаем открицательный shift)"
    res=[]
    for c in text:
        if c.lower() in ru_alphabet:
            idx = (ru_alphabet.index(c.lower()) + shift) % 33
            res.append(ru_alphabet[idx])
        else:
            res.append(c)
    return "".join(res)

print(ceasar_ciper("воздухан", 5))