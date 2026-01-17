-- list all the cities of california
SELECT
    id,
    name
FROM cities
WHERE
    state_id = (
        SELECT states.id
        FROM states
        WHERE states.name = 'California'
    )
ORDER BY id ASC;
