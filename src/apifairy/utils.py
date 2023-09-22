def parse_and_sort_util(json_obj, key_to_sort_by="name"):
    if isinstance(json_obj, list):
        if key_to_sort_by is not None and all(isinstance(item, dict) for item in json_obj):
            json_obj = sorted(json_obj, key=lambda x: x.get(key_to_sort_by, ""))
        for i, item in enumerate(json_obj):
            json_obj[i] = parse_and_sort_util(item, key_to_sort_by)
    elif isinstance(json_obj, dict):
        for key, value in json_obj.items():
            json_obj[key] = parse_and_sort_util(value, key_to_sort_by)
    return json_obj
