from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("DBMS PROJECT")
        f = Frame(self.root, width=1920, height=60)
        f.pack(side=TOP)

        l1 = Label(f, text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman", 25))
        l1.pack(side=TOP)

        self.image = PhotoImage(file="1.png")

        l2 = Label(f, image=self.image)
        l2.pack(side=TOP)

        # variables
        self.var_rn = StringVar()
        self.var_cid = StringVar()
        self.var_cname = StringVar()
        self.var_dur = StringVar()
        # self.var_sem=StringVar()


        # enroll frame

        enroll_frame = Frame(root, bd=5, bg="gray", relief="sunken", width=760, height=450)
        enroll_frame.place(x=10, y=220)
        enroll_label = Label(enroll_frame, text="Enroll", font=("Times New Roman", 20), pady=15)
        enroll_label.place(x=330, y=0)

        # RollNo Label and Entry

        rn_label = Label(enroll_frame, text="Roll Number : ", font=("Arial", 15))
        rn_label.place(x=20, y=100)

        rn_entry = Entry(enroll_frame, textvariable=self.var_rn, width=15, font=("Arial", 15), relief="flat")
        rn_entry.place(x=190, y=100)

        # Course ID
        c_id_label = Label(enroll_frame, text="Course ID        : ", font=("Arial", 15))
        c_id_label.place(x=20, y=150)

        c_id_entry = Entry(enroll_frame,textvariable=self.var_cid, width=15, font=("Arial", 15), relief="flat")
        c_id_entry.place(x=190, y=150)

        # Course Name
        c_name_label = Label(enroll_frame, text="Course Name   : ", font=("Arial", 15))
        c_name_label.place(x=20, y=200)

        c_name_entry = Entry(enroll_frame,textvariable=self.var_cname, width=15, font=("Arial", 15), relief="flat")
        c_name_entry.place(x=190, y=200)

        # Duration
        dur_label = Label(enroll_frame, text="Duration(in hrs) : ", font=("Arial", 15))
        dur_label.place(x=20, y=250)

        dur_entry = Entry(enroll_frame,textvariable=self.var_dur, width=15, font=("Arial", 15), relief="flat")
        dur_entry.place(x=190, y=250)

        # # Semester
        # sem_label = Label(enroll_frame, text="Semester       : ", font=("Arial", 15))
        # sem_label.place(x=20, y=300)
        #
        # sem_combobox = ttk.Combobox(enroll_frame,textvariable=self.var_sem, font=("Arial", 15), width=15, state="readonly")
        # sem_combobox["value"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        # sem_combobox.current(0)
        # sem_combobox.place(x=190, y=300)

        # Buttons

        button_frame = Frame(root, bd=5, bg="gray", relief="sunken", width=760, height=50)
        button_frame.place(x=10, y=690)

        save_button = Button(button_frame, command=self.add_data, text="Save", font="Arial 12", width=20)
        save_button.grid(row=0, column=0)

        update_button = Button(button_frame,command=self.update_data,text="Update", font="Arial 12", width=20)
        update_button.grid(row=0, column=1)

        del_button = Button(button_frame,command=self.delete_data, text="Delete", font="Arial 12", width=20)
        del_button.grid(row=0, column=2)

        reset_button = Button(button_frame,command=self.reset_data,text="Reset", font="Arial 12", width=20)
        reset_button.grid(row=0, column=3)

        # Search Frame
        search_frame = Frame(root, bd=5, bg="gray", relief="sunken", width=740, height=100)
        search_frame.place(x=780, y=220)

        search_label = Label(search_frame, text="Search", font=("Times New Roman", 15, "bold"), pady=5)
        search_label.place(x=340, y=0)

        #searchby label
        searchby_label = Label(search_frame, text="Search By : ", font=("Arial", 15))
        searchby_label.place(x=5, y=50)
        #searchby combobox
        self.var_searchby = StringVar()
        search_combo11box = ttk.Combobox(search_frame,textvariable=self.var_searchby, font=("Arial", 15), width=15, state="readonly")
        search_combo11box["value"] = ("Select Option", "RollNo", "Department")
        search_combo11box.current(0)
        search_combo11box.place(x=130, y=50)

        #search_entry
        self.var_search = StringVar()
        search_entry = Entry(search_frame,textvariable=self.var_search, width=15, font=("Arial", 15), relief="flat")
        search_entry.place(x=330, y=50)

        #search button
        search_button = Button(search_frame,command=self.search_data, text="Search", font="Arial 13", width=10)
        search_button.place(x=510, y=50)
        #showall button
        showall_button = Button(search_frame,command=self.fetch_data ,text="Show All", font="Arial 13", width=10)
        showall_button.place(x=620, y=50)

        # Table Frame
        table_frame = Frame(root, bd=5, bg="gray", relief="sunken", width=740, height=350)
        table_frame.place(x=780, y=330)

        xsb = ttk.Scrollbar(table_frame, orient="horizontal")
        ysb = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table = ttk.Treeview(table_frame, columns=("rn", "cid", "cname", "dur"),
                                  xscrollcommand=xsb.set, yscrollcommand=ysb.set)
        # xsb.pack(side=BOTTOM,fill=X)
        # ysb.pack(side=RIGHT,fill=Y)
        xsb.place(x=0, y=325, width=740)
        ysb.place(x=720, y=0, height=350)

        xsb.config(command=self.table.xview)
        ysb.config(command=self.table.yview)

        self.table.heading("rn", text="Roll No")
        self.table.heading("cid",text="Course ID")
        self.table.heading("cname",text="Course Name")
        self.table.heading("dur",text="Duration")

        self.table["show"] = "headings"

        self.table.column("rn", width=150)
        self.table.column("cid", width=150)
        self.table.column("cname", width=150)
        self.table.column("dur", width=150)

        self.table.place(x=0, y=0, width=740, height=325)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

    #add data
    def add_data(self):
        if (self.var_cid.get() == "" or self.var_cname.get() == "" or self.var_rn.get() == "" or self.var_dur.get() == ""):
            messagebox.showerror("Error", "All fields are required.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                               database="student_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into enroll values(%s,%s,%s,%s)",
                                  (self.var_rn.get(),self.var_cid.get(),self.var_cname.get(),self.var_dur.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Info has been added!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}")


    #fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                       database="student_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from enroll")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self,event=""):
        cursor_row = self.table.focus()
        content = self.table.item(cursor_row)
        data = content["values"]

        self.var_rn.set(data[0])
        self.var_cid.set(data[1])
        self.var_cname.set(data[2])
        self.var_dur.set(data[3])

    #update data
    def update_data(self):
        if (self.var_cid.get() == "" or self.var_cname.get() == "" or self.var_rn.get() == "" or self.var_dur.get() == ""):
            messagebox.showerror("Error", "All fields are required.")
        else:
            try:
                update = messagebox.askyesno("Update","Are you Sure?",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                   database="student_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update enroll set Course_ID=%s,Course_name=%s,duration=%s,Semester=%s where Rollno=%s",(self.var_cid.get(),
                                                                                                                                self.var_cname.get(),
                                                                                                                                self.var_dur.get(),
                                                                                                                                self.var_rn.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student Data Updated Successfully!",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}")

    #delete
    def delete_data(self):
        if self.var_rn.get()=="":
            messagebox.showerror("Error","Cannot delete student data!")
        else:
            try:
                delete = messagebox.askyesno("Delete","Are you sure?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                   database="student_management")
                    my_cursor = conn.cursor()
                    sql="delete from enroll where ROLLNO=%s"
                    value=(self.var_rn.get(),)
                    my_cursor.execute(sql,value)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}")

    def reset_data(self):
        self.var_rn.set("")
        self.var_cid.set("")
        self.var_cname.set("")
        self.var_dur.set("")

    def search_data(self):
        if self.var_search=="" or self.var_searchby=="":
            messagebox.showerror("Error","Missing Inputs!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                               database="student_management")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from enroll where "+str(self.var_searchby.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()
                if len(data)!=0:
                    self.table.delete(*self.table.get_children())
                    for i in data:
                        self.table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}")



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
