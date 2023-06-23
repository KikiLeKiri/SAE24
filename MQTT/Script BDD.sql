DROP DATABASE IF EXISTS mqttdb;
CREATE DATABASE mqttdb;
USE mqttdb;

CREATE TABLE Capteur (
id INT NOT NULL AUTO_INCREMENT,
nom_capteur VARCHAR(50) NOT NULL,
piece VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE Donnee (
id INT NOT NULL AUTO_INCREMENT,
id_capteur INT NOT NULL,
date_ DATE NOT NULL,
heure TIME NOT NULL,
temperature FLOAT NOT NULL,
PRIMARY KEY (id),
CONSTRAINT fk_Capteur
	FOREIGN KEY (id_capteur)
	REFERENCES Capteur(id)
);

INSERT INTO Capteur (id,nom_capteur,piece) VALUES ('1025','Capteur1','Salon')
