import tkinter as tk
from tkinter import ttk

students = []

def addstudent():
    name = entryname.get()
    enrollment = entryenrollmentnumber.get()
    branch = boxbranch.get()
    semester = boxsemester.get()
    marks = entrymarks.get()
    if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
        return
    if name == "" or enrollment == "" or branch == "" or semester == "" or marks == "":
        return
    student = {"name": name, "enrollment": enrollment, "branch": branch, "semester": semester, "marks": marks}
    students.append(student)
    tabletop.insert("", "end", values=(name, enrollment, branch, semester, marks))

def clear():
    entryname.delete(0, tk.END)
    entryenrollmentnumber.delete(0, tk.END)
    boxbranch.set("")
    boxsemester.set("")
    entrymarks.delete(0, tk.END)

def selectstudent(event):

    selected = tabletop.selection()

    if selected:
        values = tabletop.item(selected[0], "values")

        entryname.delete(0, tk.END)
        entryname.insert(0, values[0])

        entryenrollmentnumber.delete(0, tk.END)
        entryenrollmentnumber.insert(0, values[1])

        boxbranch.set(values[2])

        boxsemester.set(values[3])

        entrymarks.delete(0, tk.END)
        entrymarks.insert(0, values[4])

def deletestudent():

    selected = tabletop.selection()

    if selected:
        values = tabletop.item(selected[0], "values")
        enrollment = values[1]

        for student in students:
            if student["enrollment"] == enrollment:
                students.remove(student)
            break

        tabletop.delete(selected[0])

def updatestudent():

    selected = tabletop.selection()

    if not selected:
        return

    values = tabletop.item(selected[0], "values")
    old_enrollment = values[1]

    name = entryname.get()
    enrollment = entryenrollmentnumber.get()
    branch = boxbranch.get()
    semester = boxsemester.get()
    marks = entrymarks.get()

    if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
        return

    if name == "" or enrollment == "" or branch == "" or semester == "" or marks == "":
        return

    for student in students:
        if student["enrollment"] == old_enrollment:
            student["name"] = name
            student["enrollment"] = enrollment
            student["branch"] = branch
            student["semester"] = semester
            student["marks"] = marks
            break

    tabletop.item(selected[0], values=(name, enrollment, branch, semester, marks))

def searchstudent():
    search = entryserch.get()

    for item in tabletop.get_children():
        tabletop.delete(item)

    for student in students:
        if search == student["enrollment"]:
            tabletop.insert("", "end", values=(student["name"], student["enrollment"], student["branch"], student["semester"], student["marks"]))

dark_navy = "#1E293B"
white = "#FFFFFF"
slate_gray = "#CBD5E1"
very_light_gray = "#F8FAFC"
green = "#16A34A"
blue ="#2563EB"
red ="#DC2626"

window = tk.Tk()
window.title("Student Management System")
window.geometry("1000x650")
window.columnconfigure(0, weight=35)
window.columnconfigure(1, weight=65)

frameheader = tk.Frame(window, bg=dark_navy)
frameheader.grid(row=0, column=0, columnspan=2, sticky="ew")

labelheader = tk.Label(frameheader, text="Student Management System", font=("Arial", 26, "bold"), bg=dark_navy, fg=white)
labelheader.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

labelsubheader = tk.Label(frameheader, text="Manage student records efficiently", font=("Arial", 14), bg=dark_navy, fg=slate_gray)
labelsubheader.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

frameleft = tk.Frame(window, bg=very_light_gray)
frameleft.grid(row=1, column=0, sticky="nsew")

labellefthead = tk.Label(frameleft, text="Student Details", font=("Arial", 19, "bold"), bg=very_light_gray, fg=dark_navy)
labellefthead.grid(row=0, column=0, padx=10, pady=5)

labelname = tk.Label(frameleft, text="Name", font=("Arial", 13), bg=very_light_gray, fg=dark_navy)
labelname.grid(row=1, column=0, padx=10, pady=5)

entryname = tk.Entry(frameleft, font=("Arial", 13), width=25)
entryname.grid(row=2, column=0, padx=10, pady=5)

labelenrollmentnumber = tk.Label(frameleft, text="Enrollment Number", font=("Arial", 13), bg=very_light_gray, fg=dark_navy)
labelenrollmentnumber.grid(row=3, column=0, padx=10, pady=5)

entryenrollmentnumber = tk.Entry(frameleft, font=("Arial", 13), width=25)
entryenrollmentnumber.grid(row=4, column=0, padx=10, pady=5)

labelbranch = tk.Label(frameleft, text="Branch", font=("Arial", 13), bg=very_light_gray, fg=dark_navy)
labelbranch.grid(row=5, column=0, padx=10, pady=5)

boxbranch = ttk.Combobox(frameleft, values=["Computer Science and Engineering (CSE)", "Electronics & Communication (ECE)","Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Chemical Engineering"], font=("Arial", 13), state="readonly", width=25)
boxbranch.grid(row=6, column=0, padx=10, pady=5)

labelsemester = tk.Label(frameleft, text="Semester", font=("Arial", 13), bg=very_light_gray, fg=dark_navy)
labelsemester.grid(row=7, column=0, padx=10, pady=5)

boxsemester = ttk.Combobox(frameleft, values=[1, 2, 3, 4, 5, 6, 7, 8], font=("Arial", 13), state="readonly", width=25)
boxsemester.grid(row=8, column=0, padx=10, pady=5)

labelmarks = tk.Label(frameleft, text="Marks", font=("Arial", 13), bg=very_light_gray, fg=dark_navy)
labelmarks.grid(row=9, column=0, padx=10, pady=5)

entrymarks = tk.Entry(frameleft, font=("Arial", 13), width=25)
entrymarks.grid(row=10, column=0, padx=10, pady=5)

buttonadd = tk.Button(frameleft, text="ADD", font=("Arial", 12, "bold"), bg=green, fg=white, command=addstudent)
buttonadd.grid(row=11, column=0, padx=10, pady=5)

buttonupdate = tk.Button(frameleft, text="UPDATE", font=("Arial", 12, "bold"), bg=blue, fg=white, command=updatestudent)
buttonupdate.grid(row=12, column=0, padx=10, pady=5)

buttondelete = tk.Button(frameleft, text="DELETE", font=("Arial", 12, "bold"), bg=red, fg=white, command=deletestudent)
buttondelete.grid(row=13, column=0, padx=10, pady=5)

buttonclear = tk.Button(frameleft, text="CLEAR", font=("Arial", 12, "bold"), bg=slate_gray, fg=dark_navy, command=clear)
buttonclear.grid(row=14, column=0, padx=10, pady=5)

frameright = tk.Frame(window, bg=very_light_gray)
frameright.grid(row=1, column=1, sticky="nsew")
frameright.columnconfigure(0, weight=1)
frameright.rowconfigure(2, weight=1)

labelrighthead = tk.Label(frameright, text="Student Records", font=("Arial", 19, "bold"), bg=very_light_gray, fg=dark_navy)
labelrighthead.grid(row=0, column=0, padx=10, pady=5)

entryserch = tk.Entry(frameright, font=("Arial", 12), width=25, bg=white)
entryserch.grid(row=1, column=0, padx=10, pady=0, sticky="w")

buttonsearch = tk.Button(frameright, text="SEARCH", font=("Arial", 12, "bold"), bg=blue, fg=white, command=searchstudent)
buttonsearch.grid(row=1, column=0, padx=10, pady=5, sticky="e")

columns = ("Name", "Enrollment No.", "Branch", "Semester", "Marks")

tabletop = ttk.Treeview(frameright, columns=columns, show="headings")
tabletop.heading("Name", text="Name")
tabletop.heading("Enrollment No.", text="Enrollment No.")
tabletop.heading("Branch", text="Branch")
tabletop.heading("Semester", text="Semester")
tabletop.heading("Marks", text="Marks")
tabletop.column("Name", width=150)
tabletop.column("Enrollment No.", width=150)
tabletop.column("Branch", width=200)
tabletop.column("Semester", width=100)
tabletop.column("Marks", width=100)
tabletop.grid(row=2, column=0, padx=10, pady=0, sticky="nsew")

scrollbar = ttk.Scrollbar(frameright, orient="vertical", command=tabletop.yview)
scrollbar.grid(row=2, column=1, sticky="ns")
tabletop.configure(yscrollcommand=scrollbar.set)
tabletop.bind("<<TreeviewSelect>>", selectstudent)

window.mainloop()