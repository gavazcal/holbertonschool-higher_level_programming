-- bundles all records with equal value
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;
