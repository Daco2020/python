from random import *
import time

team_one = ["박정현", "고민혁", "박진성", "이용우", "이태연", "이지현"]
team_two = ["김예슬", "박세용", "강태준", "유민혁", "김혜리", "이나은", "성주호"]
team_three = ["정소영", "김상훈", "길동화", "김태영", "오동녘어진이", "이재문", "최지웅"]
team_four = ["장도원", "강인웅", "홍유진", "황성재", "김성현", "성종호"]
team_five = ["원소연", "황주영", "제갈창민", "이유진", "김은찬", "구유진"]
team_six = ["김재호", "김동욱", "김은혜", "박재용", "유승재", "김유량", "염기욱"]

restart = False
while restart == False:
    name = input("\n당신의 이름은 무엇입니까?\n\n")

    if name in team_one:
        print("\n당신은 1조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_one)
        num = 1
        restart = True
        for order in team_one:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    elif name in team_two:
        print("\n당신은 2조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_two)
        num = 1
        restart = True
        for order in team_two:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    elif name in team_three:
        print("\n당신은 3조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_three)
        num = 1
        restart = True
        for order in team_three:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    elif name in team_four:
        print("\n당신은 4조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_four)
        num = 1
        restart = True
        for order in team_four:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    elif name in team_five:
        print("\n당신은 5조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_five)
        num = 1
        restart = True
        for order in team_five:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    elif name in team_six:
        print("\n당신은 6조 군요!\n발표 순서를 정해드릴게요.\n")
        shuffle(team_six)
        num = 1
        restart = True
        for order in team_six:
            print("{0}번 순서는 {1} 입니다.".format(num, order))
            num += 1
            time.sleep(1)

    else:
        print("\n이름을 찾을 수 없습니다. \n정확한 이름을 입력해주세요.\n")
        restart == False

input("\n그럼 즐거운 스터디 하세요! ╰(*°▽°*)╯\
    \nEnter를 누르면 프로그램이 종료됩니다.\n")
