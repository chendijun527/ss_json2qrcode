#!/usr/bin/env python

import argparse
import base64
import image
import json
import os.path
import qrcode


def get_json_from_path(path):
    with open(path, 'r') as f:
        json_data = f.read()
    return json_data

def json_to_uri(json_data):
    data = json.loads(json_data)
    uri = 'ss://' + base64.b64encode(data['server_password'][0][2] + ":" + data['server_password'][0][1] + "@" + data['server_password'][0][0])
    return uri

def generate_qrcode(uri, path):
    img = qrcode.make(uri)
    with open(path, 'w') as f:
        img.save(f)

def process(path):
    json_data = get_json_from_path(path)
    uri = json_to_uri(json_data)
    new_path = os.path.splitext(path)[0] + '.png'
    generate_qrcode(uri, new_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shadowsocks JSON to QRCode')
    parser.add_argument('-s', '--source', dest='path', help='JSON config')
    args = parser.parse_args()

    path = args.path
    if os.path.isfile(path) and os.path.splitext(path)[1] == '.json':
        process(path)
    
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                process(os.path.join(root, name))
