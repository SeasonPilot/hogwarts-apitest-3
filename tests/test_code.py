#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tests.httpbin import ApiHttpbinGet, ApiHttpbinPost

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code", 200)\
        .validate("headers.server", "gunicorn/19.9.0")\
        .validate("json().url", "http://127.0.0.1/get")\
        .validate("json().headers.Accept", "application/json")

def test_httpbin_get_with_prams():
    ApiHttpbinGet()\
        .set_params(abc=123, xyz=456)\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://127.0.0.1/get?abc=123&xyz=456")\
        .validate("json().headers.Accept", "application/json")\
        .validate("json().args.abc", "123")

def test_httpbin_post():
    ApiHttpbinPost()\
        .set_data("abc=456")\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.server", "gunicorn/19.9.0")\
        .validate("json().url", "http://127.0.0.1/post")\
        .validate("json().headers.Accept", "application/json") \
        .validate("json().data", "abc=456")

def test_httpbin_get_parameters_share():
    user_id = "adk129"
    ApiHttpbinGet()\
        .set_params(user_id=user_id)\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://127.0.0.1/get?user_id=adk129")\
        .validate("json().headers.Accept", "application/json")

    ApiHttpbinPost()\
        .set_json({"user_id":user_id})\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.server", "gunicorn/19.9.0")\
        .validate("json().url", "http://127.0.0.1/post")\
        .validate("json().headers.Accept", "application/json") \
        .validate("json().json.user_id", "adk129")

