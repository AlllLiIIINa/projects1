
def qs2html(qs_list):
    s = '<table>'
    for student in qs_list:
        s += f'<tr><td>{student.first_name}</td><td>{student.last_name}</td><td>{student.birthday}</td>' \
             f'<td>{student.email}</td><td>{student.phone}</td></tr>'
    s += '</table>'

    return s
