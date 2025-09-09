import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

template = """\
From: {3}
To: {4}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {0}! {1} приглашает тебя на сайт {2}

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

url = "https://dvmn.org/profession-ref-program/hahawqwqofficial/B7KOk/"

friend = "Макс"

sender = "Макакич"

email_to = "hahawqwqofficial@gmail.com"

email_from = os.getenv("EMAIL_FROM")

password_app = os.getenv("PASSWORD_APP")

letter = template.format(friend, sender, url, email_from, email_to).encode("UTF-8")


server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)

server.login(email_from, password_app)

server.sendmail(email_from, email_to, letter)

server.quit()