def cleanup_query(query_params, sort):
    query_params = dict(query_params)
    if 'page' in query_params:
        del query_params['page']
    if 'limit' in query_params:
        del query_params['limit']
    if 'sort' in query_params:
        del query_params['sort']

    if sort not in ['cash', 'brand', 'model', 'year']:
        sort = {
            'updated': 'last_updated',
            'price': 'cash'
        }.get(sort, 'last_updated')

    return query_params, sort

def cleanup_query_modified(query_params, sort, order):
    query_params = dict(query_params)
    if 'page' in query_params:
        del query_params['page']
    if 'limit' in query_params:
        del query_params['limit']
    if 'sort' in query_params:
        sort = query_params['sort']
        del query_params['sort']
    if 'order' in query_params:
        order = query_params['order']
        del query_params['order']

    # if sort not in ['cash', 'brand', 'model', 'year']:
    #     sort = {
    #         'updated': 'last_updated',
    #         'price': 'cash'
    #     }.get(sort, 'last_updated')

    return query_params, sort, order