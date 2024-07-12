# def send_email(message, recipient, *, sender='university.help@gmail.com'):
#     if not ('@' in recipient and ('.com' in recipient or '.ru' in recipient or '.net' in recipient)):
#         print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
#     elif not ('@' in sender and ('.com' in sender or '.ru' in sender or '.net' in sender)):
#         print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
#     elif recipient == sender:
#         print('Нельзя отправить письмо самому себе!')
#     else:
#         if sender == 'university.help@gmail.com':
#             print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
#         else:
#             print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

#решение с endswith
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif not recipient.endswith('.com' or '.ru' or '.net') and sender.endswith('.com' or '.ru' or '.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')