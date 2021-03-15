-- Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с 
-- нашим пользователем.
USE vk;

-- берём всенаправленные сообщения
SELECT COUNT(*) AS cnt, from_user_id, to_user_id 
FROM messages
-- отсекаем сообщения только с нашим выбранным пользователем
WHERE (from_user_id = 1 OR to_user_id = 1) 
-- и с подтверждённой дружбой
AND 
(
SELECT status 
FROM friend_requests
WHERE initiator_user_id = messages.from_user_id
AND
target_user_id = messages.to_user_id 
) = 'approved'
-- группируем по отправителям и получателям 
GROUP BY from_user_id, to_user_id
ORDER BY cnt DESC
LIMIT 1;


-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
SELECT COUNT(*) AS likes_under_10
FROM likes
-- выбираем возраст пользователей из профилей
WHERE (
	SELECT TIMESTAMPDIFF(YEAR, birthday, NOW())
	FROM profiles
-- где id пользователя соответствует id пользователя медиа
	WHERE user_id = (
		SELECT user_id 
		FROM media
		WHERE id=likes.media_id 
)) < 10;



-- Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT COUNT(user_id) AS gender_likes, 
-- подставляем пол
(
SELECT
CASE (gender)
     WHEN 'm' THEN 'мужской'
     WHEN 'f' THEN 'женский'
     ELSE 'другой'
END
AS gender
FROM profiles
WHERE user_id = likes.user_id) AS gender
FROM LIKES
GROUP BY gender;

