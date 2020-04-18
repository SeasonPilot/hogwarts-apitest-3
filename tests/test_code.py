#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hogwarts_apitest.api import BaseApi

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)

class ApiHttpbinGet(BaseApi):

    url = "http://127.0.0.1/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}

class ApiHttpbinPost(BaseApi):

    url = "http://127.0.0.1/post"
    method = "POST"
    headers = {"accept": "application/json"}
    # data = "abc=123"
    # json = {"abc": 123}

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code", 200)\
        # .validate("headers.server", "gunicorn/19.9.0")\
        # .validate("json.url", "http://127.0.0.1/get")

def test_httpbin_get_with_prams():
    ApiHttpbinGet()\
        .set_params(abc=123, xyz=456)\
        .run()\
        .validate("status_code", 200)

def test_httpbin_post():
    ApiHttpbinPost()\
        .set_data("abc=123") \
        .run()\
        .validate("status_code", 200)

