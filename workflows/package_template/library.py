import re

def pcktmp_create_integers(input_dict):
    intStr = input_dict['intStr']
    intList = []
    for i in re.findall(r'\w+', intStr):
        try:
            intList.append(int(i))
        except:
            pass
    if input_dict['sort'].lower() == "true":
        intList.sort()
    return {'intList':intList}

def pcktmp_sum_integers(input_dict):
    intList = input_dict['intList']
    return {'sum':sum(intList)}

def pcktmp_pre_filter_integers(input_dict):
    return input_dict

def pcktmp_post_filter_integers(postdata,input_dict,output_dict):
    intListOut = postdata['intListOut']
    intList = []
    for i in intListOut:
        try:
            intList.append(int(i))
        except:
            pass
    return {'intList': intList}

def pcktmp_pre_display_summation(input_dict):
    return {}