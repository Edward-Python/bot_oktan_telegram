import tkinter as tk
from tkinter import ttk

from app.database.models import OktanBD


class ClientOktanDB(tk.Frame):

    def __init__(self, win):
        super().__init__(win)
        self.init_info()
        self.btn()
        self.tree_view()
        self.db = OktanBD()
        self.output()

    def init_info(self):
        self.fr = ttk.Frame().pack(padx=0, pady=26)
    
    def btn(self):
        ttk.Button(self.fr, text="Обновить", command=self.output)\
            .place(x=10, y=13)
        ttk.Button(self.fr, text="Удаление", command=self.delete_data_base)\
            .place(x=130, y=13)
        ttk.Button(self.fr, text="Выход", command=win.destroy)\
            .place(x=400, y=13)
        
    def tree_view(self):
        list_anim = ["id", "name", "username"]
        list_head = ["ID", "Name", "Username"]
        dict_list = dict(zip(list_anim, list_head))
        self.tree = ttk.Treeview(self, columns=(list_anim),\
                                height=26, show="headings")
        self.tree.column("id", width=40, anchor=tk.CENTER)
        for i in list_anim[1:]:
            self.tree.column(i, width=140, anchor=tk.CENTER)
        for k, v in dict_list.items():
            self.tree.heading(k, text=v)
        self.tree.pack(expand=True, fill="both")

    def output(self):        
        self.db.cur.execute("SELECT * FROM data_table")
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in self.db.cur.fetchall():
            self.tree.insert("", "end", values=i)
        
    def delete_data_base(self):
        for j in self.tree.selection():
            self.db.cur.execute("""DELETE FROM data_table WHERE
                                id==?""", (self.tree.set(j, "#1"),))
            self.db.db.commit()
            self.tree.delete(j)


if __name__ == "__main__":   
    win = tk.Tk()
    app = ClientOktanDB(win)
    app.pack()
    win.title("Клиенты СТО Октан")
    win.geometry("520x640+420+180")
    win.resizable(False, False)
    _font = ("JetBrains", "11")
    style = ttk.Style()
    style.configure(win, font=_font, foreground="#222540")
    win.mainloop()