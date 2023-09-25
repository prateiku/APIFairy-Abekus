def sort_parameters_by_name(_item: dict) -> dict:
    item = _item['paths']
    for k, v in item.items():
        for method in ['get', 'post', 'put', 'patch', 'delete']:
            parameters = v.get(method, {}).get('parameters', [])
            sorted_parameters = sorted(parameters, key=lambda param: param.get('name', ''))
            v.setdefault(method, {})['parameters'] = sorted_parameters
    return _item