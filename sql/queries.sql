-- 1. Список всех подкастов (SELECT)
SELECT id, title FROM podcasts ORDER BY title;

-- 2. Список всех пользователей (SELECT)
SELECT id, username, email FROM users ORDER BY username;

-- 3. Поиск подкастов по названию (WHERE + LIKE)
SELECT id, title FROM podcasts WHERE title LIKE ?;

-- 4. Отзывы конкретного пользователя (WHERE)
SELECT id, podcast_id, text FROM reviews WHERE user_id = ?;

-- 5. Отзывы с оценкой выше 4 (WHERE)
SELECT id, podcast_id, rating FROM reviews WHERE rating >= 4;

-- 6. Все отзывы с названием подкаста и именем автора (JOIN)
SELECT r.id, r.text, p.title AS podcast_title, u.username
FROM reviews r
JOIN podcasts p ON r.podcast_id = p.id
JOIN users u ON r.user_id = u.id
ORDER BY r.id;

-- 7. Подкасты с авторами (JOIN)
SELECT p.id, p.title, u.username AS author_name
FROM podcasts p
LEFT JOIN users u ON p.author_id = u.id;

-- 8. Общее количество отзывов (агрегат COUNT)
SELECT COUNT(*) AS reviews_count FROM reviews;

-- 9. Средняя оценка по подкасту (агрегат AVG + GROUP BY)
SELECT p.id, p.title, AVG(r.rating) AS avg_rating, COUNT(r.id) AS cnt
FROM podcasts p
LEFT JOIN reviews r ON p.id = r.podcast_id
GROUP BY p.id, p.title
ORDER BY avg_rating DESC;

-- 10. Пользователи с количеством отзывов (GROUP BY)
SELECT u.id, u.username, COUNT(r.id) AS reviews_count
FROM users u
LEFT JOIN reviews r ON u.id = r.user_id
GROUP BY u.id, u.username
ORDER BY reviews_count DESC;

-- 11. Подкасты с более чем 1 отзывом (HAVING)
SELECT p.title, COUNT(r.id) AS cnt
FROM podcasts p
JOIN reviews r ON p.id = r.podcast_id
GROUP BY p.id, p.title
HAVING COUNT(r.id) > 1;