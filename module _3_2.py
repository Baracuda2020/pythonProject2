


def send_email(message, recipient, sender="university.help@gmail.com"):
    message = ["Невозможно отправить письмо с адреса", "Письмо успешно отправлено с адреса",
               "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", "на адрес",
               "Нельзя отправить письмо самому себе!"]
    recipient.endswith(('.com', '.ru', '.net'))
    sender.endswith(('.com', '.ru', '.net'))
    if "@" not in recipient \
            or "@" not in sender \
            or not recipient.endswith(('.com', '.ru', '.net')) \
            or not sender.endswith(('.com', '.ru', '.net')):
        print(message[0], sender, message[3], recipient)
    elif sender == recipient:
        print(message[4])
    elif sender == "university.help@gmail.com":
        print(message[1], sender, message[3], recipient)
    else:
        print(message[2], sender, message[3], recipient)


send_email(message='Пожалуйста, пришлите пин-код вашей карты', recipient='vasyok1337@gmail.com',
           sender='university.help@gmail.com')
send_email(message='Пожалуйста, пришлите пин-код вашей карты', recipient='urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email(message='Пожалуйста, исправьте задание', recipient='urban.student@mail.ru', sender='urban.student@mail.uk')
send_email(message='Пожалуйста, пришлите пин-код вашей карты', recipient='university.help@gmail.com',
           sender='university.help@gmail.com')