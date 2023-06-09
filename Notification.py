import time
from datetime import datetime, timedelta
from pytz import timezone
from plyer import notification

if __name__ == "__main__":
    # Set the timezone to Indian Standard Time (IST)
    tz = timezone('Asia/Kolkata')

    # Calculate the end time for the notification (two days from the current time)
    current_time = datetime.now(tz)
    end_time = current_time + timedelta(days=2)

    while datetime.now(tz) < end_time:
        # Display the notification
        
        notification.notify(
            title="Certificate Submission!",
            message="Rajveer, click the photos of your certificate for submission and mentoring marks.",
            app_icon=r"C:\Users\Rajveer Singh\Desktop\Work\Python\certificate.ico",
            timeout=5
        )

        # Wait for a certain interval before displaying the next notification
        time.sleep(60*60)  # Sleep for 60 seconds (1 minute) before displaying the next notification
