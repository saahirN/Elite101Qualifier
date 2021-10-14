import random

class Bot():

  def __init__(self):
    self.start = True
    self.user_response = ""
    self.topic = ""
  
  def Start(self):
    print("Hello, I am chatbot")
    self.topic = input("What would you like to talk about? ")
    self.topic = self.topic.upper()
  
  def talk(self):
    self.check_question()
    while(self.topic != "BYE"):
      if (self.topic == "VIDEO GAMES"):
          self.videoGameQuestion()
      elif(self.topic == "MOVIES"):
        self.movieQuestion()
      elif(self.topic == "BOOKS"):
        self.bookQuestion()
        
  def checkTopicSwitch(self):
    self.topic = self.topic.upper()
    self.user_response = self.user_response.upper()
    if ("VIDEO GAMES" in self.user_response):
      self.topic = "VIDEO GAMES"
    elif ("MOVIES" in self.user_response):
      self.topic = "MOVIES"
    elif ("BOOKS" in self.user_response):
      self.topic = "BOOKS"
    elif ("BYE" in self.user_response):
      self.topic = "BYE"
      print("Bye")
      exit()

  def videoGameQuestion(self):
    question_list = ['1', '2', '3']
    while(self.topic == "VIDEO GAMES"):
      question_number = random.choice(question_list)
      if(len(question_list) > 1):
        if (question_number == '1'):
          self.gameQuestions(1)
          question_list.remove('1')
        elif (question_number == '2'):
          self.gameQuestions(2)
          question_list.remove('2')
        elif (question_number == '3'):
          self.gameQuestions(3)
          question_list.remove('3')
      else:
          self.gameQuestions(int(question_list[0]))
          print("There are no more video game questions")
          self.topic = ''
          self.topic = input('Please choose a new topic: ')
          self.topic = self.topic.upper()
          self.checkTopicSwitch()

  def gameQuestions(self, questionNumber):
    if (questionNumber == 1):
      self.user_response = input("What is your favorite video game? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if("STARDEW VALLEY" in self.user_response):
        print("Stardew Valley is my favorite game too!")
      else:
        print("That's a great game! Good choice!")
    elif (questionNumber == 2):
      self.user_response = input("What console do you play on? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if ("NONE" in self.user_response):
        print("Ok")
      else:
        print("That's my favorite console too!")
    elif (questionNumber == 3):
      self.user_response = input("What genre of games do you like?")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if ("OPEN WORLD" in self.user_response):
        print("Open World games are also my favorite")
      else:
        print("That genre of games is fun!")
  
  def movieQuestion(self):
    question_list = ['1', '2', '3']
    while(self.topic == "MOVIES"):
      question_number = random.choice(question_list)
      if(len(question_list) > 1):
        if (question_number == '1'):
          self.movQuestions(1)
          question_list.remove('1')
        elif (question_number == '2'):
          self.movQuestions(2)
          question_list.remove('2')
        elif (question_number == '3'):
          self.movQuestions(3)
          question_list.remove('3')
      else:
          self.movQuestions(int(question_list[0]))
          self.user_response = self.user_response.upper()
          print("There are no more movie questions")
          self.topic = ''
          self.topic = input("Please choose a new topic: ")
          self.topic = self.topic.upper()
          self.checkTopicSwitch()

  def movQuestions(self, questionNumber):
    if (questionNumber == 1):
      self.user_response = input("What is your favorite movie? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if("2001: A SPACE ODYSSEY" in self.user_response):
        print("2001: A SPACE ODYSSEY is my favorite movie too :)")
      else:
        print("That's a great movie! Good choice!")
    elif (questionNumber == 2):
      self.user_response = input("Who is your favorite actor? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if ("NONE" in self.user_response):
        print("Ok")
      else:
        print("That's my favorite actor too!")
    elif (questionNumber == 3):
      self.user_response = input("What genre of movie do you like?")
      self.user_response = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if ("ACTION" in self.user_response):
        print("Action movies are also my favorite")
      else:
        print("That genre of movies is cool!")

  def bookQuestion(self):
    question_list = ['1', '2', '3']
    while(self.topic == "BOOKS"):
      question_number = random.choice(question_list)
      if(len(question_list) > 1):
        if (question_number == '1'):
          self.bQuestions(1)
          question_list.remove('1')
        elif (question_number == '2'):
          self.bQuestions(2)
          question_list.remove('2')
        elif (question_number == '3'):
          self.bQuestions(3)
          question_list.remove('3')
      else:
          self.bQuestions(int(question_list[0]))
          self.user_response = self.user_response.upper()
          print("There are no more book questions")
          self.topic = ''
          self.topic = input('Please choose a new topic: ')
          self.topic = self.topic.upper()
          self.checkTopicSwitch()

  def bQuestions(self, questionNumber):
    if (questionNumber == 1):
      self.user_response = input("What is your favorite book? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if("SCYTHE" in self.user_response):
        print("SYCTHE is my favorite book too!")
      else:
        print("That's a great book! Good choice!")
    elif (questionNumber == 2):
      self.user_response = input("Who is your favorite author? ")
      self.topic = self.topic.upper()
      self.user_response = self.user_response.upper()
      self.checkTopicSwitch()
      if ("RICK RIORDAN" in self.user_response):
        print("He's my favorite author too!")
      else:
        print("They're a good author!")
    elif (questionNumber == 3):
      self.user_response = input("What genre of book do you like? ")
      self.user_response = self.topic.upper()
      self.user_response = (self.user_response).upper()
      self.checkTopicSwitch()
      if ("MEMOIR" in self.user_response):
        print("Memoirs are also my favorite")
      else:
        print("That genre of books is great!")
  
  def check_question(self):
    breakpoint()
    System.
    print(self.user_response.index('?'))
    if (self.user_response[len(self.user_response) - 1] == "?"):
      print("This worked")
    

chatbot = Bot()
chatbot.Start()
chatbot.talk()