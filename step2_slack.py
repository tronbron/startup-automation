from pathlib import Path
import subprocess

folder = Path.home() / "Desktop" / "Transcription"
slack = folder / "Slack"

subprocess.run(["explorer", str(folder)])
subprocess.run(["start", str(slack)], shell=True)