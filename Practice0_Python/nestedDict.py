

emp = {
    "Sales":{
        "emp001":{
        "name":"Ali",
        "position":"Manager",
        "salary":20000},
        "emp002":{
        "name":"Umer",
        "position":"Salesman",
        "salary":15000},
        "emp003":{
        "name":"Ahad",
        "position":"Salesman",
        "salary":240000}
    },

    "Finance":{
        "emp004":{
        "name":"Shaheer",
        "position":"Manager",
        "salary":20000},
        "emp002":{
        "name":"Umair",
        "position":"Director",
        "salary":1000000},
        "emp003":{
        "name":"Saleem",
        "position":"Accountant",
        "salary":84000}
    }
}

# print(emp["Sales"]["emp002"]["salary"])

# max salary

maxSalary=0

for dept in emp:
    for empid in emp[dept]:
        if emp[dept][empid]["salary"]>maxSalary:
            max_emp=emp[dept][empid].items()
            maxSalary=emp[dept][empid]["salary"]
            

print(max_emp)
