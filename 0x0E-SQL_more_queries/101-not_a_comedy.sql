-- listing shows
SELECT title
FROM tv_shows
WHERE title NOT IN (SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
