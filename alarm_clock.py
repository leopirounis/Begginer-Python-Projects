import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "digital alarm.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake up!⏰")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)  #load music
            pygame.mixer.music.play() #play music
            is_running = False
            while pygame.mixer.music.get_busy():
                time.sleep(1) # paizei tin mousiki oso den kleinoume to programma

        time.sleep(1) #deixnei tin ora pou pernaei kathe 1 defterolepto

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)