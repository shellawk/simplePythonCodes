import pandas as pd

day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri']

unit_list = ['ALP Research Project II', 'ALP Land Evaluation', 'ALP 2411 Land Use Modelling', 'Introduction to Book Keeping and accounting','ALP 2409 GIS Application', 'Enterprenuership Skills']

time_range = ['7-10', '10-1', '1-4', '4-7']

mon_table = {
    time_range[0]: unit_list[5],
    time_range[1]: unit_list[5],
    time_range[2]: unit_list[5],
    time_range[3]: unit_list[5]
}

tue_table = {
    time_range[0]: unit_list[4],
    time_range[1]: unit_list[4],
    time_range[2]: unit_list[4],
    time_range[3]: unit_list[4]
}
wed_table = {
    time_range[0]: unit_list[0],
    time_range[1]: unit_list[0],
    time_range[2]: unit_list[0],
    time_range[3]: unit_list[0]
}

thu_table = {
    time_range[0]: unit_list[1],
    time_range[1]: unit_list[1],
    time_range[2]: unit_list[1],
    time_range[3]: unit_list[1]
}

fri_table = {
    time_range[0]: unit_list[3],
    time_range[1]: unit_list[3],
    time_range[2]: unit_list[3],
    time_range[3]: unit_list[3]
}

def get_day_table(day_dict):
    day_table = []
    for i in range(4):
        day_table.append(day_dict[time_range[i]])
    return day_table

table = pd.DataFrame({
   'Mon': get_day_table(mon_table),
   'tue': get_day_table(tue_table),
   'Wed': get_day_table(wed_table),
   'Thu': get_day_table(thu_table),
   'fri': get_day_table(fri_table)
})

print(table)