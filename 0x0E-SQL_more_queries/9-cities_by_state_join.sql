--List all cities contained in the database.
--sort in Ascending order
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
