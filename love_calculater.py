name1 = input("WHAT IS YOUR NAME ?")
name2 = input("WHAT IS HIS/HER NAME ?")

combine_string = name1 + name2

lower_case_string = combine_string.lower()

t = lower_case_string.count('t')

r = lower_case_string.count('r')

u = lower_case_string.count('u')

e = lower_case_string.count('e')

true = t + r + u + e

L = lower_case_string.count('L')

o = lower_case_string.count('o')

v = lower_case_string.count('v')

e = lower_case_string.count('e')

Love = L + o + v + e

Love_score = int(str(true) + str(Love))

if Love_score < 10 or Love_score > 90:
    print(f"YOUR LOVE_SCORE IS {Love_score} VERY VERY BEUTIFUL :")
elif Love_score >= 40 or Love_score <= 50:
    print(f"YOUR LOVE SCORE IS {Love_score} BEUTIFUL :")
else:
    print(f"YOUR LOVE_SCORE IS {Love_score} :")
