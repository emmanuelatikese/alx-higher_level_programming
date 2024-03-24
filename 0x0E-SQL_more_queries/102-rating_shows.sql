-- suming all rating
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows LEFT JOIN tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating
DESC;
