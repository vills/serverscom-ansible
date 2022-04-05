# Copyright (c) 2020 Servers.com
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
from ansible_collections.serverscom.sc_api.plugins.module_utils.modules import (
    ScL2Segment,
)  # noqa


__metaclass__ = type


def test__listdict_to_set_trivial():
    assert ScL2Segment._listdict_to_set([]) == set()

def test__listdict_to_set_None():
    assert ScL2Segment._listdict_to_set(None) == set()

def test__set_to_listdict_trivial():
    assert ScL2Segment._set_to_listdict(set()) == []


def test_set_to_listdict_and_listdict_to_set():
    DATA1 = {"id": "foo", "mode": "native"}
    DATA2 = {"id": "bar", "mode": "trunk"}
    DATA = [DATA1, DATA2]
    res = ScL2Segment._set_to_listdict(ScL2Segment._listdict_to_set(DATA))
    assert DATA1 in res
    assert DATA2 in res
