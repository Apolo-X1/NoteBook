CREATE DATABASE IF NOT EXISTS first_app_notebook;
USE first_app_notebook;

CREATE TABLE users(

id             int(1000) auto_increment not null,
name_user      varchar(100) not null,
last_name      varchar(100) not null,
email          varchar(300) not null,
passwd         varchar(500) not null,
dateDay        date not null,

CONSTRAINT pk_users PRIMARY KEY (id),
CONSTRAINT uq_email UNIQUE (email)
)ENGINE = InnoDb;



CREATE TABLE notes(

id            int(1000) auto_increment not null,
user_id       int(1000) not null,
title         varchar(200) not null,
note_txt      MEDIUMTEXT,
dateDay       date not null,

CONSTRAINT pk_notes PRIMARY KEY (id),
CONSTRAINT fk_user_note FOREIGN KEY (user_id) REFERENCES users (id)

)ENGINE =InnoDb;
