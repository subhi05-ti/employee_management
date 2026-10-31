from fastapi import FastAPI
from employee import *
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Employee"}

@app.post("/add_employee")
def add(id:int,name:str,salary:int,age:int):
    return add_employee(id,name,salary,age)
    # employee = {
    #     "id":id,
    #     "name":name,
    #     "salary":salary,
    #     "age":age
    # }
    # employees.append(employee)
    # return{"message":"Employee added successfully","data":employee}

@app.delete("/delete_employee/{id}")
def remove(id:int):
    # for employee in employees:
    #     if employee["id"] == id:
    #         employees.remove(employee)
    #         return{"message":"Employee deleted successfully","data":employee}
    result = remove_employee(id)
    if result:
        return {"message":"employee deleted "}

    return{"message":"employee not found"}

@app.put("/update_employee/{id}")
def update(id:int,name:str,salary:int,age:int):
    # for employee in employees:
    #     if employee["id"] == id:
    #         employee["name"] = name,
    #         employee["salary"] = salary,
    #         employee["age"] = age
    #         return{"message":"employee updated successfully","data":employee}

    result = update_employee(id,name,salary,age)
    if result:
        return {"message":"employee updated"}

    return{"meaage":"employee not found"}

@app.get("/get_emplooyees/{id}")
def get(id:int):
    # for employee in employees:
    #     if employee["id"] == id:
    #         return{"message":"Employee found","data":employee}

    # return{"message":"Employee not found"}
    result = get_employee(id)
    if result:
        return{"message":"employee found","data":result}

    return{"message":"employee not found"}

@app.get("/get_all_employees")
def get_all():
    result = get_all_employees()

    if result:
        return result
    
    return{"message":"no employees found"}



