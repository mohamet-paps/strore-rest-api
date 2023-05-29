from .item import items
stores = {
    1: {
        "name": "SambaShop",
        "address": "Ziguinchor",
        "items": [item for item in items.values() if item["store_id"] == 1]
    },
    2: {
        "name": "AmadouShop",
        "address": "Dakar",
        "items": [item for item in items.values() if item["store_id"] == 2]
    }
}
