from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Siapkan list kosong untuk menampung object-object Question
question_bank = []
# Looping untuk mengambil data dan membuat object
for question in question_data:
    # Mengambil value dari dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Membuat object baru dari class Question
    new_question = Question(question_text,question_answer)

    # Memasukkan object tersebut ke dalam list question_bank
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.final_score()