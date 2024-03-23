class QuestionManager:
    @staticmethod
    def create_question_table(cursor, conn):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                correct_option TEXT
            )
        ''')
        conn.commit()
    @staticmethod
    def fetch_questions_from_database(cursor):
        cursor.execute("SELECT question, option1, option2, option3, option4, correct_option FROM quiz_questions")
        return cursor.fetchall()

    @staticmethod
    def insert_question(cursor, conn, question, options, correct_option):
        cursor.execute('''
            INSERT INTO quiz_questions (question, option1, option2, option3, option4, correct_option)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, *options, correct_option))
        conn.commit()

    #@staticmethod
    #def fetch_questions_from_database(cursor):
    #   cursor.execute("SELECT question, option1, option2, option3, option4, correct_option FROM quiz_questions")
    #    return cursor.fetchall()*/
    #  @staticmethod
    # def fetch_questions_from_database(cursor):
    #     cursor.execute("SELECT question, option1, option2, option3, option4, correct_option FROM quiz_questions")
    #     return cursor.fetchall()
