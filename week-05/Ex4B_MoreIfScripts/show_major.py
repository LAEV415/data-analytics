# 1. Create a script named show_major.py that defines two variables for a student:
# student_name and student_major. The student_major variable will contain a
# code for the student’s major (e.g. ENG).

student_name = 'James Bond'
student_major = "BIOL"

# 2. Use the following table to create lookup logic to display the name of the major and
# location of the department’s office based on the major code:

major_info = {
    'BIOL' : ('Biology' , 'Science Bldg, Room 310'),
    'CSCI' : ('Computer Science' , 'Sheppard Hall, Room 314'),
    'ENG' : ('English' , 'Kerr Hall, Room 201'),
    'HIST' : ('History' , 'Kerr Hall, Room 114'),
    'MKT' : ('Marketing' , 'Westly Hall, Room 310')
}

print(f'With student major code {student_major}, the information associated is:' "\n"
      f'(Name of major) , (Department Office)')
match student_major:
    case 'BIOL':
        print(major_info['BIOL'])
    case 'CSCI':
        print(major_info['CSCI'])
    case 'ENG':
        print(major_info['ENG'])
    case 'HIST':
        print(major_info['HIST'])
    case 'MKT':
        print(major_info['MKT'])
    case other:
        print('<unknown> , <unknown>')
