-- Lists all comedy shows.
SELECT ts.title FROM tv_shows ts
JOIN tv_show_genres tsg ON tsg.show_id = ts.id
JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title;
