import subprocess
from pathlib import Path

folder = Path.home() / "Desktop" / "Transcription"
slack = folder / "Slack"
urls = [
    "https://mail.google.com/mail/u/2/#all",
    "https://alphascribes.alphasights.com/interactions", 
    "https://www.google.com/",
    "https://alphasights.docsend.com/view/s/e23qqdnqhupdjxqq",
    "https://stable.getautoclicker.com/"
]
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([r"C:\Program Files\Mullvad VPN\MUllvad VPN.exe"])
subprocess.run(["mullvad", "connect"])
subprocess.run(["explorer", str(folder)])
subprocess.run(["start", str(slack)], shell=True)
subprocess.run([chrome] + urls)