from datetime import date


# --------------- Часть A. Функции----------------


# 1. Нормализация email адресов. Приводит адреса к нижнему регистру и убирает пробелы
def normalize_addresses(value: str) -> str:
    return value.strip().lower()


# 2. Сокращенная версия тела письма. Создает короткую версию тела (первые 10 символов + "...")
def add_short_body(email: dict) -> dict:
    email["short_body"] = email["body"][:10] + "..."
    return email


# 3. Очистка текста письма. Заменяет табы и переводы строк на пробелы
def clean_body_text(body: str) -> str:
    return body.translate(str.maketrans('\t\n\r', '   ')).strip()


# 4. Формирование итогового текста письма. Создает форматированный текст письма
def build_sent_text(email: dict) -> str:
    return f"Кому: {email['to']}, от {email['from']}\nТема: {email['subject']}, дата {email['date']}\n{email['clean_body']}"


# 5. Проверка пустоты темы и тела. Проверяет, заполнены ли обязательные поля
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    is_subject_empty = not bool(subject)
    is_body_empty = not bool(body)
    return is_subject_empty, is_body_empty


# 6. Маска email отправителя. Создает маскированную версию email = первые 2 символа + "***@" + домен
def mask_sender_email(login: str, domain: str) -> str:
    masked_login = login[:2] + "***@" + domain
    return f"{masked_login}@{domain}"


# 7. Создать функцию, которая проверит корректности email адресов. Адрес считается корректным, если:
# содержит символ @;
# оканчивается на один из доменов: .com, .ru, .net.
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []
    for email in email_list:
        clean_email = email.strip()

        if not clean_email:
            continue

        match clean_email:
            case _ if '@' in clean_email and (clean_email.endswith('.com') or
                                              clean_email.endswith('.ru') or
                                              clean_email.endswith('.net')):
                correct_emails.append(clean_email)
    return correct_emails


test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]

print("Корректные email:")
result = get_correct_email(test_emails)
for email in result:
    print(f"  - {email}")


# 8. Создание словаря письма. Создает базовую структуру письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    return {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "body": body
    }


# 9. Добавление даты отправки.  Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
def add_send_date(email: dict) -> dict:
    email['date'] = str(date.today())
    return email


# 10. Получение логина и домена. Разделяет email на логин и домен
def extract_login_domain(address: str) -> tuple[str, str]:
    return tuple(address.split('@', 1)) \
        if '@' in address else (address, '')


# ------------------ Часть B. Отправка письма---------------------

# Создать функцию отправки письма с базовой валидацией адресов и логикой выбора отправителя recipient
# Функция принимает список получателей, тему, сообщение и отправителя.

def sender_email(
        recipient_list: list[str],
        subject: str,
        message: str, *,
        sender="default@study.com"
) -> list[dict]:
    # 1. Проверить, что список получателей recipient_list не пустой
    if not recipient_list:
        return []

    # 2. Проверить корректность email отправителя и получателей через get_correct_email()
    all_emails = [sender] + recipient_list
    correct_emails = get_correct_email(all_emails)

    if sender not in correct_emails:
        return []

    # 3. Проверить заполненность темы и тела письма через check_empty_fields().
    # Если одно из них пустое — вернуть пустой список.
    is_subj_empty, is_body_empty = check_empty_fields(subject, message)
    if is_subj_empty or is_body_empty:
        return []

    # 4. Исключить отправку самому себе: пройти по каждому элементу recipient_list в цикле for,
    # если адрес совпадает с sender, удалить его из списка.
    recipient_list = [r for r in recipient_list if r != sender]

    # 5. Нормализовать: subject и body → с помощью clean_body_text() recipient_list и sender → с помощью normalize_addresses()
    normalized_subject = clean_body_text(subject)
    normalized_body = clean_body_text(message)
    normalized_sender = normalize_addresses(sender)
    recipient_list = [normalize_addresses(r) for r in recipient_list]

    # 6. Создать письмо для каждого получателя функцией create_email().
    all_emails = []

    for one_recipient in recipient_list:
        email = create_email(
            sender=normalized_sender,
            recipient=one_recipient,
            subject=normalized_subject,
            body=normalized_body
        )
        all_emails.append(email)
        email["clean_body"] = normalized_body

        # 7. Добавить дату отправки с помощью add_send_date().
        email = add_send_date(email)

        # 8. Замаскировать email отправителя с помощью extract_login_domain() и mask_sender_email().
        login, domain = extract_login_domain(sender)
        masked_sender = mask_sender_email(login, domain)
        email["sender"] = masked_sender

        # 9. Сохранить короткую версию в email["short_body"].
        email = add_short_body(email)

        # 10. Сформировать итоговый текст письма функцией build_sent_text().
        email['sent_text'] = build_sent_text(email)

        all_emails.append(email)

    # Вернуть итоговый список писем.
    return all_emails


# ---------- Пример ----------
if __name__ == "__main__":
    test_emails = [
        "user@gmail.com",
        "admin@company.ru",
        "test_123@service.net",
        "Example.User@domain.com",
        "default@study.com",
        " hello@corp.ru  ",
        "user@site.NET",
        "user@domain.coM",
        "user.name@domain.ru",
        "usergmail.com",
        "user@domain",
        "user@domain.org",
        "@mail.ru",
        "name@.com",
        "name@domain.comm",
        "",
        "   ",
    ]

result = sender_email(
    recipient_list=test_emails,
    subject="Важно",
    message="С праздником!",
    sender="admin@company.ru"
)

for email in result:
    print(email["sent_text"])
    print("-" * 50)
