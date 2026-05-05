import subprocess, time

time.sleep(5)

phone_number = "+911234567890"
subprocess.run([
    "am", "start",
    "-a", "android.intent.action.CALL",
    "-d", f"tel:{phone_number}"
])


import subprocess

phone_number = "+911234567890"
subprocess.run(["termux-telephony-call", phone_number])
