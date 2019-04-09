# -*- encoding:utf-8 -*-
import json
from flask import request
from app import app

from views import User
from fake_db import xhs


@app.route('/community', methods=['GET'])
def community():
    if request.method == 'GET':
        __json_dic = {}
        __json_dic['communities'] = xhs.community
        __ret_json = json.dumps(__json_dic, ensure_ascii=False)
        return __ret_json, 200
    else:
        return "", 400


@app.route('/user', methods=['GET', 'POST', 'PUT'])
def register():
    __json_dic = {}

    # register new user
    if request.method == 'POST':
        __username = request.form['username']
        __tel = request.form['tel']
        __email = request.form['email']
        __password = request.form['password']

        ret_val = User.add_user(__username, __tel, __email, __password)

        if ret_val[0] == User.SUCCESS:
            __json_dic['ret_code'] = "200"
            __json_dic['ret_msg'] = "Register Success"
        elif ret_val[0] == User.ERROR_USER_EXISTS:
            __json_dic['ret_code'] = "300"
            __json_dic['ret_msg'] = "User Already Exist!"
        else:
            __json_dic['ret_code'] = "400"
            __json_dic['ret_msg'] = "Unknown Error!!"

        __json_dic['new_user_info'] = ret_val[1]
        __ret_json = json.dumps(__json_dic, ensure_ascii=False)

        return __ret_json, __json_dic['ret_code']

    # get all user list
    elif request.method == 'GET':
        ret_val = User.get_all_users()

        if ret_val[0] == User.SUCCESS:
            __json_dic['ret_code'] = "200"
            __json_dic['ret_msg'] = "Get all user information Success"
            __json_dic['users'] = ret_val[1]
        else:
            __json_dic['ret_code'] = "400"
            __json_dic['ret_msg'] = "Unknown Error!"
            __json_dic['users'] = []

        __ret_json = json.dumps(__json_dic, ensure_ascii=False)
        return __ret_json, __json_dic['ret_code']

    # update user info
    elif request.method == 'PUT':
        __user_name = request.json['username']
        __tel = request.json['tel']
        __email = request.json['email']
        __password = request.json['password']

        ret_val = User.update_user_info(__user_name, __tel, __email, __password)
        if ret_val[0] == User.SUCCESS:
            __json_dic['ret_code'] = "200"
            __json_dic['ret_msg'] = "Update User Info Success"
        else:
            __json_dic['ret_code'] = "400"
            __json_dic['ret_msg'] = "Update User Info Error"

        __json_dic['users_info'] = ret_val[1]
        __ret_json = json.dumps(__json_dic, ensure_ascii=False)
        return __ret_json, __json_dic['ret_code']

    else:
        __json_dic['ret_code'] = "403"
        __json_dic['ret_msg'] = "The method not allowed"

        __ret_json = json.dumps(__json_dic, ensure_ascii=False)
        return __ret_json, __json_dic['ret_code']
