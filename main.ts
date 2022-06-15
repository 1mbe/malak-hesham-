basic.showString("malak")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
let item = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    item += 1
    basic.showNumber(item)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    for (let h = 0; h < 5; h++) {
        basic.showNumber(h)
    }
})
let N = 70
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (N >= 69) {
        basic.showString("PASS")
    } else {
        basic.showString("FAIL")
    }
    
})
