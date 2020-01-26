import requests


output_dict = {}

def get_json_from_url(page_url):

    response = requests.get(page_url)
    page_json = response.json()
   
    return page_json


def add_value(key, value):
  
    try:
        if key != '':
            if key not in output_dict:
                output_dict.update({key: [value]})
            else:
                output_dict[key].append(value)
    except KeyError:
        pass


def out_flatten(dict_value, str_value):

    if type(dict_value) is dict: 
        for key in dict_value.keys():
            new_key = key
            if str_value: 
                new_key = str_value + '_' + key
            add_value(str_value, new_key)       
            out_flatten(dict_value[key], new_key) 
    elif type(dict_value) is list or type(dict_value) is set:
        for item in dict_value:
            out_flatten(item, str_value + '_' + item)
    else:
        add_value(str_value, dict_value)

    return output_dict


if __name__ == "__main__":

    json = get_json_from_url("https://raw.githubusercontent.com/omni-us/coding-challenges-resources/master/python-developer/sample-1.json")
    out_flatten(json, '')

    json = get_json_from_url("https://raw.githubusercontent.com/omni-us/coding-challenges-resources/master/python-developer/sample-2.json")
    out_flatten(json, '')

    json = get_json_from_url("https://raw.githubusercontent.com/omni-us/coding-challenges-resources/master/python-developer/sample-3.json")
    out_flatten(json, '')
