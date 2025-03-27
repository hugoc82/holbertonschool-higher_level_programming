-- Ce script imprime la description complète de la table first_table
-- sans utiliser DESCRIBE ou EXPLAIN.

SELECT 
    'first_table' AS table_name,
    'CREATE TABLE `first_table`(' AS create_statement,
    GROUP_CONCAT(
        CONCAT('`', COLUMN_NAME, '`', 
            CASE WHEN IS_NULLABLE = 'NO' THEN ' NOT NULL' ELSE '' END, 
            CASE WHEN EXTRA != '' THEN ' ' + EXTRA ELSE '' END,
            ' ', COLUMN_TYPE
        )
        SEPARATOR ', '
    ) AS table_columns,
    'PRIMARY KEY(`id`)' AS primary_key,
    ')ENGINE=InnoDBDEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci' AS table_end
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table'
GROUP BY table_name;
