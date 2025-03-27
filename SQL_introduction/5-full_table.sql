-- com
SELECT
    table_name AS Table,
    GROUP_CONCAT(
        CONCAT(
            '  `', column_name, '` ', column_type, 
            IF(is_nullable = 'NO', ' NOT NULL', ' NULL'),
            IF(column_default IS NOT NULL, CONCAT(' DEFAULT ', column_default), '')
        ) ORDER BY ordinal_position SEPARATOR ',\n'
    ) AS 'Create Table'
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table'
GROUP BY table_name;
