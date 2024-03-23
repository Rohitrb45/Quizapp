import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
from question_manager import QuestionManager

class QuizApp:
    def __init__(self, master):
        self.master=master
        self.options = ["Option A", "Option B", "Option C", "Option D"]
        self.correct_option = None
        self.selected_option = tk.StringVar(value="")
        #self.questions_pool = []
        self.conn = sqlite3.connect("quiz_database.db")
        self.cursor = self.conn.cursor()
        self.questions_pool_size=0
        QuestionManager.create_question_table(self.cursor, self.conn)
        self.load_questions_into_database()

        self.questions_pool = QuestionManager.fetch_questions_from_database(self.cursor)

        self.current_question_index = 0
        
        self.player_scores = {'Player 1': 0, 'Player 2': 0}

        self.selected_questions = random.sample(self.questions_pool, len(self.questions_pool))

        self.display_question()

    # def __init__(self, master):
    #     self.conn = sqlite3.connect("quiz_database.db")
    #     self.cursor = self.conn.cursor()

    #     QuestionManager.create_question_table(self.cursor, self.conn)
    #     self.load_questions_into_database()

    #     self.current_question_index = 0
    #     self.player_scores = {'Player 1': 0, 'Player 2': 0}

    #     self.selected_questions = random.sample(self.questions_pool, len(self.questions_pool))

    #     self.display_question()

    #@staticmethod
    #def fetch_questions_from_database(cursor):
    #    cursor.execute("SELECT question, option1, option2, option3, option4, correct_option FROM quiz_questions")
    #    return cursor.fetchall()

    def load_questions_into_database(self):
        # Example questions and options
        questions_and_options = [
            ("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], "Paris"),
            ("What is the capital of India?",  ["Paris", "Berlin", "Delhi", "Madrid"], "Delhi"),
            ("What is the capital of Nepal?", ["Paris", "Kathmandu", "London", "Madrid"], "Kathmandu"),
            ("What is the capital of Spain?", ["Paris", "Berlin", "London", "Madrid"], "Madrid"),
            ("What is the capital of Germany?", ["Paris", "Berlin", "London", "Madrid"], "Berlin"),
            ("What is the capital of UK?", ["Paris", "Berlin", "London", "Madrid"], "London"),
            # Add more questions as needed
        ]

        for question_data in questions_and_options:
            question, options, correct_option = question_data
            QuestionManager.insert_question(self.cursor, self.conn, question, options, correct_option)

        self.questions_pool_size=len(questions_and_options)

        # Fetch questions from the updated database
        QuestionManager.fetch_questions_from_database(self.cursor)

    
    def display_question(self):
        if self.current_question_index < (self.questions_pool_size):
            question_data = self.selected_questions[self.current_question_index]
        
            question, option1, option2, option3, option4, correct_option = question_data
            options=[option1, option2, option3, option4]
            question_label = tk.Label(self.master, text=question)
            question_label.pack()

            var = tk.StringVar()
            checkbox1 = tk.Checkbutton(self.master, text=option1, variable=var, onvalue=option1, offvalue="")
            checkbox1.pack(anchor="w")
            
            
            checkbox2 = tk.Checkbutton(self.master, text=option2, variable=var, onvalue=option2, offvalue="")
            checkbox2.pack(anchor="w") 

            checkbox3 = tk.Checkbutton(self.master, text=option3, variable=var, onvalue=option3, offvalue="")
            checkbox3.pack(anchor="w")

            checkbox4 = tk.Checkbutton(self.master, text=option4, variable=var, onvalue=option4, offvalue="")
            checkbox4.pack(anchor="w")
            
            next_button = tk.Button(self.master, text="Next", command=lambda:self.check_answer(options,var))
            next_button.pack()

        else:
            self.show_final_scores()

    
        

    def check_answer(self,options,var):
        
        selected_option = None
        selected_option = var.get()
        
        #print("so=",selected_option)
        question_data = self.selected_questions[self.current_question_index]
        correct_option=question_data[5]
        #print("selected_option=",selected_option)
        #print("correct_option=",correct_option)
        
        if selected_option == correct_option:
            messagebox.showinfo("Correct!", "Your answer is correct!")
            self.update_score(1)
        else:
            messagebox.showinfo("Incorrect!", f"The correct answer is: {correct_option}")
            self.update_score(0)
        self.current_question_index += 1


        # Clear the current UI to display the next question
        for widget in self.master.winfo_children():
            widget.destroy()

        # Display the next question
        # self.display_question()
        # self.clear_widgets()
        self.display_question()

    def update_score(self, score):
        # Assuming you have a method to get the current player
        current_player = self.get_current_player()
        
        # Update the score for the current player
        self.player_scores[current_player] += score

    def get_current_player(self):
        # Example: Alternate between Player 1 and Player 2
        return 'Player 1' if self.current_question_index % 2 == 0 else 'Player 2'


    def show_final_scores(self):
        final_scores_text = "Final Scores:\n"
        for player, score in self.player_scores.items():
            final_scores_text += f"{player}: {score}\n"

        messagebox.showinfo("Quiz Completed", final_scores_text)

    def close_database_connection(self):
        self.conn.commit()
        self.conn.close()
    
