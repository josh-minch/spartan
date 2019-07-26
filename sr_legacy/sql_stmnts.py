create_food_des_stmt = '''
DROP TABLE IF EXISTS 'food_des';
CREATE TABLE 'food_des' (
  id int PRIMARY KEY NOT NULL,
  food_group_id int REFERENCES food_group(id) NOT NULL,
  long_desc text NOT NULL DEFAULT '',
  short_desc text NOT NULL DEFAULT '',
  common_name text NOT NULL DEFAULT '',
  manufac_name text NOT NULL DEFAULT '',
  survey text NOT NULL DEFAULT '',
  ref_desc text NOT NULL DEFAULT '',
  refuse int NOT NULL,
  sci_name text NOT NULL DEFAULT '',
  nitrogen_factor float NOT NULL,
  protein_factor float NOT  NULL,
  fat_factor float NOT NULL,
  carb_factor float NOT NULL
);
CREATE INDEX food_short_desc_search_index ON food_des(short_desc);
CREATE INDEX food_long_desc_search_index ON food_des(long_desc);
'''

create_fd_group_stmnt = '''
DROP TABLE IF EXISTS `fd_group`;
CREATE TABLE `fd_group` (
  id int PRIMARY KEY NOT NULL,
  name text NOT NULL
);
'''

create_nut_data_stmt = '''
DROP TABLE IF EXISTS 'nut_data';
CREATE TABLE 'nut_data' (
    food_id int REFERENCES food(id) NOT NULL,
    nut_id int REFERENCES nutrient(id) NOT NULL,
    amount float,
    num_data_points int,
    std_error float,
    source_code text,
    derivation_code text,
    reference_food_id REFERENCES food(id),
    added_nutrient text,
    num_studies int,
    min float,
    max float,
    degrees_freedom int,
    lower_error_bound float,
    upper_error_bound float,
    stat_comments text,
    modification_date text,
    PRIMARY KEY(food_id, nut_id)
    );
'''

create_nutr_def_stmnt = '''
DROP TABLE IF EXISTS `nutr_def`;
CREATE TABLE `nutr_def` (
  id int PRIMARY KEY NOT NULL,
  units text NOT NULL,
  tag_name text NOT NULL DEFAULT '',
  name text NOT NULL,
  num_decimal_places text NOT NULL,
  sr_order int NOT NULL
);
CREATE INDEX nutr_def_name_search_index ON nutr_def(name);
'''

create_weight_stmnt = '''
DROP TABLE IF EXISTS `weight`;
CREATE TABLE `weight` (
    food_id int REFERENCES food(id) NOT NULL,
    sequence_num int NOT NULL,
    amount float NOT NULL,
    description text NOT NULL,
    gm_weight float NOT NULL,
    num_data_pts int,
    std_dev float,
    PRIMARY KEY(food_id, sequence_num)
);
'''

insert_food_des_stmt = '''
    INSERT INTO food_des VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
insert_fd_group_stmt = '''
    INSERT INTO fd_group VALUES (?, ?)
'''
insert_nut_data_stmt = '''
    INSERT INTO nut_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
insert_nutr_def_stmt = '''
    INSERT INTO nutr_def VALUES (?, ?, ?, ?, ?, ?)
'''
insert_weight_stmt = '''
    INSERT INTO weight VALUES (?, ?, ?, ?, ?, ?, ?)
'''

file_names = ['FOOD_DES.txt', 'FD_GROUP.txt', 'NUT_DATA.txt', 'NUTR_DEF.txt', 'WEIGHT.txt']

file_name_to_insert = {
    'FOOD_DES.txt': insert_food_des_stmt,
    'FD_GROUP.txt': insert_fd_group_stmt,
    'NUT_DATA.txt': insert_nut_data_stmt,
    'NUTR_DEF.txt': insert_nutr_def_stmt,
    'WEIGHT.txt': insert_weight_stmt
}

def add_missing_nut_ids():

    con = sql.connect('sr_legacy.db')
    cur = con.cursor()

    cur.execute('select id from food_des')
    food_ids = cur.fetchall()

    for food_id in food_ids:

        cur.execute('CREATE TEMPORARY TABLE temptable(food_id INT, nut_id INT, amount FLOAT)')

        cur.execute('''
        insert into temptable (nut_id) 
        select id from nutr_def
        except
        select (nut_id) from nut_data where food_id = ? ''', food_id)

        cur.execute('update temptable set food_id = ?', food_id)
        cur.execute('update temptable set amount = NULL')

        cur.execute('''
        insert into nut_data (food_id, nut_id, amount) 
        select food_id, nut_id, amount from temptable ''')

        cur.execute('drop table temptable')

    con.commit()
    con.close()