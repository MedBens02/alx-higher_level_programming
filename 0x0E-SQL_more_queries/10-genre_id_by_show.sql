-- Lists all shows with 1 genre at least.
SELECT ts.title, tg.genre_id FROM tv_shows ts
INNER JOIN tv_show_genres tg ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id;
