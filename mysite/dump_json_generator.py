catalog = [
    {
        "category": "motors", "items": [
            {"name": "Мотор", "specs": [("voltage","sv"), ("speed",10)]},
            {"name":"Мотор2", "specs":[("voltage", "sv"),("speed", 20)]}
        ]
    },
    {
        "category":"Props","items":[
        {"name":"Props","specs":[("Size", 25),("blades", 3)]}
    ]
    }
]

import json

print(json.dumps(catalog))
