# -*- encoding: utf-8 -*-
from fake_db import xhs
import time


class UserOptionCode(object):
    SUCCESS = 10000
    ERROR_USER_EXISTS = -1001
    ERROR_UPDATE_USER = -1002


class User(UserOptionCode):

        @classmethod
        def add_user(cls, user_name, tel, email, password):
            time.sleep(0.6)
            __currents_users = xhs.users
            __new_user = {"username": user_name,
                          "tel": tel,
                          "email": email,
                          "password": password
                          }

            for __user in __currents_users:
                if __user['username'] == __new_user['username']:
                    return [cls.ERROR_USER_EXISTS, __new_user]

            xhs.users.append(__new_user)
            return [cls.SUCCESS, __new_user]

        @classmethod
        def get_all_users(cls):
            time.sleep(1)
            __currents_users = xhs.users
            return [cls.SUCCESS, __currents_users]

        @classmethod
        def update_user_info(cls, user_name, tel, email, password):
            ret_val = cls.add_user(user_name, tel, email, password)
            if ret_val[0] == cls.SUCCESS:
                return [cls.SUCCESS, ret_val[1]]
            else:
                return [cls.ERROR_UPDATE_USER, ret_val[1]]



