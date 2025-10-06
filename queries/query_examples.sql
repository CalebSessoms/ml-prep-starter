
SELECT species, COUNT(*) AS n FROM iris GROUP BY species ORDER BY n DESC LIMIT 10;
SELECT species, AVG(sepal_length) AS avg_sepal_length FROM iris GROUP BY species ORDER BY avg_sepal_length DESC;
