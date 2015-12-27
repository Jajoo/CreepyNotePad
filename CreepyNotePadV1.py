import pyautogui

MESSAGE = 'I am watching you'



def OpenUpNotePad():
    pyautogui.moveTo(24, 842, 2)#moves mouse to windows buttonu
    pyautogui.click()#clicks the windows button
    pyautogui.typewrite('notepad',0.5)#types in 'notepad' into search bar
    pyautogui.press('enter')

def TyperandCloser():
    pyautogui.moveTo(730,300)#moves mouse to window button
    pyautogui.click()#clicks
    pyautogui.typewrite(MESSAGE, .05)#types



OpenUpNotePad()
TyperandCloser()
