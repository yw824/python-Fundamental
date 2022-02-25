# https://runebook.dev/ko/docs/pygame/ref/time#pygame.time.Clock
# 이벤트 관련 링크 : 
# https://kkamikoon.tistory.com/entry/PyGame-%EC%9D%B4%EB%B2%A4%ED%8A%B8-pygameKEYDOWN-pygameKEYUP
import pygame, sys, time, random

# 블록 진행 속도
speed = 15

#windows sizes
frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()
# check_errors 출력하면 (5, 0) 이라는 2차원 튜플 출력됨

# 아마도 check_errors[1] 값이 0이면 정상 실행된 것이고, 
# 양수이면 오류가 발생하여 정상적 실행이 되지 않은 것일듯
if(check_errors[1]>0):
    print("Error "+check_errors[1])
else:
    print("Game Sucessfully Initiated")

#initialize game windows
# 제목 바의 프로그램 이름을 설정하는 코드인 듯
pygame.display.set_caption("Snake Game")

# 실행할 프로그램의 가로, 세로 크기를 설정하는 코드
# set_mode (size = (0, 0), flags = 0, depth = 0, display = 0, vsync = 0)
# X좌표 위치, Y좌표 위치는 묶어 하나의 튜플로 전달
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

#colors : R-G-B 값
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# 시간을 추적하는 데 도움이 되는 시계 객체 만들기
# 시계는 게임의 프레임 속도를 제어하는 데 도움이 되는 몇 가지 기능도 제공
fps_controller = pygame.time.Clock()

# one snake square size
square_size = 20

# 초기 설정
# global : 함수에서 전역변수 선언
def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT" # 초기 방향 = 오른쪽
    head_pos = [120,60] # snake_body의 가장 앞 머리의 위치
    snake_body=[[120, 60]] # 아마 한칸씩 계속 뒤에 더해가는듯 

    #food 위치 : 1부터 전체 인덱스(전체크기/사각형크기로 구함) 사이에 랜덤으로 위치 설정 
    # //연산자 : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    food_pos = [random.randrange(1,frame_size_x//square_size)*square_size, 
                random.randrange(1,frame_size_y//square_size)*square_size]

    food_spawn = True
    score = 0

# 앞에서 성공적으로 실행되었다면 초기 설정값 설정하여 게임 시작하도록 설정
init_vars()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size) # 시스템 글꼴에서 Font 객체를 만든다.
    # pygame.font.SysFont.render : 새로운 표면에 텍스트를 그린다. 
    # 그릴 객체에 폰트는 저장되어 있으니 내용 및 색깔을 더해 표시하기
    score_surface = score_font.render("Score : "+str(score), True, color)
    # pygame.Surface.get_rect() : 
    # 표면의 직사각형 영역을 얻는다.
    score_rect = score_surface.get_rect()

    # 164번째 줄
    # 1을 인자로 보내줌 : 게임 시스템 내에서 요청되었다는 표시
    if choice == 1 : # 점수 텍스트가 들어갈 사각형 객체의 중간 위값 설정
        score_rect.midtop = (frame_size_x/10, 15)
    else: # 점수 텍스트가 들어갈 사각형 객체의 중간 위값 설정 = 중앙 인근에 표시 : 다른 경우에??
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)

    game_window.blit(score_surface, score_rect)


# game loop

while True:
    # pygame.event.get(): 현재 게임상에서 발생하는 모든 이벤트를 
    # 무한루프로 갱신하여 계속 받기
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # pygame.QUIT : 모든 파이 게임 모듈들을 초기화 해제
            sys.exit() # 실행중인 코드를 종료하는 코드 : 컴파일러에게 파일 종료 명령 전달
        
        # 키보드를 누른 후 뗄 때 발생함
        elif event.type == pygame.KEYDOWN: 
            # ord 함수 : 하나의 유니코드 문자를 나타내는 문자열이 주어지면 
            # 해당 문자의 유니코드 코드 포인트를 나타내는 정수를 돌려줍니다(파이썬 내장함수)
            if( event.key == pygame.K_UP or event.key == ord('w') 
                and direction != 'DOWN'):
                direction = "UP" 
            elif( event.key == pygame.K_DOWN or event.key == ord('s') 
                and direction != 'UP'):
                direction = "DOWN" 
            elif( event.key == pygame.K_LEFT or event.key == ord('a') 
                and direction != 'RIGHT'):
                direction = "LEFT" 
            elif( event.key == pygame.K_RIGHT or event.key == ord('d') 
                and direction != 'LEFT'):
                direction = "RIGHT" 
            # 아직까지는 현재 상태 조건판단에 따라 문자열 편집 과정만 치르고 있음
            
    # 이 문자열로 실제 상태 변경은 여기서부터
    # 일단 머리 칸의 위치를 변경
    # head_pos[0] : 가로(LEFT/RIGHT) , head_pos[1] : 세로(UP/DOWN)
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    elif direction == "RIGHT": # else: 와 같다. 방향은 4개밖에 없으니까
        head_pos[0] += square_size

    # 밖으로 나갔을 때에 위치 변경 코드 작성
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size # 제일 오른쪽
    elif head_pos[0] > frame_size_x - square_size: 
        head_pos[0] = 0 # 제일 왼쪽
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size # 제일 위쪽
    elif head_pos[1] > frame_size_x - square_size:
        head_pos[1] = 0 # 제일 아래쪽
        
    # eating apple
    snake_body.insert(0, list(head_pos))# 앞에 한 칸 추가
    if(head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]): # 먹었을 떄 맨 뒤 안떙기기(길이추가)
        score += 1
        food_spawn = False # 있던 음식칸 상태 없음으로 변경
    else: # 먹지 않았을 때
        snake_body.pop() # 맨 뒤 인덱스 삭제해서 한칸 움직인 만큼 땡기기
        
    # spawn food
    if not food_spawn:
        food_pos = [random.randrange(1,frame_size_x//square_size)*square_size, 
            random.randrange(1,frame_size_y//square_size)*square_size]
        food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body: # game_window 안에 green색깔로 사각형 그리기
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0] + 2, pos[1] + 2, # 위치해야 하는 위치부터 margin 2 부여(크기는 상대적으로 작아짐)
            square_size -2, square_size -2 )) # square_size-2의 크기만큼 색칠하기
    
    # 설정된 위치로 food 블록을 게임에 출력
    pygame.draw.rect(game_window, red, pygame.Rect(
        food_pos[0], food_pos[1], square_size, square_size))
        
    #game over condition
    
    for block in snake_body[1:]: # 만약 머리와 뒤 몸통이 부딪히면 다시 시작
        if(head_pos[0] == block[0] and head_pos[1] == block[1]):
            init_vars() # 초기화
        
    # 1을 인자로 보내줌 : 게임 시스템 내에서 요청되었다는 표시
    show_score(1, white, 'consolas', 20) # score 출력

    # 소프트웨어 디스플레이 화면 업데이트( 변경된 일부분만 )
    # 추가 ) flip함수는 전체 영역을 업데이트
    pygame.display.update()
    # pygame.time.Clock() : 초당 speed 프레임만큼 초과하여 실행되지 않는다.
    fps_controller.tick(speed)
