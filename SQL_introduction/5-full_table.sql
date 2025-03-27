-- Afficher la structure de first_table
SELECT
    'first_table' AS table_name,
    'CREATE TABLE `first_table` (' AS create_statement,
    GROUP_CONCAT(
        CONCAT('`', COLUMN_NAME, '` ',
            COLUMN_TYPE,
            CASE WHEN IS_NULLABLE = 'NO' THEN ' NOT NULL' ELSE '' END,
            CASE WHEN EXTRA != '' THEN CONCAT(' ', EXTRA) ELSE '' END
        )
        ORDER BY ORDINAL_POSITION
        SEPARATOR ', '
    ) AS table_columns,
    ', PRIMARY KEY(`id`)' AS primary_key,
    ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;' AS table_end
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table'
GROUP BY table_name;
