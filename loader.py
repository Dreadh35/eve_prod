#!/usr/bin/env python3

import configparser
import mysql.connector


config.read('config.ini')
config = configparser.ConfigParser()

db_user = config('mysql','user')
db_pw = config('mysql','user')
db_host = config('
db_eve_sde = config('mysql','eve_sde_db')
db_eve_prod = config('config','eve_prod_db')

eve_sde_db = mysql.connector.connect(
							user=db_user, 
							password=db_pw,
                            host=db,
                            database=)
							
e