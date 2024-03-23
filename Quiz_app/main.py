import tkinter as tk
from quiz_app import QuizApp

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
    app.close_database_connection()
