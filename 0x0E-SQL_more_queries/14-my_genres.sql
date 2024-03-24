-- listing shows
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.title = tv_shows.title
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
