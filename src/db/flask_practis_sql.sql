DROP DATABASES IF EXIST flask_practis_sql;
CREATE DATABASES flask_practis_sql;

use flask_practis_sql;

CREATE TABLE users(
    id int auto_increment primary key,
    nombre varchar(15),
    email varchar(50),
    password varchar(255)
);

CREATE TABLE products(
    id int auto_increment primary key,
    nombre varchar(15),
    precio float,
    img varchar(255)
);

CREATE TABLE users_favorites(
    user_id int 
    id_products int 
    primary key(user_id,id_products)
    foreign key (user_id) references users(id) on delete cascade
    foreign key (id_products) references products(id) on delete cascade 
);