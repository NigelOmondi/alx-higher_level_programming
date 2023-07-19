--List all cities of california that can be found
--in hbtn_0d_usa database.
--Results sorted in ascending order based on cities.id
SELECT id, name
FROM cities
WHERE state_id IN ( 
		SELECT id
		FROM states
		WHERE name = "California")
ORDER BY id ASC;
