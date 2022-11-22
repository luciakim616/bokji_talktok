from bayes import bayes
#return 은 정책 번호이고, 컨솔에는 정책에 대한 정보를 출력합니다.
returns = bayes("저는 학자금 대출이 필요한 남자 대학생입니다.", verbose = False)

print(returns)