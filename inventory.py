#!/bin/python
import json

inventory = {}

inventory["webservers"] = {
    "hosts": ["server1.example.com", "server2.example.com"],
    "vars": {
        "package": "httpd",
        "service": "httpd"
    }
}

inventory["databases"] = {
    "hosts": ["server3.example.com", "server4.example.com"],
    "vars": {
        "package": "mariadb-server",
        "service": "mariadb"
    }
}

print(json.dumps(inventory, indent=2))
