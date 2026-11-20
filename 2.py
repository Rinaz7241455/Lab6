# Контрольный пример (Фотография 2)
# Проверка на фразе «а роза упала на лапу Азора»

src = "а роза упала на лапу Азора"
words = len(src.split())
rev = src[::-1]
upper = src[:1].upper() + src[1:]
cleaned = "".join(ch.lower() for ch in src if ch.isalnum())
verdict = "Да" if cleaned == cleaned[::-1] else "Нет"

print("--- Результаты модульной обработки строки ---")
print(f"Исходная строка: «{src}»")
print(f"Количество слов (WordCount): {words}")
print(f"Реверс строки (Reverse): «{rev}»")
print(f"С заглавной буквы (ToUpperFirst): «{upper}»")
print(f"Палиндром (IsPalindrome): {verdict}")
