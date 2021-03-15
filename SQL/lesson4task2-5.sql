-- Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке.

USE vk;

SELECT DISTINCT firstname FROM users ORDER BY firstname ASC;


-- Первые пять пользователей пометить как удаленные.
UPDATE users SET is_deleted=1 LIMIT 5;
-- посмотрим, что получилось
SELECT firstname,lastname,is_deleted FROM USERS LIMIT 10;

-- Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней).
DELETE FROM messages WHERE created_at > NOW();

-- Написать название темы курсового проекта.
Создание БД для сервиса автоматического парсинга и перевода сайтов с использованием API etxt.ru
