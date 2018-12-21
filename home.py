import eel
from time import sleep

def main():
    # load web file
    eel.init("web")
    eel.start("main.html")


@eel.expose
def js_func(a):
    print(a)
    print("Called javascript")
    sleep(2)
    # expose and fire js function with argument "maribo"
    eel.my_javascript_function('maririnrin')
    
