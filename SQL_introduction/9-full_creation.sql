-- Si la table 'second_table' existe déjà, elle sera supprimée
-- Cela ne génère pas d'erreur si la table n'existe pas.
DROP TABLE IF EXISTS second_table;

-- Création de la table 'second_table'
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insertion des données dans la table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
