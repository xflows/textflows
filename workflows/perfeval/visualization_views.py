from django.shortcuts import render

def perfeval_display_summation(request,input_dict,output_dict,widget):
    if sum(input_dict['intList']) == input_dict['sum']:
        check = 'The calculation appears correct.'
    else:
        check = 'The calculation appears incorrect!'
    return render(request, 'visualizations/perfeval_display_integers.html',{'widget':widget,'input_dict':input_dict, 'output_dict':output_dict, 'check':check})


def eval_to_2d_table_view(request,input_dict,output_dict,widget):
    table_header_list = ['algorithm']
    table_data_list = ['']
    metric = input_dict['evaluation_metric']
    for inner in input_dict['eval_results'][0]:
        table_header_list.append(inner['y_name'])
    for inner in input_dict['eval_results']:
        table_row = [inner[0]['name']]
        for obj in inner:
            table_row.append(obj[metric])
        table_data_list.append(table_row)
    data = [table_header_list, table_data_list, metric]
    return render(request, 'visualizations/eval_to_2d_table.html',{'widget':widget,'data':data,'output_dict':output_dict})
