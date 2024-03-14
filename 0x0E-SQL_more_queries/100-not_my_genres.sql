-- Lists all genres not linked to Dexter.
SELECT tg.name FROM tv_genres tg
WHERE name NOT IN (
	SELECT tg.name FROM tv_genres tg
	LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
	LEFT JOIN tv_shows ts ON tsg.show_id = ts.id
	WHERE ts.title = 'Dexter'
)
GROUP BY tg.name
ORDER BY tg.name;
