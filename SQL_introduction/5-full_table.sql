SELECT 
    CONCAT(
        table_name, 
        ' CREATE TABLE `', table_name, '` (',
        GROUP_CONCAT(
            CONCAT(
                '\n  `', column_name, '` ', column_type,
                IF(is_nullable = 'NO', ' NOT NULL', ' NULL'),
                IF(column_default IS NOT NULL, CONCAT(' DEFAULT ', column_default), ''),
                IF(extra != '', CONCAT(' ', extra), '')
            ) ORDER BY ordinal_position SEPARATOR ',',
        ') ENGINE=', engine,
        ' DEFAULT CHARSET=', table_collation
    ) AS 'Create Table'
FROM information_schema.tables t
JOIN information_schema.columns c ON t.table_name = c.table_name
WHERE t.table_schema = DATABASE() AND t.table_name = 'first_table'
GROUP BY table_name;
