import sqlite3 as sql
from flask import Flask, request
import json

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/get_donated_refugees')
def get_donated_refugees():
    user = request.args.get('user')
    con = sql.connect('refugee.db')
    con.row_factory = dict_factory

    cur = con.cursor()
    cur.execute("select * from refugees where donor='" + user + "'")

    rows = cur.fetchall()
    return json.dumps(rows)


@app.route('/get_refugee')
def get_refugees():
    user = request.args.get('user')
    # age = int(request.args.get('age'))
    # if age == 0:
    #     age_query = ''
    # elif age == 1:
    #     age_query =
    #
    # gender = request.args.get('gender')
    # if gender == 0:
    #     gender_query = ''
    # elif gender == 1:
    #     gender_query = 'gender = MALE'
    # elif gender == 2:
    #     gender_query = 'gender = FEMALE'
    #
    # disability = request.args.get('disability')
    # if disability == 0:
    #     disability_query = ''
    # elif disability == 1:
    #     disability_query = 'disability = Yes'
    # elif disability == 2:
    #     disability_query = 'disability = No'
    #
    # familial_status = request.args.get('familial_status')
    # if familial_status == 0:
    #     familial_status_query = ''
    # elif disability == 1:
    #     familial_status_query = 'familial_status = Married'
    # elif disability == 2:
    #     familial_status_query = 'familial_status = Unmarried'
    #
    # dependencies = request.args.get('dependencies')
    # if familial_status == 0:
    #     familial_status_query = ''
    # elif disability == 1:
    #     familial_status_query = 'familial_status = Married'
    # elif disability == 2:
    #     familial_status_query = 'familial_status = Unmarried'
    #
    # orphan_status = request.args.get('orphan_status')
    # if orphan_status == 0:
    #     orphan_status_query = ''
    # elif disability == 1:
    #     orphan_status_query = 'orphan_status = Yes'
    # elif disability == 2:
    #     orphan_status_query = 'orphan_status = No'

    con = sql.connect('refugee.db')
    con.row_factory = dict_factory

    cur = con.cursor()
    cur.execute("select * from refugees where not donor='"+user+"'")

    rows = cur.fetchall()
    return json.dumps(rows)


if __name__ == '__main__':
    app.run(debug=True)
