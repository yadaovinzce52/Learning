student_dict ={
    'student': ['Angela','James', 'Lily'],
    'score': [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for(key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)