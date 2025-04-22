import random

number = random.randint(1, 100)
score = 100
tries = 5

def restart(answer):

    if answer == "Y":
        return True
    elif answer == "N":
        return False
    else:
        return False

print("=== DEVINE LE NOMBRE ===")
print("1. Jouer")
print("2. Règles")
print("3. Quitter")

choice = int(input("Choisis une option : "))
if choice == 2:
    print('Appuyer sur jouer')
elif choice == 3:
    exit()
elif choice == 1:

    while True:

        try:
            tentative = int(input("Devine le nombre (entre 1 et 100) : "))
        except ValueError:
            print("Ce n'est pas un nombre valide !")
            continue

        if tentative > number:
            tries -= 1
            score -= 20
            print(f"Trop grand ! Encore {tries} tentative(s).")
        elif tentative < number:
            tries -= 1
            score -= 20
            print(f"Trop petit ! Encore {tries} tentative(s).")
        else:
            print(f"Bravo ! Le nombre était bien {number} 🎉 Score: {score}%")
            playAgain = input("Rejouer ? (Y/N) ").upper()
            if playAgain.upper() == "Y":
                number = random.randint(1, 100)
                tries = 5
            else:
                break

        if tries == 0:
            print(f"Dommage ! Tu as épuisé toutes tes tentatives. Le nombre était {number}. Score: {score}%")
            playAgain = input("Rejouer ? (Y/N) ").upper()
            if bool(restart(playAgain)):
                number = random.randint(1, 100)
                tries = 5
                score = 100
            else:
                print('Bonne journée !')
                break