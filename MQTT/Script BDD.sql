DROP DATABASE IF EXISTS mqttdb;
CREATE DATABASE mqttdb;
USE mqttdb;

CREATE TABLE Capteur (
id VARCHAR(50) NOT NULL,
nom_capteur VARCHAR(50) NOT NULL,
piece VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE Donnee (
id_capteur varchar(50) NOT NULL,
date_ date NOT NULL,
heure time NOT NULL,
temperature float NOT NULL,
CONSTRAINT fk_Capteur
	FOREIGN KEY (id_capteur)
	REFERENCES Capteur(id)
);

INSERT INTO Capteur (id,nom_capteur,piece) VALUES ('1025','Capteur1','Salon')
