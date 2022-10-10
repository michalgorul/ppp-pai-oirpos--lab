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
        insert into books (topic, author, text, genre) values ('Terathopius ecaudatus', 'Trevor Osorio', 'purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan', 'Tools');
        insert into books (topic, author, text, genre) values ('Gabianus pacificus', 'Faina Mathivon', 'odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices', 'Toys');
        insert into books (topic, author, text, genre) values ('Anastomus oscitans', 'Joete Orts', 'nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed', 'Automotive');
        insert into books (topic, author, text, genre) values ('Terrapene carolina', 'Erv Brickham', 'vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque', 'Beauty');
        insert into books (topic, author, text, genre) values ('Ovis orientalis', 'Clint Hapgood', 'nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis', 'Beauty');
        insert into books (topic, author, text, genre) values ('Lamprotornis chalybaeus', 'Opalina Tondeur', 'pede lobortis ligula sit amet eleifend pede libero quis orci nullam', 'Movies');
        insert into books (topic, author, text, genre) values ('Tachyglossus aculeatus', 'Herb Mansel', 'eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat', 'Automotive');
        insert into books (topic, author, text, genre) values ('Nannopterum harrisi', 'Wendi Stokes', 'eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui', 'Grocery');
        insert into books (topic, author, text, genre) values ('Larus dominicanus', 'Norby Hatherall', 'quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies', 'Automotive');
        insert into books (topic, author, text, genre) values ('Physignathus cocincinus', 'Gilberta Erley', 'elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus', 'Jewelry');
        insert into books (topic, author, text, genre) values ('Ephippiorhynchus mycteria', 'Evangeline Twinbourne', 'felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc', 'Games');
        insert into books (topic, author, text, genre) values ('Chionis alba', 'Ricard Willishire', 'nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et', 'Toys');
        insert into books (topic, author, text, genre) values ('Estrilda erythronotos', 'Lemmie Tiery', 'nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non velit donec diam neque', 'Beauty');
        insert into books (topic, author, text, genre) values ('Gopherus agassizii', 'Michele Slyme', 'curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique', 'Shoes');
        insert into books (topic, author, text, genre) values ('Cervus canadensis', 'Grant Fazakerley', 'ornare consequat lectus in est risus auctor sed tristique in tempus sit', 'Industrial');
        insert into books (topic, author, text, genre) values ('Thamnolaea cinnmomeiventris', 'Olimpia Struijs', 'varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum', 'Electronics');
        insert into books (topic, author, text, genre) values ('Ovibos moschatus', 'Demetri Foyster', 'porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor', 'Automotive');
        insert into books (topic, author, text, genre) values ('Zenaida asiatica', 'Tiphanie Maris', 'aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat', 'Industrial');
        insert into books (topic, author, text, genre) values ('Speothos vanaticus', 'Evangeline Witnall', 'cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non', 'Books');
        insert into books (topic, author, text, genre) values ('Rangifer tarandus', 'Alexei Syme', 'praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse', 'Health');
        """
    )
    conn.commit()
    conn.executescript(
        """
        insert into news (topic, author, text) values ('Felis chaus', 'Griffie Mulder', 'nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus');
        insert into news (topic, author, text) values ('Cygnus buccinator', 'Meggie Crutchley', 'vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet');
        insert into news (topic, author, text) values ('Numida meleagris', 'Zachery Gillford', 'id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices');
        insert into news (topic, author, text) values ('Equus burchelli', 'Tommie Gullefant', 'nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula');
        insert into news (topic, author, text) values ('Manouria emys', 'Lisette Dorrington', 'felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam');
        insert into news (topic, author, text) values ('Vanessa indica', 'Pennie Boyd', 'praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor');
        insert into news (topic, author, text) values ('Ephippiorhynchus mycteria', 'Erhart Pulster', 'eleifend pede libero quis orci nullam molestie nibh in lectus pellentesque at');
        insert into news (topic, author, text) values ('Pseudocheirus peregrinus', 'Ernesto Neat', 'orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris');
        insert into news (topic, author, text) values ('Colobus guerza', 'Joy Fearey', 'porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper');
        insert into news (topic, author, text) values ('Felis yagouaroundi', 'Joyous Fearns', 'quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse');
        insert into news (topic, author, text) values ('Choriotis kori', 'Brok Bairstow', 'nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo');
        insert into news (topic, author, text) values ('Macaca mulatta', 'Ondrea Langman', 'ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim');
        insert into news (topic, author, text) values ('Centrocercus urophasianus', 'Tabbie Meller', 'venenatis lacinia aenean sit amet justo morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim');
        insert into news (topic, author, text) values ('Eubalaena australis', 'Valaria de Mullett', 'a libero nam dui proin leo odio porttitor id consequat in consequat');
        insert into news (topic, author, text) values ('Laniaurius atrococcineus', 'Tiphany Emanson', 'blandit mi in porttitor pede justo eu massa donec dapibus duis at velit eu est');
        insert into news (topic, author, text) values ('Orcinus orca', 'Genevieve Commin', 'nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo');
        insert into news (topic, author, text) values ('Ratufa indica', 'Winny Joicey', 'leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis');
        insert into news (topic, author, text) values ('Microcebus murinus', 'Randi Sponder', 'mauris vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt');
        insert into news (topic, author, text) values ('Dicrostonyx groenlandicus', 'Thebault Domniney', 'pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc');
        insert into news (topic, author, text) values ('Chauna torquata', 'Noreen Kenwright', 'mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum nulla tellus in sagittis dui');
        """
    )
    conn.commit()

