import subprocess

phone_number = "+911234567890"
subprocess.run([
    "am", "start",
    "-a", "android.intent.action.DIAL",
    "-d", f"tel:{phone_number}"
])
