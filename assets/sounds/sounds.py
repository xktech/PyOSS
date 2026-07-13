import winsound

def error_sound():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
def success_sound():
    winsound.Beep(800, 100)