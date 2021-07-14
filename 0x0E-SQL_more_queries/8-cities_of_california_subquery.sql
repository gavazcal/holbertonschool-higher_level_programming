-- performs a subquery to return all cities in a state
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name='California') ORDER BY id ASC;
