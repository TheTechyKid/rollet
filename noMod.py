# project.py

import random
from time import sleep

gameloop = True
health = 3
dealer_health = 3
dealers_turn = True
double_dealers_turn = 0
rounds_fired = 0

dealer_text = [
    """
*#################################################################*
#%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%#
@@@@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%@@@@@@@
..#@@@@@@@@@@%%%%%%%@@@@@@@@@@......@.@@@=@@@@@@@@@@@@@@@@@@@@@....
.........@@@@@@@@@@@@@..............+...........@@@@@@@@@@........@
@@@@@@+.........@@.....................:.@#++..@............@@@@@@@
#%%%%@@@@@@@.@@-........+@@%@@@@@@@+-........=*%@#@@..@@@@@@@%%%%@#
#%%%%%%@@@@@@...@@@@@@@@....#=@%#++-@..@--==++..........@@@@%%%@%%#
#%%%%%%@@@....@@@@@@@@@@:........=......@.:...=@@@@@.-....@@@%@%%%#
#%%%%@@@...@.@@@@%%%%@%@@.@.-.......@-.....................@@@%@%%#""", """
#%%%@@@..=@+@@@%%%%%%%%%@...+.............@@@@@@@@@@@@......@@@%%%#
#%%%@@..-..:@@@%%%%%%%@@@.---........=:.*@@@%%%%%%%%@@@:..@...@%@%#
#%@@@..*.@.@@%%%%%%%%%%@@...@........=..@@@%%%%%%%%%%%@@@...@.@@@%#
#%%@@..@..@@@%%%%%%%%@@@..=#........*..@@%%%%%%%%%%%%%@@@@@....@@%#
#%%@@..+@..@@@%%%%%%%%%@-.........%.:..@@%%%%%%%%%%%%%@%@@.@...@@@#
#@@@...#@@@@@@@@@%@%@@@@%*.......@=.....@@@%%%%%%%%%%%%@@@.@@.:.@@#
##@@......--.@@@@@@@@+..-@........*:....@@@@@@@@@%%%@@@@..@=*...@@#
#@@................................#=....:..@@@@@@@@@@@.@.....-..@#
#%@@.@@.::-+...................=--...=:-....................@#-..@*
#%@@.@@@@....*..........#@...................................::..@#
#%@..@.@@@...............:@@......@##-:+:...=%.......@@@@@@@:-...@#
#@@=@@@....@@@@@@@@@@@@@......@@#@*..:...*#.+.....@@.*@@:.-.....@@#
#@.@...%@@@@@@@@..@@#@@@@*.....................@@@@@.@@@-@......@@#
*@@.@%#@@*@..@@..@@....@@@@@..:.+.*=...@:@#=@@@@..@@.@@@.@.@@...@%#
*@.@.@@@...@.@@.@@..@..@..@@@........@@@@@@@.......@@@%@.@.@@@.@@%#""", """
#@%@@..@@@@+.@@.@@.@@.+.....@@@@..@@@@@@+.@@....+@@..@@@@@@@@@..@@#
*%%@@@@..@@@.@@@@@@@@.@.-@...@@@@@@@#.......@@@..@@@@..@@+#%@=...@#
#%%.@.@@@@@..@@@@%%%@@@.%....................@@..@@%@-.@@@@@@@@@.@#
#%@@@**@@@..@..@%%%%@@.@....@....@.#..@.@..@@.@@%.@@@@.@@%%@.@@..@#
#%@@@+-%@@...@.@@%%%%@@.@@@.@@.@#...@.@..@@.@@@@@@#@%@..@@%@@@@..@#
#%%%@@%%@......@@@@@@@@@@.@@@@@.@.@.@@.@@@@@@@@@@@.@@@@@@@@@@@.@.@#
#%%%@@@@@@.@....@%@.@%@%@.@@@@@@@@@@@@@@%%%@@@.@%@@#@@#:+*%@%@@@@@*
#%%%%%%@@@.@@...@.@.@@@%@..@@.@@@@%@@@@@%@@##@+@%@@-=@@@@@@%%@@@%%#
#%%%%%%%%@@@.@@@@.@.#%@%@.@@@:@@.@%%%*-@%%@@@@@%@@@@@@@@@%%%%%%%%%#
#%%%%%%%%%#@@@..:@@.@@@@@..+.@@.:@@@@@@@%%@%@@@@@@@@%@%%%%%%%%%%%%#
#%%%%%%%%@@@@@@@@%@@@...@@.@.@@*@@%%%%@@@@@%%-=.-..%%%%%%%%%%%%%%%#
#%%%%%%%%%%%%%%%@%@@@@@@@@.@@@@@@@@@@@@%...%%@@@@@@@@%%%%%%%%%%%%%#
#%%%%%%%%%%%%%%%%%%%%%%@@@@@*....%....*@@@@@@%%%%%%%%%%%%%%%%%%%%%#
*###########################@@@@@=@@@@@%##########################*"""
]


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def randomShots():
  shot = [1, 1]
  num_shots = random.randint(1, 2)
  ran_shots = [1, 0]
  for x in range(num_shots):
    x = random.choice(shot)
    ran_shots.append(x)
  return ran_shots


def typewrite(text):
  print(text)
  sleep(0.3)


def randomItems():
  items = ["Handcuffs", "Magnifying glass", "Cola", "Medicine", "Saw"]
  ran_items = random.choice(items)
  return ran_items


def Help():
  typewrite("There is a shotgun between us.")
  typewrite("I will load a number of live and blank rounds into")
  typewrite("the shotgun in a random order.")
  typewrite("we will both take turns firing.")
  typewrite(
      "you can use that USE command to use an item you have in your inventory."
  )
  typewrite("Good luck.")


shots = randomShots()
for text in dealer_text:
  print(text, end="")
  sleep(0.5)
print("\n")

typewrite("Welcome to Buckshot CLI")
typewrite(bcolors.WARNING + f"Here are your shots {shots}" + bcolors.ENDC)

two_items = [randomItems(), randomItems(), "Empty Slot", "Empty Slot"]
dealers_items = [randomItems(), randomItems(), "Empty Slot", "Empty Slot"]

while gameloop is True:
  dealers_turn = True

  typewrite(
      f"Here are your two items: {bcolors.OKGREEN+two_items[0] + ' and ' + two_items[1] + bcolors.ENDC}"
  )
  typewrite(
      f"Dealers two items: {bcolors.OKBLUE+dealers_items[0] + ' and ' + dealers_items[1] + bcolors.ENDC}"
  )
  typewrite(f"Health: {health}")
  typewrite(f"Dealer's Health: {dealer_health}")
  typewrite("YOUR TURN")
  print("\nUSE (item), SHOOT (you Or dealer), or HELP")
  random.shuffle(shots)

  # players turn
  player_input = input("> ").lower()

  if double_dealers_turn == 1 or double_dealers_turn == 2:
    double_dealers_turn += 1
  elif double_dealers_turn == 3:
    double_dealers_turn = 0

  if "help" in player_input:
    Help()
    dealers_turn = False

  elif "use" in player_input:

    if player_input not in two_items:
      typewrite(bcolors.WARNING + "YOU don't have the item." + bcolors.ENDC)
      dealers_turn = False

    # magnifying glass
    elif player_input == "use " + "magnifying glass":
      if "Magnifying glass" in two_items:
        typewrite("YOU used the Magnifying glass.")
        if shots[0] == 1:
          typewrite("The shell loaded is a live.")
        else:
          typewrite("The shell loaded is a blank.")
        two_items.remove("Magnifying glass")
      else:
        typewrite("YOU don't have the item.")
      dealers_turn = False

    elif player_input == "use " + "handcuffs":
      typewrite("YOU used the Handcuffs.")
      typewrite("DEALER skips 2 turns.")
      double_dealers_turn += 1
      two_items.remove("Handcuffs")
      dealers_turn = False

    elif player_input == "use " + "medicine":
      health += 1
      typewrite("You used Medicine. Life +1")
      two_items.remove("Medicine")

    elif player_input == "use " + "saw":
      typewrite("You used Saw. double damage for first hit. +1")
      player_dmg = 2
      double_dmg = True
      two_items.remove("Saw")
      dealers_turn = False

    elif player_input == "use " + "Cola":
      typewrite("You used the Cola. Ejects the bullet loaded.")
      typewrite("Bullet ejected.")
      if shots[0] == 1:
        typewrite("The bullet was a live.")
      elif shots[0] == 0:
        typewrite("The bullet was a blank.")
      two_items.remove("Cola")
      dealers_turn = False

  elif "shoot" in player_input:
    if player_input == "shoot " + "you":
      if shots[0] == 1:
        print(f"{bcolors.FAIL+'BAM!'+bcolors.ENDC} Health -1")
        rounds_fired += 1
        health -= 1
        shots.pop(0)
        #dealers turn
      else:
        print("Click... It was a blank. Health -0")
        health -= 0
        shots.pop(0)

    elif player_input == "shoot " + "dealer":
      if shots[0] == 1:
        print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Health -1")
        rounds_fired += 1
        dealer_health -= 1
        shots.pop(0)
      else:
        print("Click... Dealer Health -0")
        dealer_health -= 0
        shots.pop(0)
    else:
      typewrite(bcolors.WARNING + "Invalid command." + bcolors.ENDC)
      dealers_turn = False

  else:
    typewrite(bcolors.WARNING + "Invalid command." + bcolors.ENDC)
    dealers_turn = False

  # dealers turn
  if dealers_turn is True and double_dealers_turn == 0:
    live_shots = shots.count(1)
    blank_shots = shots.count(0)

    typewrite("DEALER'S TURN")
    if live_shots > blank_shots:
      typewrite("DEALER shoots you")
      if shots[0] == 1:
        print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Health -1")
        rounds_fired += 1
        health -= 1
        shots.pop(0)
      else:
        print("Click... It was a blank. Health -0")
        shots.pop(0)

    elif blank_shots > live_shots:
      typewrite("DEALER shoots himself")
      if shots[0] == 1:
        print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Health -1")
        rounds_fired += 1
        dealer_health -= 1
        shots.pop(0)
      elif shots[0] == 0:
        print("Click... DEALER'S Health -0")
        shots.pop(0)

    else:
      if "Magnifying glass" in dealers_items:
        typewrite("DEALER used Magnifying glass")
        typewrite("DEALER breaks it.")
        typewrite("Dealer: 'Very Intresting...'")
        dealers_items.remove("Magnifying glass")
        if shots[0] == 1:
          if "Saw" in dealers_items:
            typewrite("DEALER sawed of shotgun +2 damage")
            typewrite("DEALER shoots you")
            dealers_items.remove("Saw")
            if shots[0] == 1:
              print("Your Health -2")
              rounds_fired += 1
              health -= 2
              shots.pop(0)
          else:
            if "Cola" in dealers_items:
              typewrite("DEALER drank Cola")
              typewrite("Bullet -1")
              dealers_items.remove("Cola")
              if shots[0] == 1:
                print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Your Health -1")
                rounds_fired += 1
                health -= 1
                shots.pop(0)
              else:
                print("Click... It was a blank. Health -0")
                health -= 0
                shots.pop(0)
            else:
              typewrite("DEALER shoots you")
              print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Your Health -1")
              rounds_fired += 1
              health -= 1
              shots.pop(0)
        else:
          typewrite("DEALER shoots himself")
          print("Click... It was a blank. DEALER'S Health -0")
          dealer_health -= 0
          shots.pop(0)

      elif "Medicine" in dealers_items:
        typewrite("DEALER used Medicine")
        typewrite("DEALER health +1")
        dealers_items.remove("Medicine")
        dealer_health += 1
        typewrite("DEALER shoots You")
        if shots[0] == 1:
          print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Your Health -1")
          rounds_fired += 1
          health -= 1
          shots.pop(0)
        else:
          print("Click... It was a blank. Health -0")
          shots.pop(0)
      else:
        do = ["player", "self"]
        shoot = random.choice(do)
        if shoot == "self":
          typewrite("DEALER shoots himself")
          if shots[0] == 1:
            print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} DEALERS Health -1")
            rounds_fired += 1
            dealer_health -= 1
            shots.pop(0)
          else:
            print("Click... It was a blank. Health -0")
            shots.pop(0)
        else:
          typewrite("DEALER shoots you")
          if shots[0] == 1:
            print(f"\n{bcolors.FAIL+'BAM!'+bcolors.ENDC} Your Health -1")
            rounds_fired += 1
            health -= 1
            shots.pop(0)
          else:
            print("Click... It was a blank. Health -0")
            shots.pop(0)
  else:
    typewrite("Dealer skips turn.")

  if health == 0:
    gameloop = False
    print("You loose.")

  elif shots.count(1) == 0:
    gameloop = False
    typewrite("No more live rounds.")
    if dealer_health > health:
      typewrite("Dealer has more health")
      typewrite("Dealer won.")
    elif dealer_health < health:
      typewrite("Player has more health")
      typewrite("You won.")
    elif dealer_health == health:
      typewrite("Both of you have same health.")
      typewrite("Its a draw.")

  print()
typewrite(f"Dealer's health: {dealer_health}")
typewrite(f"Your health: {health}")
typewrite(f"Rounds fired: {rounds_fired}")
