import sqlite3

DATABASE = "flask_lab.app.db"


def db_init() -> None:
    conn = sqlite3.connect(DATABASE)
    conn.executescript(
        "CREATE TABLE if not exists books ("
        "topic TEXT, "
        "author TEXT, "
        "genre TEXT, "
        "text TEXT, "
        "create_time DATETIME, "
        "last_edit_time DATETIME)"
    )
    conn.commit()
    conn.executescript(
        "CREATE TABLE if not exists users_flask ("
        "login TEXT UNIQUE, "
        "password TEXT, "
        "admin INTEGER)"
    )
    conn.close()


def db_fill() -> None:
    conn = sqlite3.connect(DATABASE)
    conn.executescript(
        """
        delete from books;
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Pseudalopex gymnocercus', 'Olympe Lehrer', 'Front-line', 'in faucibus orci luctus et ultrices posuere cubilia curae mauris', '2021-10-15 17:32:00', '2022-07-03 18:31:24');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Eolophus roseicapillus', 'Ax Fanner', 'secured line', 'massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat', '2022-02-08 01:24:31', '2022-04-28 04:05:08');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Acridotheres tristis', 'Mei Gowing', 'Triple-buffered', 'ut suscipit a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce congue', '2021-10-31 11:27:22', '2022-09-22 16:21:12');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Equus burchelli', 'Claire Stallworth', 'interface', 'mauris morbi non lectus aliquam sit amet diam in magna bibendum', '2021-10-15 06:33:02', '2022-09-29 09:21:45');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Cygnus atratus', 'Currey Hartus', 'challenge', 'id nisl venenatis lacinia aenean sit amet justo morbi ut odio cras mi', '2022-01-12 04:12:20', '2022-03-10 01:36:23');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Coluber constrictor', 'Ferdinanda Escott', 'Assimilated', 'ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae', '2021-12-29 12:04:16', '2022-02-11 22:10:55');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Bettongia penicillata', 'Tabb Keyzman', 'strategy', 'in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis', '2021-11-08 16:54:27', '2022-02-01 02:38:19');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Bassariscus astutus', 'Miof mela Boother', 'Organized', 'ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat volutpat in congue etiam justo', '2022-05-14 13:22:41', '2022-07-06 09:49:54');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Trichechus inunguis', 'Ali Dedon', 'Integrated', 'quam pharetra magna ac consequat metus sapien ut nunc vestibulum', '2022-02-10 12:21:26', '2022-01-29 00:35:10');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Centrocercus urophasianus', 'Aimee Halliburton', 'capacity', 'risus semper porta volutpat quam pede lobortis ligula sit amet', '2021-11-07 15:47:37', '2022-07-18 22:51:58');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Naja haje', 'Gunar Drover', 'software', 'et magnis dis parturient montes nascetur ridiculus mus etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem', '2022-09-13 04:20:09', '2021-10-21 09:21:06');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Eolophus roseicapillus', 'Ros Kerswell', 'hierarchy', 'mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim', '2022-02-16 18:34:46', '2022-05-26 20:46:13');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Semnopithecus entellus', 'Clemens Roots', 'Open-architected', 'tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit', '2022-08-12 03:37:24', '2022-03-07 01:15:02');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Bassariscus astutus', 'Taddeusz Stivey', 'Proactive', 'rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat', '2022-01-22 16:01:22', '2022-03-20 02:54:01');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Tetracerus quadricornis', 'Edythe Scohier', 'alliance', 'rutrum rutrum neque aenean auctor gravida sem praesent id massa id nisl venenatis lacinia aenean sit amet justo', '2022-04-08 09:34:10', '2022-08-13 15:53:39');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Lemur fulvus', 'Billie Aseef', 'workforce', 'diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est quam', '2022-08-15 03:17:17', '2022-06-09 00:42:16');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Odocoileus hemionus', 'Lorens Hannigan', 'homogeneous', 'vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae', '2021-12-06 07:39:03', '2021-12-30 09:19:09');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Haematopus ater', 'Perry O''Breen', 'Decentralized', 'nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit', '2022-08-03 06:01:17', '2022-04-02 13:35:16');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Francolinus leucoscepus', 'Bord Bolstridge', 'exuding', 'porta volutpat quam pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh', '2021-12-26 08:58:27', '2021-12-24 23:19:22');
        insert into books (topic, author, genre, text, create_time, last_edit_time) values ('Zosterops pallidus', 'Gib Siddle', 'function', 'est quam pharetra magna ac consequat metus sapien ut nunc vestibulum ante ipsum primis in faucibus', '2022-02-24 07:39:21', '2021-12-23 22:44:44');"""
    )
    conn.commit()
    conn.executescript(
        """
        delete from users_flask;
        insert into users_flask (login, password, admin) values ('user', 'user', 0);
        insert into users_flask (login, password, admin) values ('admin', 'admin', 1);
        """
    )
    conn.commit()
    conn.close()


def db_setup() -> str:
    try:
        db_init()
        db_fill()
        return """
            Successfully initialized database
            <a href="/"><h3>Home</h3></a>
            """
    except Exception:
        return "Database init Failed"
