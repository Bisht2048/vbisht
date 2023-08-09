import win32com.client as wincom
import time
speak=wincom.Dispatch("SAPI.spvoice")
text = "Hello Vaibhav"
# time.sleep(3)
speak.Speak(text)