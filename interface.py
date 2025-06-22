from SEED import Encrypt, Decrypt, GenerateRoundKeys


def encrypt():
    text_file = input(
        "Введіть ім'я файлу зі значенням, яке потрібно зашифрувати: ").strip()
    key_file = input(
        "Введіть ім'я файлу з ключем шифрування: ").strip()
    ciphertext_file = input(
        "Введіть ім'я файлу, куди зберегти зашифроване значення: ").strip()

    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()
        text = int(text, 16)

    with open(key_file, 'r', encoding='utf-8') as f:
        key = f.read().strip()
        key = int(key, 16)

    round_keys = GenerateRoundKeys(key)
    ciphertext = Encrypt(text, round_keys)

    with open(ciphertext_file, 'w', encoding='utf-8') as f:
        f.write(hex(ciphertext)[2:])

    print(f"Зашифровано. Результат записано в '{ciphertext_file}'.")


def decrypt():
    ciphertext_file = input(
        "Введіть ім'я файлу з зашифрованим значенням: ").strip()
    key_file = input(
        "Введіть ім'я файлу з ключем шифрування: ").strip()
    text_file = input(
        "Введіть ім'я файлу, куди зберегти розшифрований текст: ").strip()

    with open(ciphertext_file, 'r', encoding='utf-8') as f:
        ciphertext = f.read().strip()
        ciphertext = int(ciphertext, 16)

    with open(key_file, 'r', encoding='utf-8') as f:
        key = f.read().strip()
        key = int(key, 16)

    round_keys = GenerateRoundKeys(key)
    text = Decrypt(ciphertext, round_keys)

    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(hex(text)[2:])

    print(f"Розшифровано. Результат записано в '{text_file}'.")


def main():
    print("Виберіть операцію:")
    print("1 — Зашифрувати файл")
    print("2 — Розшифрувати файл")
    choice = input("Ваш вибір (1/2): ").strip()

    if choice == '1':
        encrypt()
    elif choice == '2':
        decrypt()
    else:
        print("Невідомий вибір. Спробуйте ще раз.")


if __name__ == '__main__':
    main()
