create table machineries_images
(
    id      int auto_increment
        primary key,
    item_id int         null,
    image   varchar(36) not null
);

create index images_machineries_id_fk
    on machineries_images (item_id);

create table machinery
(
    id                  int auto_increment
        primary key,
    title               text                               null,
    manufacturer        text                               null,
    technical_condition text                               null,
    location            text                               null,
    year                text                               null,
    description         text                               null,
    cash                text                               null,
    leasing             text                               null,
    credit              text                               null,
    link                text                               null,
    created_at          datetime default CURRENT_TIMESTAMP not null,
    last_updated        datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    image               text                               null
);

create table passenger_car_images
(
    id      int auto_increment
        primary key,
    item_id int         null,
    image   varchar(36) not null
);

create index images_personal_cars_id_fk
    on passenger_car_images (item_id);

create table passenger_cars
(
    id           int auto_increment
        primary key,
    title        text                               null,
    brand        text                               null,
    model        text                               null,
    type         text                               null,
    year         text                               null,
    capacity     text                               null,
    mileage      text                               null,
    fuel         text                               null,
    vat          text                               null,
    location     text                               null,
    approval     text                               null,
    description  text                               null,
    cash         decimal(10, 2)                     null,
    leasing      decimal(10, 2)                     null,
    credit       decimal(10, 2)                     null,
    link         text                               null,
    created_at   datetime default CURRENT_TIMESTAMP not null,
    last_updated datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    image        text                               null
);

create table users
(
    id       int auto_increment
        primary key,
    username text null,
    name     text null
);

