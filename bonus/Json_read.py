import json
with open("questions.json", "r") as file:
    content = file.read()
data = json.loads(content)
score = 0
for quesions in data:
    print(quesions["question_text"])
    for index , alternative in enumerate(quesions["alternative"]):
        print(f"{index+1}-{alternative}")
    answer = input("Enter the aswer: ")
    quesions["user_answer"] = int(answer)


for index , quesion in enumerate(data):
    if quesion["user_answer"] == quesion["correct_answer"]:
        score +=1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index+1}- {result} Your answer: {quesion['user_answer']} , corrct_answer : {quesion['correct_answer'] }"
    print(message)
print(score ,"/", len(data))

