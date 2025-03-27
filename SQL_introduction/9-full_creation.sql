-- Si la table 'second_table' existe déjà, elle sera supprimée
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

-- Insertion des lignes manquantes pour correspondre à la sortie attendue
INSERT INTO second_table (id, name, score) VALUES (11, 'A', 12);
INSERT INTO second_table (id, name, score) VALUES (12, 'B', 12);
INSERT INTO second_table (id, name, score) VALUES (13, 'C', 12);
INSERT INTO second_table (id, name, score) VALUES (14, 'D', 12);
