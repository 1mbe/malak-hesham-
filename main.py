basic.show_string("malak")
def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)
item = 0
def on_button_pressed_b():
    global item
    item +=1  
    basic.show_number(item)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_gesture_shake():
    for h in range(5):
        basic.show_number(h)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
N =70
def on_button_pressed_ab():
    if N  >= 69:
     basic.show_string("PASS")
    else:
        basic.show_string("FAIL")
input.on_button_pressed(Button.AB, on_button_pressed_ab)
