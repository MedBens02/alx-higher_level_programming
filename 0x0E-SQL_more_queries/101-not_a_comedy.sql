-- Lists all shows that are not comedy.
SELECT title FROM tv_shows
WHERE title NOT IN (
	SELECT ts.title FROM tv_shows ts
	LEFT JOIN tv_show_genres tsg ON tsg.show_id = ts.id
	LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id
	WHERE tg.name = 'Comedy'
	)
GROUP BY title
ORDER BY title;
