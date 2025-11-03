#marks = 30
#if (marks>33):
#    print("Failed")
#elif (marks>33 and marks<50):
#    print("appear for re-exam")
#elif (marks>50 and marks<90):
#    print("pass")
#elif (marks>=90):
#    print("A+ grade and top ranker")


marks = int(input("enter the marks"))

if marks < 33:
    print("Failed")
elif marks >= 33 and marks < 50:
    print("Appear for re-exam")
elif marks >= 50 and marks < 90:
    print("Pass")
elif marks >= 90:
    print("A+ grade and top ranker")

