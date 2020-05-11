import requests
import copy


documents_url = "https://raw.githubusercontent.com/omni-us/coding-challenges-resources/master/python-developer/api-response.json"
response = requests.get(documents_url)
documents_json = response.json()


# Problem 1
def get_docs_quantity_by_status():
    statuses_dict={}
    try:
        keys = []
        values = []
        for data_item in documents_json['payload']['items']:
       
            if data_item['status'] not in keys:
                keys.append(data_item['status'])
                values.append(1)
            else:
                item_index = keys.index(data_item['status'])
                values[item_index] = values[item_index] + 1

        for key, val in zip(keys, values):
            statuses_dict[key]=val

    except KeyError:
        pass
    finally:
        return statuses_dict


# Problem 2
def get_doc_details_by_status(status):
    status_details_list=[]
    try:
        for data_item in documents_json['payload']['items']:
            if data_item['status'] == status:
                status_details_dict = copy.deepcopy(data_item)
                del status_details_dict['status']
                status_details_list.append(status_details_dict)

    except KeyError:
        pass
    finally:
        if len(status_details_list) == 0:
            return {}
        else:
            return status_details_list


# Problem 3
def get_doc_details_by_filename(filename):
    file_details_dict={}
    try:
        for data_item in documents_json['payload']['items']:
            if data_item['file_name'] == filename:
                file_details_dict = copy.deepcopy(data_item)
                del file_details_dict['file_name']     
                return(file_details_dict)

    except KeyError:
        pass
    finally:
        return file_details_dict


if __name__ == "__main__":
    get_docs_quantity_by_status()
    get_doc_details_by_status('VALIDATED')
    get_doc_details_by_filename('77.pdf')
