import eel
from time import sleep

def main():
    # load web file
    eel.init("web")
    
    eel.start("main.html")



"""script when link1 pushed"""
# "@eel.expose" enables functions to be recognized by js
@eel.expose
# don't forget to set the same name with js function which you want to fire here
def link1_click():
    null = 1
    print("link1_clicked%s" % null)
    print("sleep")
#     fire js_func with argument 'mari'
    js_func('mari')
    

@eel.expose
def js_func(a):
     print(a)
     print("Called javascript")
     sleep(2)
     # expose and fire js function with argument "maribo"
     eel.my_javascript_function('maribo')
    

"""script when link2 pushed"""
@eel.expose
def link2_click(args):
    null = 2
    print(args)
    print("%s" % null)
    return "link2_clicked"

@eel.expose
def link3_click():
    null = 3
    print("link3_clicked%s" % null)

if __name__ == '__main__':
     main()