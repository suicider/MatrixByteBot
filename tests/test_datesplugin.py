# -*- coding: utf-8 -*-
"""
Testing file for datesplugin.py
"""
from os.path import getmtime
from os import remove
from datetime import datetime, timedelta
from shutil import copyfile

from .helpers.mockups import MockBot, MockRoom

from ..plugins.datesplugin import DatesPlugin as TestPlugin

#def test_callback():
#    """make sure some text is returned"""
#    bot = MatrixBot("DummyName", "http://example.com")
#    test_plugin = TestPlugin("nametest", bot)
#    bot.add_plugin(TestPlugin("Test-Plugin", bot))
#
#    users_event = {'content':{'body':'!users'}}
#    users_event2 = {'content':{'body':'!Users'}}
#
#    status_event = {'content':{'body':'!Status'}}
#    status_event2 = {'content':{'body':'!status'}}
#
#    room = MockRoom()
#    test_plugin.users(room)
#    call = room.text_response
#    test_plugin.callback(room, users_event)
#    assert room.text_response == call
#    test_plugin.callback(room, users_event2)
#    assert room.text_response == call
#
#    test_plugin.status(room)
#    call = room.text_response
#    test_plugin.callback(room, status_event)
#    assert room.text_response == call
#    test_plugin.callback(room, status_event2)
#    assert room.text_response == call

def test_get_help():
    """make sure some text is returned"""
    bot = MockBot()
    test_plugin = TestPlugin("nametest", bot)
    assert len(test_plugin.get_help()) > 10
    assert len(test_plugin.get_help().split('\n')) == 2

def test_update_cache():
    """make sure some text is returned"""
    bot = MockBot()
    test_plugin = TestPlugin("nametest", bot)
    room = MockRoom()
    ## create a new empty file
    cache = open('tmp/dates.cache', "w", encoding='utf-8')
    cache.close()
    old = getmtime('tmp/dates.cache')
    test_plugin._update_cache(room)
    new = getmtime('tmp/dates.cache')
    assert new > old
    cache = open('tmp/dates.cache', "r", encoding='utf-8')
    assert len(cache.read()) > 100
    cache.close()
    remove('tmp/dates.cache')
    test_plugin._update_cache(room)
    cache = open('tmp/dates.cache', "r", encoding='utf-8')
    assert len(cache.read()) > 100
    cache.close()

def test_output_dates():
    """make sure some text is returned"""
    bot = MockBot()
    test_plugin = TestPlugin("nametest", bot)
    room = MockRoom()
    testtime = datetime.strptime('2018-10-28', '%Y-%m-%d')
    copyfile('tests/dates.example', 'tmp/dates.cache')
    test_plugin.output_dates(testtime, testtime + timedelta(days=21), 'Bytespeicher', room,)
    assert "Kennenlerntreffen" in room.text_response
    assert len(room.text_response.split('\n')) == 11
#
#def test_status():
#    """make sure some text is returned"""
#    bot = MatrixBot("DummyName", "http://example.com")
#    test_plugin = TestPlugin("nametest", bot)
#    room = MockRoom()
#    test_plugin.status(room)
#    assert "open" in room.text_response or "closed" in room.text_response
