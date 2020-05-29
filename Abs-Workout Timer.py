"""
DONE BY: LEW YONG JIUN
PROGRAM DESCRIPTION: This is a Abs Workout Timer
"""

########################################################################
# Imports
import time
import winsound

########################################################################
# Constants
########################################################################
work_it = True
REST = 15
WORKOUT_ROUNDS = 1
WORKOUT_ROUTINE = {"High Knee Taps": 45, "Russian Twist": 45, "Leg Raise": 45, "Hip Raise": 45, "Flutter Kicks": 45
    , "Plank Knees to Elbow": 45, "Chair Sit Up - Right Hand": 45, "Chair Sit Up - Left Hand": 45
    , "Seated In & Out": 45, "Jumping Jacks": 45}


########################################################################
# Function
########################################################################
def countdown():
    if WORKOUT_ROUNDS < 5:
        print("=====================================================")
        print("ROUND {} START!!".format(WORKOUT_ROUNDS))
        print("=====================================================")
        if WORKOUT_ROUNDS > 1:
            to_continue = input("Press ENTER to ROUND {}".format(WORKOUT_ROUNDS))
        workout_configuration()
    else:
        print("Congrats, you have finished the daily Abs Workout!!")
        exit()


def workout_configuration():
    global WORKOUT_ROUNDS

    for workout, duration in WORKOUT_ROUTINE.items():
        print("")
        print("START: {}".format(workout))
        timer_algorithm(duration)
        print("You have finish {}".format(workout))
        print("")
        print("START: REST")
        timer_algorithm(REST)
        print("REST OVER!")

    print("")
    print("You have finish ROUND {}".format(WORKOUT_ROUNDS))
    WORKOUT_ROUNDS += 1


def timer_algorithm(duration):
    while duration:
        minutes, seconds = divmod(duration, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1
    winsound.Beep(700, 1200)


########################################################################
# Main
########################################################################
def main():
    hit_it = input("Welcome to Abs Workout Timer. There is a total of 4 Rounds! \nPress ENTER to start")
    while work_it:
        countdown()


########################################################################

if "__main__" == __name__:
    main()
