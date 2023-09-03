import time
from plyer import notification


def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Daily Activity Reminder",
        timeout=10  # Notification will stay on screen for 10 seconds
    )


def get_user_activities():
    activities = []
    while True:
        activity = input("Enter an activity (or 'done' to finish): ")
        if activity.lower() == 'done':
            break
        time_str = input(f"Enter the time for '{activity} (HH:MM AM/PM)': ")
        activities.append({"time": time_str, "activity": activity})
    return activities


if __name__ == "__main__":
    daily_activities = get_user_activities()

    while True:
        current_time = time.strftime("%I:%M %p")
        for activity in daily_activities:
            if current_time == activity["time"]:
                title = "Daily Reminder"
                message = f"Don't forget to {activity['activity']}!"
                desktop_notifier(title, message)
                time.sleep(60)
        time.sleep(60)
