def find(items, id):
    for elem in items:
        if elem['id'] == id:
            return elem


def gen_usr_id(items):
    id = 1
    if not items:
        return id

    for elem in items:
        if elem['id'] > id:
            id = elem['id'] + 1
        return id


def delete(items, id):
    for idx, elem in enumerate(items):
        if elem['id'] == id:
            del items[idx]
    return items
