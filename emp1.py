employee=["Radha","Raman","Krishna","Ramesh"]
emp_id=[101,102,103,104]
emp_dept=["Delhi","Bhopal","Tirupati"]
print(len(employee))
print(emp_dept*3)
print(employee+emp_id+emp_dept)
del employee[3]
emp_dept.remove("Delhi")
employee.pop(2)
employee[0]="ravi"
employee.clear()