-- Lists all genres and number of shows.
SELECT tg.name AS 'genre', COUNT(tsg.genre_id) AS 'number_of_shows'
FROM tv_genre tg
RIGHT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_pf_shows DESC;
