# -*- coding: utf-8 -*-
"""Score.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qz8i4DC8tGytEOiopI8LqyNTSzQpFmPL
"""

scores = input("請輸入一串成績(以空格分隔)：").split()

num_failures = 0
total_score = 0
max, min = int(Score[0]), int(Score[0])

for score in scores:
  score = int(score)
  total_score += score
  
  if score > max:
        max = score
    if score < min:
        min = score
  if score < 60:
    num_failures += 1

average_score = total_score / len(scores)
print("不及格數量：", num_failures)
print("平均值: ", average_score)
print("max: , min: ", max, min)
