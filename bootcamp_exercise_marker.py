# Abdur-Raheem Lee <abdur-raheem@wethinkcode.co.za>

def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    listOfQuestions=[]
    questions_txt=open("questions.txt","r")
    if questions_txt.readable():
        questions=questions_txt.readlines()
        
        for question in questions:
            if question.strip():
                listOfQuestions.append(question.strip())
        return listOfQuestions
    return listOfQuestions



def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    incorrectlyAnswers=[]
    question_number=1
    for question in list_of_questions:
        solution=question.split(",")[1].strip()
        user_ans=display_question(question_number,question)
        if not is_correct_answer(solution,user_ans):
            incorrectlyAnswers.append(question)
        print()
        question_number=question_number+1
    return incorrectlyAnswers


def display_question(question_number, question):
    '''
    Displays a single question from the list of questions
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''
    qxn_split=question.split(",")
    print(str(question_number)+". "+qxn_split[0])
    
    for i in range(2,len(qxn_split)):
        print(qxn_split[i].strip())
    user_ans=input("Answer: ")
    while user_ans!="A" and user_ans!="a" and user_ans!="b" and user_ans!="B" and user_ans!="c" and user_ans!="C":
        user_ans=input("Enter correct input answer: ")
    return user_ans


def is_correct_answer(solution, user_answer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''
    if solution==user_answer.upper():
        return True
    return False


def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''
    return current_round+1


if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)
