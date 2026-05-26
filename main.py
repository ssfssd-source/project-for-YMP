RU_REF_FREQS = {
    'о': 10.97, 'е': 8.45, 'а': 8.01, 'и': 7.35, 'н': 6.70, 'т': 6.26, 'с': 5.47, 
    'р': 4.73, 'в': 4.54, 'л': 4.40, 'к': 3.49, 'м': 3.21, 'д': 2.98, 'п': 2.81, 
    'у': 2.62, 'я': 2.01, 'ы': 1.90, 'ь': 1.74, 'г': 1.70, 'з': 1.65, 'б': 1.59, 
    'ч': 1.44, 'й': 1.21, 'х': 0.97, 'ж': 0.94, 'ш': 0.73, 'ю': 0.64, 'ц': 0.48, 
    'щ': 0.36, 'э': 0.32, 'ф': 0.26, 'ъ': 0.04, 'ё': 0.04
}
RU_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def caesar_cipher(text:str, shift:int):
    """Шифрование и расшифрование (для дешифровки передаем отрицательный shift)"""
    res = []
    for c in text:
        if c.lower() in RU_ALPHABET:
            idx = (RU_ALPHABET.index(c.lower()) + shift) % 33
            res.append(RU_ALPHABET[idx].upper() if c.isupper() else RU_ALPHABET[idx])
        else:
            res.append(c)
    return "".join(res)

def auto_decrypt(text:str) -> str:
    """Взлом частотным анализом по метрике наименьших квадратов"""
    chars = [c.lower() for c in text if c.lower() in RU_ALPHABET]
    if not chars: 
        return None
    
    # Расчет частот букв в тексте
    freqs = {c: (chars.count(c) / len(chars)) * 100 for c in RU_ALPHABET}
    
    res = []
    for s in range(33):
        # Вычисляем квадратичное отклонение от эталона для текущего сдвига
        dev = sum((freqs[RU_ALPHABET[i]] - RU_REF_FREQS[RU_ALPHABET[(i - s) % 33]])**2 for i in range(33))
        res.append((s, dev))
        
    res.sort(key=lambda x: x[1])  # Сортировка по возрастанию отклонения
    return res[0][0], caesar_cipher(text, -res[0][0]), res[:3]

def get_int(prompt):
    """Отказоустойчивый ввод целого числа"""
    while True:
        try: return int(input(prompt))
        except ValueError: print("Ошибка: нужно ввести целое число!")

def main():
    while True:
        print("\n1. Зашифровать\n2. Расшифровать\n3. Авто-взлом\n4. Выход")
        choice = input("Выбор: ").strip()
        if choice == '4': break
        if choice not in ('1', '2', '3'): continue
        
        text = input("Введите текст: ")
        if not text.strip(): 
            print("Текст пустой!"); continue
            
        if choice == '1':
            print("\nРезультат:", caesar_cipher(text, get_int("Сдвиг: ")))
        elif choice == '2':
            print("\nРезультат:", caesar_cipher(text, -get_int("Сдвиг: ")))
        elif choice == '3':
            out = auto_decrypt(text)
            if not out: 
                print("Нет русских букв для анализа!"); continue
            print(f"\nПодобранный сдвиг: {out[0]}\nРезультат: {out[1]}")

if __name__ == "__main__":
    main()