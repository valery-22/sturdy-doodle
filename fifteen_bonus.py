import copy

def salary_increment(employees):
    
    # implement this
    employees_copy = copy.deepcopy(employees)
    
    for employee in employees_copy:
        if employee['role'] == 'developer':
            employee['salary'] *= 1.15
            employee['salary'] = round(employee['salary'], 2)    
    
    return employees_copy

# Test cases

employees = [{
    'name': 'John',
    'role': 'developer',
    'salary': 50000
}, {
    'name': 'Mary',
    'role': 'developer',
    'salary': 70000
}, {
    'name': 'Jim',
    'role': 'manager',
    'salary': 85000
}]

print(salary_increment(employees))
# Expected output: [{'name': 'John', 'role': 'developer', 'salary': 57500}, 
#                   {'name': 'Mary', 'role': 'developer', 'salary': 80500.0},
#                   {'name': 'Jim', 'role': 'manager', 'salary': 85000.0}]