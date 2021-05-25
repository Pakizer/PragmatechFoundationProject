##Statik hisseler
1.navbar
2.contact
3.about
4.footer

##Dinamik hisseler
1.slider
2.login
3.categories
4.social media icon

[]


##SQL kodlari

create table users (
    id           INTEGER       PRIMARY KEY,
    user_name    VARCHAR (255),
    user_email   VARCHAR (255),
    user_type_id
);

create table type(
id integer,
type_name varchar(255)
)

create table slider(
id integer,
slider_img varchar(255),
slider_text varchar(255)
)
