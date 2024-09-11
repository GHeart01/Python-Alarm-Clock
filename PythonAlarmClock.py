#PythonAlarmClock
import time
import datetime #string representation of time
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarmSound.mp3"
    is_running = True
    

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 🥳")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False      

        time.sleep(1)


if __name__ == "__main__": #if we run this file the directly run the clcok
    alarm_time = input("Enter the alarm time (HH:MM:SS): ") #24 hour clock
    set_alarm(alarm_time)
