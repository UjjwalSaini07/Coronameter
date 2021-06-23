def start_test():
    answerlist = list()
    print('please note that the information from this chat'
          ' will be used for monitoring & management of the current'
          'health crisis and research in the fight against COVID-19.')
    print('----------------------------------------------------------')
    print('Are you experiencing any of the following symptoms ?\n'
          '1) Cough\n'
          '2) Fever\n'
          '3) Difficulty in Breathing\n'
          '4) Loss of the senses of smell and taste\n'
          '5) None of the above\n')
    user1 = int(input('>>> '))
    if 5 >= (user1) >= 1:
        answerlist.append((user1))
    else:
        print('invalid input, select the option number.\n')
    print('Have you ever heard of the following ?\n'
          '1) Diabetes\n'
          '2) Hypertension\n'
          '3) Lung Disease\n'
          '4) Heart Disease\n'
          '5) Kidney Disorder\n'
          '6) None of the above\n')
    user2 = int(input('>>> '))
    if 6 >= (user2) >= 1:
        answerlist.append((user2))
    else:
        print('invalid input, select the option number.\n')
    print('Have you travelled anywhere internationally in the last 28-45 days?\n'
          '1) yes\n'
          '2) no\n')
    user3 = int(input('>>> '))
    if 2 >= (user3) >= 1:
        answerlist.append((user3))
    else:
        print('invalid input, select the option number.\n')
    print("Which of the following apply to you ?\n"
          "1) i have recently interacted or lived with someone who has tested positive for COVID-19\n"
          "2) i am a healthcare worker and i examined a COVID-19 confirmed case without protective gear\n"
          "3) None of the above\n")
    user4 = int(input('>>> '))
    if 3 >= (user4) >= 1:
        answerlist.append((user4))
    else:
        print('invalid input, select the option number.')
    if user1 == 5 and user2 == 6 and user3 == 2 and user4 == 3:
        print("--------------------------Your Risk Test Result : By DoctorBuddy--------------------------")
        print("your infection risk is very low.\n"
              "we recommend that you stay at home to avoid any chance of exposure to the novel coronavirus\n"
              "retake the test if you develop symptoms or come in contact with a covid-19 confirmed patient.\n"
              "Thank you for taking the risk-test :)\n")
    else:
        print("--------------------------Your Risk Test Result : By DoctorBuddy--------------------------")
        print('if the information provided by you is accurate, it indicates that you are either unwell or at risk.\n'
              'please be a responsible citizen and protect yourself and your country from coronavirus panedemic\n'
              'by taking the physical covid-19 test from your nearest covid-19 test centers.\n'
              'Thank you for taking the risk-test :)')
#__main__
print("\t\t\t\t*    CoronaMeter : The DoctorBuddy    *")
print("\t\t\t\t* CoronaMeter : Offline Risk Predictor 2020 *")
print('Enter START to start the risk test now')
user = str(input('>>> '))
if user == 'START' or 'start':
    start_test()
else:
    print('Invalid Input Detected, Try Again :(')