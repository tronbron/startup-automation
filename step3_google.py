import subprocess

urls = [
    "https://mail.google.com/mail/u/2/#all",
    "https://alphascribes.alphasights.com/interactions", 
    "https://www.google.com/",
    "https://alphasights.docsend.com/view/s/e23qqdnqhupdjxqq",
    "https://stable.getautoclicker.com/"
]

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.run([chrome] + urls)