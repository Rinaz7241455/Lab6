# Лабораторная работа № 6. Вариант 8: «Строки»
# Функции WordCount, Reverse, ToUpperFirst, IsPalindrome (ввод, обработка, вывод)

def input_text() -> str:
    """Функция ввода: запрашивает исходную строку у пользователя."""
    return input("Введите строку для обработки: ")

def word_count(text: str) -> int:
    """Возвращает количество слов в строке."""
    return len(text.split())

def reverse_str(text: str) -> str:
    """Возвращает строку, записанную в обратном порядке."""
    return text[::-1]

def to_upper_first(text: str) -> str:
    """Делает первый символ строки заглавным."""
    return text[:1].upper() + text[1:]

def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом без учёта регистра и пробелов."""
    cleaned: str = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

def print_results(text: str, words: int, rev: str, upper: str, pal: bool) -> None:
    """Функция вывода: печатает результаты всех преобразований с пояснениями."""
    verdict: str = "Да" if pal else "Нет"
    print("\n--- Результаты модульной обработки строки ---")
    print(f"Исходная строка: «{text}»")
    print(f"Количество слов (WordCount): {words}")
    print(f"Реверс строки (Reverse): «{rev}»")
    print(f"С заглавной буквы (ToUpperFirst): «{upper}»")
    print(f"Палиндром (IsPalindrome): {verdict}")

def main() -> None:
    """Главная функция: связывает этапы ввода, обработки и вывода без глобальных переменных."""
    src: str = input_text()
    print_results(src, word_count(src), reverse_str(src), to_upper_first(src), is_palindrome(src))

if __name__ == "__main__":
    main()
