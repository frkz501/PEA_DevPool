from flask import Flask

app =  Flask(__name__)

@app.route('/')
def shat():
    import re
    import pandas as pd

    try:
        student = pd.read_csv('student.csv')
    except:
        student = pd.DataFrame(columns=['Name', 'House'])
    
    name = str(input('Enter name(s) [seperated by commas]:'))
    house = ['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw']

    def whouse(name: str):
        vow = len(re.findall('[AEIOUaeiou\u0E30-\u0E45]', name))
        vow = vow % 4
        if len(student[student['House'] == house[vow]]) >= 12:
            print(f"Sorry, {name}, house {house[vow]} is full.")
            while len(student[student['House'] == house[vow]]) >= 12:
                if len(student[student['House'] == house[vow]]) == 12 and len(student) == 49:
                    # last student
                    print(f"But you're the last one so we will squeeze you in {house[vow]}.")
                    return house[vow]
                vow += 1
                if vow >= 4:
                    vow = 0
            print(f"We're assigning {name} to {house[vow]}.")
        return house[vow]
    
    print('Hmm...')
    if name.count(',') > 0:
        name = name.split(',')
    else:
        name = [name]
    for n in name:
        n = n.strip().lower().capitalize()
        n = re.sub(' +', ' ', n)
        if n == '':
            print('You entered a blank name, skipped.')
            continue
        if n in student['Name'].values:
            print(f"{n} is already in {student.loc[student['Name'] == n, 'House'].values[0]}!")
        else:
            if len(student) == 50:
                print(f"Houses are full! Sorry, {n}.")
                summary = student.groupby('House').count().reset_index()
                return summary.to_html(index=False) + '<body><br></body>' + student.to_html(index=False)
            student = pd.concat([student, pd.DataFrame({'Name': n, 'House': whouse(n)}, index=[0])], ignore_index=True)
            print(f"Congrats!\n{n} is in {student['House'][student['Name'] == n].values[0]}!")
    student.to_csv('student.csv', index=False)
    summary = student.groupby('House').count().reset_index()
    return summary.to_html(index=False) + '<body><br></body>' + student.to_html(index=False)
if __name__ == "__main__":
    # app.run("https://rocky-earth-45049.herokuapp.com/")
    app.run(host="127.0.0.1", port=8080, debug=True)
