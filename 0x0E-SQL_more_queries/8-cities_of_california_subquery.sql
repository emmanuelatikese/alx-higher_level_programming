-- listing cities from california
SELECT id, name FROM hbtn_0d_usa.cities
WHERE state_id = (SELECT id FROM states) ORDER BY id ASC;
