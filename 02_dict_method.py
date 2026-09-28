marks = {
      "Harry": 100,
      "Anamika": 56,
      "Rohan": 23,
       0: "Harry" 
}
# print(marks.keys())

# print(marks.items())

# print(marks.values())

marks.update({"Anamika":96, "Ravi": 80})
print(marks)

print(marks.get("Anamika"))

# print(marks.get("Anamika")) -- prints none
# print(marks["Anamika"]) -- Returns an error