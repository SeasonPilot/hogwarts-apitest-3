#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hogwarts_apitest.api import  BaseApi

class ApiHttpbinGet(BaseApi):

    url = "http://127.0.0.1/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}

class ApiHttpbinPost(BaseApi):

    url = "http://127.0.0.1/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    json = {"abc": 123}