def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda k: k['price'], reverse=True)[:limit]


print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))
print(bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]))