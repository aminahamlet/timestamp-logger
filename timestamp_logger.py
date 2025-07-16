from datetime import datetime

with open("timestamp_log.txt", "a") as file:
    file.write(f"Timestamp logged at: {datetime.now()}\n")

print("Timestamp logged successfully!")

