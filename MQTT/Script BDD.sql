DROP DATABASE IF EXISTS mqttdb;
CREATE DATABASE mqttdb;
USE mqttdb;

CREATE TABLE Maison1 (
messageID INT NOT NULL AUTO_INCREMENT,
id VARCHAR(50) NOT NULL,
piece VARCHAR(50) NOT NULL,
date_ date NOT NULL,
heure time NOT NULL,
temperature float NOT NULL,
PRIMARY KEY (messageID)
);

CREATE TABLE Maison2 (
messageID INT NOT NULL AUTO_INCREMENT,
id VARCHAR(50) NOT NULL,
piece VARCHAR(50) NOT NULL,
date_ date NOT NULL,
heure time NOT NULL,
temperature float NOT NULL,
PRIMARY KEY (messageID)
);
