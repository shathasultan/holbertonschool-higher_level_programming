-- show list of second_table by top score and score >= 10
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
