# Iterating over a list of dictionaries in a Jinja template

from jinja2 import Environment, FileSystemLoader

employee_list = [
    {"id": 1, "name": "Alice",  "age": 30},
    {"id": 2, "name": "Bobby", "age": 40},
    {"id": 3, "name": "Carl", "age": 50},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("home.html")

# 👇️ pass the list of dictionaries as a variable to the template
content = template.render(employee_list=employee_list)

print(content)