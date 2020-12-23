class Qusetion:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer==answer


# print(q1.checkAnswer('c#'))

class Quiz:
   
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
      
    
    def getQuestion(self):
        
        return self.questions[self.questionIndex]
        
    def displayQuestion(self):
        question= self.getQuestion()
        print(f"soru {self.questionIndex + 1} : {question.text}")
        
        for q in question.choices:
            print('-'+ q)

        answer =input('cevap: ')
        self.guess(answer)     #burası guess() metodunu çalıştırır. 
        self.loadQuestion()

    def guess(self,answer):
        question= self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex +=1
        
        

    def loadQuestion(self):
        if self.questionIndex==len(questions):
            print(f" test bitti scorunuz: {self.score} ".center(100,'*'))
        else:
            self.displayProgress()
            self.displayQuestion() # displayQuestion ve loadQuestion arasında döngü oluşturur.

    def showScore(self):
        print('score:  ',self.score)
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex  + 1

        if questionNumber > totalQuestion:
            print(f"test bitti scorunuz:  {self.score}".center(100,'*'))
        else:
            print(f"soru sayı {self.questionIndex + 1} of {totalQuestion}".center(100,'*'))






q1=Qusetion('en iyi programlama dili hangisidir?',['c#','python','javacript','java'],'python')
q2=Qusetion('en popüler programlama dili hangisidir?',['c#','python','javacript','java'],'python')
q3=Qusetion('en çok kazandıran programlama dili hangisidir?',['c#','python','javacript','java'],'python')
questions=[q1,q2,q3]

quiz=Quiz(questions)
#question=quiz.getQuestion()  #quiz.questions[quiz.questionIndex] >> bunu quiz clası içinde getQuestion methodu yaptık.
#print(question)  #questionIndex=0 için question=q1'dir. print q1'in adresini getirir.
#ancak içinden soruyu yani(text parametresini) çekersek q1'in sorusunu getirir:
#print(question.text)

quiz.loadQuestion()




