import random
import cv2
li1 = []
li2 = []
check_li = []
check_li2 = []

before_state = []
current_state = []
count = 0

for i in range(0,5):
    li1.append(random.randint(0,1))
    li2.append(random.randint(0,1))
    check_li.append(li1[i])
    check_li2.append(li2[i])

li1.append(li2)


class game1:
    def __init__(self,select):
        self.select = select

    def select_stair(self):
        while(True):
            global count, before_state, current_state, check_li, check_li2

            if(self.select == "위"):
                up_input = int(input("(위)0~4 까지 입력하세요:"))



                before_state.append(up_input)
                current_state.append(up_input)
                count += 1

                #위에 이빨에 모든 값이 0일때 any함수로 False를 반환하는걸 체크후에 아래로 넘어가는 부분
                if(any(check_li) == False):
                    print("위에 값이 모두 0이므로 밑으로 넘어감")
                    self.select = "아래"

                #전에 입력한 값이랑 같으면 잘못됐다는 것을 알려주는 부분 
                if(count >= 2):
                    if(current_state[count-1] == before_state[count-2]):
                        print("똑같은 값을 입력하셨습니다 다시 입력하세요")


                if(li1[up_input] == 1):
                    print("입이 닫혔습니다.")
                    print("▽▽▽▽▽▽")
                    print("△△△△△△")
                    break
                elif(up_input > 4):
                    print("다시입력하세요")
                else:
                    print("통과하였습니다.")


            elif(self.select == "아래"):
                down_input = int(input("(아래)0~4 까지 입력하세요:"))


                before_state.append(down_input)
                current_state.append(down_input)
                count += 1


                if(any(check_li2) == False):
                    print("아래에 값이 모두 0이므로 위으로 넘어감")
                    self.select = "위"


                if(count >= 2):
                    if(current_state[count-1] == before_state[count-2]):
                        print("똑같은 값을 입력하셨습니다 다시 입력하세요")

                try:
                    if(li2[down_input] == 1):
                        print("입이 닫혔습니다.")
                        print("▽▽▽▽▽▽")
                        print("△△△△△△")
                        break
                    else:
                        print("통과하였습니다.")
                except IndexError:
                    if(down_input > 4):
                        print("다시입력하세요")


            elif(self.select == "x"):
                break

            else:
                print("잘못 선택하셨습니다 다시 시작하세요")
                break


def start_game():
    print("=====악어 이빨 복불복 게임=====")
    print("▽▽▽▽▽▽\n")
    print("△△△△△△")
    print("q를 눌러 게임을 진행하세요.")
    while(1):
        img = cv2.imread("open.png")
        img_mini = cv2.resize(img,(512,512))
        cv2.imshow("입연 악어", img_mini)
        key = cv2.waitKey(60)
        if(key == 113): 
            cv2.destroyAllWindows()
            break
    a.select_stair()


game_select = input("\n(위,아래) 이빨중 선택할 곳을 고르시오 <그만하고 싶으면 'x'를누르세요> :")
a = game1(game_select)



start_game()