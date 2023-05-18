from utils.display import delay_print
import time
import random
import sys
import os

def initial_display():
    print("="*30)
    print("< 동물팡 >에 오신 것을 환영합니다!")
    animals = ["여우", "호랑이", "강아지"]
    for index, animal in enumerate(animals):
        print(f"[{index+1}] {animal}\t", end="")
        
    while True:
        try:
            selected_num = int(input('\n플레이할 "동물"의 번호를 선택하세요: '))
            user_animal = animals[int(selected_num)-1]
        except ValueError:
            print("잘못된 값입니다.")
        except IndexError:
            print("잘못된 번호입니다.")
        except Exception as e:
            print(e)
        else:
            user_name = input("이름을 입력해주세요: ")
            break
    print(f"[{selected_num}] {user_animal} 을(를) 선택했습니다.")
    print(f"{user_name} 님 환영합니다!")
    return user_animal

class Animal:
    def __init__(self, name, types, move, EVs, HP="===================="):
        self.name = name
        self.types = types
        self.move = move
        self.attack = EVs["공격력"]
        self.defense = EVs["방어력"]
        self.evasion = round(random.uniform(0.1, 0.3), 4)
        self.HP = HP
        self.bars = 20
        
def create_animal(animal):
    if animal == "여우":
        return Animal("여우", "풀", ["태클", "머리박치기", "풀망치"], {"공격력": 2, "방어력": 4})
    elif animal == "호랑이":
        return Animal("호랑이", "불", ["방울빔", "머리박치기", "불꽃펀치"], {"공격력": 3, "방어력": 3})
    elif animal == "강아지":
        return Animal("강아지", "물", ["방울빔", "태클", "물폭탄"], {"공격력": 4, "방어력": 2})
    
def initial_fight(home_animal, away_animal):
    print("========== 전투 시작 !! ==========")
    print(f"\n{home_animal.name}")
    print("타입/", home_animal.types)
    print("공격력/", home_animal.attack)
    print("방어력/", home_animal.defense)
    print("회피율/", home_animal.evasion)
    print("\nVS\n")
    print(f"\n{away_animal.name}")
    print("타입/", away_animal.types)
    print("공격력/", away_animal.attack)
    print("방어력/", away_animal.defense)
    print("회피율/", away_animal.evasion)
    
    attrs = ["풀", "불", "물"]
    string_1_attack = ""
    string_2_attack = ""
    for index, value in enumerate(attrs):
        if home_animal.types == value:
            if home_animal.types == value:
                string_1_attack = "\n효과가 적다."
                string_2_attack = "\n효과가 적다."
                
            if away_animal.types == attrs[(index+1)%len(attrs)]:
                away_animal.attack *= 2
                away_animal.defense *= 2
                string_1_attack = "\n효과가 없다.."
                string_2_attack = "\n효과가 있다!"
                
            if away_animal.types == attrs[(index+2)%len(attrs)]:
                home_animal.attack *= 2
                home_animal.defense *= 2
                string_1_attack = "\n효과가 있다!"
                string_2_attack = "\n효과가 없다.."
    fight(home_animal, away_animal, string_1_attack, string_2_attack)
    
def fight(home_animal, away_animal, string_1_attack, string_2_attack):
    while(home_animal.bars > 0 and away_animal.bars > 0):
        print(f"\n[유저][{home_animal.name}]\t{home_animal.HP}")
        print(f"[상대][{away_animal.name}]\t{away_animal.HP}\n")
        turn(home_animal, away_animal, string_1_attack, True)
        turn(away_animal, home_animal, string_2_attack, False)
        
def turn(home_animal, away_animal, effective, is_user):
    if is_user:
        print(f"{home_animal.name}!")
    else:
        print(f"{home_animal.name}이 공격해 온다!")
        
    for index, value in enumerate(home_animal.move):
        print(f"[{index+1}] {value}")   
    
    if is_user:
        while True:
            try:
                move_index = int(input("공격을 선택하세요: "))
                if move_index-1 in range(len(home_animal.move)):
                    break
                else:
                    print("올바른 숫자를 입력해주세요.")
            except:
                print("숫자만 입력 가능합니다.")
    else:
        move_index = random.randint(0, 2)
    delay_print(f"\n{home_animal.name}! {home_animal.move[move_index-1]} 공격!")
    time.sleep(1)
    
    if random.uniform(0, 1) < away_animal.evasion:
        delay_print(f"\n공격이 빗나갔습니다!")
    else:
        delay_print(effective)
        away_animal.bars -= home_animal.attack - (0.3 * away_animal.defense)
        
    away_animal.HP = ""
    
    for _ in range(int(away_animal.bars)):
        away_animal.HP += "="
        
    time.sleep(1)
    os.system("clear")
    
    if away_animal.bars <= 0:
        delay_print(f"\n[{home_animal.name}] 승리...")
        delay_print(f"\n[{away_animal.name}] 패배...")
        sys.exit(0)
    
if __name__ == "__main__":
    user_animal = create_animal(initial_display())
    other_animal = create_animal("호랑이")
    
    initial_fight(user_animal, other_animal)

