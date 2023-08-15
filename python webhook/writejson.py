#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
