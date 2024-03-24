-- listing things from two tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.title = tv_show_genres.title
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

