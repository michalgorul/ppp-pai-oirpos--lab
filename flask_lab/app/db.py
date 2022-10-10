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
    conn.executescript(
        "CREATE TABLE if not exists news ("
        "topic TEXT, "
        "author TEXT, "
        "text TEXT, "
        "create_time DATETIME, "
        "last_edit_time DATETIME)"
    )
    conn.commit()
    conn.close()


def db_fill() -> None:
    conn = sqlite3.connect(DATABASE)
    conn.executescript(
        """
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
        insert into news (topic, author, text, create_time, last_edit_time) values ('Zosterops pallidus', 'Elfie Minnis', 'odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat', '2022-04-14 17:57:13', '2022-06-27 17:15:24');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Cereopsis novaehollandiae', 'Fletcher Westbury', 'vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id massa', '2022-07-01 15:20:28', '2022-06-17 19:00:28');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Microcebus murinus', 'Annnora Neill', 'sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus', '2021-10-14 23:36:58', '2022-04-06 22:57:23');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Macropus parryi', 'Rustin Swinnerton', 'curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu libero rutrum ac lobortis', '2022-03-19 21:18:34', '2021-12-24 03:44:50');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Hystrix cristata', 'Marve Grogan', 'non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet', '2022-07-27 05:07:42', '2022-02-28 01:58:53');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Streptopelia senegalensis', 'Georgia Gunthorpe', 'sit amet erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac', '2022-09-28 03:42:34', '2022-06-03 09:08:36');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Nyctanassa violacea', 'Atlanta Benninck', 'lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat', '2021-12-17 20:27:47', '2021-10-10 17:21:52');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Motacilla aguimp', 'Josiah Gyver', 'id luctus nec molestie sed justo pellentesque viverra pede ac diam cras pellentesque volutpat dui maecenas tristique est et', '2022-04-11 01:30:05', '2022-06-01 01:51:00');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Ardea golieth', 'Kingston Keesman', 'diam in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis', '2021-10-24 02:32:18', '2021-11-10 12:27:11');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Uraeginthus angolensis', 'Virgie Kindle', 'varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi', '2022-02-23 04:08:41', '2022-02-08 04:44:36');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Spizaetus coronatus', 'Hayden Segrott', 'nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id', '2022-03-04 22:20:19', '2022-02-19 04:58:39');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Canis lupus', 'Caroline Oatley', 'non pretium quis lectus suspendisse potenti in eleifend quam a odio in hac', '2021-10-19 23:10:23', '2022-03-20 02:09:48');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Manouria emys', 'Marlon Robbins', 'eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec', '2022-02-02 17:09:50', '2022-06-18 18:31:01');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Corythornis cristata', 'Lemmy Burdus', 'curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus at', '2022-02-19 14:38:35', '2022-09-21 00:29:13');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Anastomus oscitans', 'Nevile Doumerc', 'sed augue aliquam erat volutpat in congue etiam justo etiam pretium iaculis', '2021-10-31 12:19:22', '2022-04-02 03:01:12');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Agouti paca', 'Nicol Biggadike', 'eget eleifend luctus ultricies eu nibh quisque id justo sit amet sapien dignissim', '2021-10-21 14:32:57', '2021-11-26 03:39:02');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Ploceus intermedius', 'Maxim Lidgely', 'at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum', '2021-12-07 20:42:38', '2022-10-05 19:13:18');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Chloephaga melanoptera', 'Taryn Ayton', 'tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est', '2022-02-10 20:08:14', '2022-01-27 14:08:11');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Chamaelo sp.', 'Greta Plose', 'pretium nisl ut volutpat sapien arcu sed augue aliquam erat volutpat in congue etiam justo etiam', '2022-02-25 02:16:36', '2022-08-05 20:15:49');
        insert into news (topic, author, text, create_time, last_edit_time) values ('Anser anser', 'Briggs Gasgarth', 'hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien', '2022-07-25 15:09:25', '2022-05-28 17:27:35');        """
    )
    conn.commit()

