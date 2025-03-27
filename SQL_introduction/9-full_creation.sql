-- Vérifier si la table 'second_table' existe déjà et la supprimer si c'est le cas
DROP TABLE IF EXISTS second_table;

-- Création de la table 'second_table'
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insertion des 4 premières lignes
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);

-- Ajout des nouveaux enregistrements après vérification de l'existence de la table
INSERT INTO second_table (id, name, score) VALUES (11, 'A', 12);
INSERT INTO second_table (id, name, score) VALUES (12, 'B', 12);
INSERT INTO second_table (id, name, score) VALUES (13, 'C', 12);
INSERT INTO second_table (id, name, score) VALUES (14, 'D', 12);

-- Affichage des enregistrements après ajout des nouveaux
SELECT * FROM second_table;
