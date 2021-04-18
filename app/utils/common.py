from flask import request

def get_item_list(items, index):
    if index < len(items):
        return items[index]

    return None

def unpack_url_params():
    search = request.args.get('search')
    search = search if search else ''

    page = request.args.get('page')
    page = page if page else 1

    per_page = request.args.get('perPage')
    per_page = per_page if per_page else 15

    return search, page, per_page
