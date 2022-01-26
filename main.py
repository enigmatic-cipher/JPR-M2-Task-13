"""
Given two strings as input, string 1 has the correct answers of a MCQ paper and string 2 has the answers submitted by a student, calculate the score of the student. A correct answer gets 4 marks, a wrong answer gets -1 marks. Space in string 2 denotes that the question has not been attempted by the student.
Input-> 
String1="ABCBD" String2="ABDDD"
Output-> 10
"""

st1 = "ABCBD"
st2 = "ABDDD"
ln1 = len(st1)
ln2 = len(st2)
ln = 0
total = 0
if(ln1==ln2):
  ln = ln1
for i in range(0,ln):
  e1 = st1[i]
  e2 = st2[i]
  if (e2 == " "):
    total = total + 0
  elif(e1 == e2):
    total = total + 4
  elif(e1 != e2):
    total = total - 1
print(total)
