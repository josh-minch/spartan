create_food_des = '''
DROP TABLE IF EXISTS 'food_des';
CREATE TABLE 'food_des' (
  id int PRIMARY KEY NOT NULL,
  food_group_id int REFERENCES fd_group(id) NOT NULL,
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

create_fd_group = '''
DROP TABLE IF EXISTS `fd_group`;
CREATE TABLE `fd_group` (
  id int PRIMARY KEY NOT NULL,
  name text NOT NULL
);
'''

create_nut_data = '''
DROP TABLE IF EXISTS 'nut_data';
CREATE TABLE 'nut_data' (
    food_id int REFERENCES food_des(id) NOT NULL,
    nut_id int REFERENCES nut_data(id) NOT NULL,
    amount float,
    num_data_points int,
    std_error float,
    source_code text,
    derivation_code text,
    reference_food_id REFERENCES food_des(id),
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

create_nutr_def = '''
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

create_weight = '''
DROP TABLE IF EXISTS `weight`;
CREATE TABLE `weight` (
    food_id int REFERENCES food_des(id) NOT NULL,
    sequence_num int NOT NULL,
    amount float NOT NULL,
    description text NOT NULL,
    gm_weight float NOT NULL,
    num_data_pts int,
    std_dev float,
    PRIMARY KEY(food_id, sequence_num)
);
'''

insert_food_des = '''
    INSERT INTO food_des VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
insert_fd_group = '''
    INSERT INTO fd_group VALUES (?, ?)
'''
insert_nut_data = '''
    INSERT INTO nut_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
insert_nutr_def = '''
    INSERT INTO nutr_def VALUES (?, ?, ?, ?, ?, ?)
'''
insert_weight = '''
    INSERT INTO weight VALUES (?, ?, ?, ?, ?, ?, ?)
'''

file_name_to_insert = {
    'FOOD_DES.txt': insert_food_des,
    'FD_GROUP.txt': insert_fd_group,
    'NUT_DATA.txt': insert_nut_data,
    'NUTR_DEF.txt': insert_nutr_def,
    'WEIGHT.txt': insert_weight
}