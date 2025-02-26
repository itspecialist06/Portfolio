import random
import string


def generate_password(length=12, use_digits=True, use_special_chars=True, use_uppercase=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    if not all_chars:
        return "Ошибка: Не выбраны символы для генерации пароля."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def generate_multiple_passwords(count=5, length=12, use_digits=True, use_special_chars=True, use_uppercase=True):
    return [generate_password(length, use_digits, use_special_chars, use_uppercase) for _ in range(count)]


if __name__ == "__main__":
    print("🔥 Добро пожаловать в Ультимативный Генератор Паролей! 🔥")
    length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
    use_digits = input("Включать цифры? (д/н, по умолчанию д): ").strip().lower() in ['д', 'да', '']
    use_special_chars = input("Включать специальные символы? (д/н, по умолчанию д): ").strip().lower() in ['д', 'да',
                                                                                                           '']
    use_uppercase = input("Включать заглавные буквы? (д/н, по умолчанию д): ").strip().lower() in ['д', 'да', '']
    count = int(input("Сколько паролей сгенерировать? (по умолчанию 1): ") or 1)

    passwords = generate_multiple_passwords(count, length, use_digits, use_special_chars, use_uppercase)
    print("\n🚀 Сгенерированные пароли:")
    for idx, pwd in enumerate(passwords, 1):
        print(f"{idx}. {pwd}")
    print("\n✅ Будьте в безопасности и используйте надежные пароли!")
