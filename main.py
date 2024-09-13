import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
link_ref = 'https://dvmn.org/referrals/ZwYwTf9IUPe9JJvFGvoHmAEBk518qNbJ38YnOr1N/'
my_friends_name = 'Л.Торвальдс!'
my_name = 'Гвидо ван Россум'
my_address = 'Lekantras84@yandex.ru'
recipent_addres = 'ligioner29@mail.ru'

title_of_letter = '''From: {}
To: {}
Subject: Заголовок письма
Content-Type: text/plain; charset="UTF-8";'''.format(my_address, recipent_addres)

text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''


text = text.replace('%website%', link_ref)
text = text.replace('%friend_name%!', my_friends_name)
text = text.replace('%my_name%', my_name)

letter = title_of_letter + '\n' + '\n' + text
letter_utf8 = letter.encode('UTF-8')


server.login(os.getenv('YANDEX_LOGIN_FROM_MAIL'), os.getenv('YANDEX_PASSWORD_FROM_MAIL'))
server.sendmail(my_address, recipent_addres, letter_utf8)
server.quit()

