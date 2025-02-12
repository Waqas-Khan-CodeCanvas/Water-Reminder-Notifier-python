import time
from plyer import notification



def send_notification():
    notification.notify(
        title="💧 Stay Hydrated!",
        message="Your body needs water. Drink a glass now! 🥤",
        timeout=10
    )

if __name__ == "__main__":
    interval = 60 * 30

    while True:
        send_notification()
        print("Reminder sent! Next reminder in 30 minutes...")
        time.sleep(interval)  


