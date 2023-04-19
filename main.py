def on_button_pressed_ab():
    timeanddate.advance_by(1, timeanddate.TimeUnit.MINUTES)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string(timeanddate.time(timeanddate.TimeFormat.HMMAMPM))
input.on_button_pressed(Button.B, on_button_pressed_b)

timeanddate.set_time(8, 59, 55, timeanddate.MornNight.AM)
pins.set_audio_pin(AnalogPin.P1)
music.set_volume(255)
radio.set_group(218)

def on_every_interval():
    timeanddate.advance_by(1, timeanddate.TimeUnit.SECONDS)
loops.every_interval(1000, on_every_interval)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P2) == 1 and timeanddate.time(timeanddate.TimeFormat.HMMSSAMPM) == "09:05.00":
        radio.send_string("meds weren't taken")
        basic.show_icon(IconNames.NO)
        basic.pause(1000)
        basic.clear_screen()
    elif pins.digital_read_pin(DigitalPin.P2) == 0 and (timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR) >= "09:00.00" and timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR) <= "09:05.00"):
        basic.show_icon(IconNames.YES)
        music.stop_all_sounds()
        basic.pause(1000)
        basic.clear_screen()
    else:
        pass
basic.forever(on_forever)

def on_forever2():
    if timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR) == "09:00.00":
        radio.send_string("take your meds")
        servos.P0.set_angle(80)
        basic.pause(900)
        servos.P0.set_angle(100)
        basic.pause(800)
        servos.P0.stop()
basic.forever(on_forever2)

def on_forever3():
    while pins.digital_read_pin(DigitalPin.P2) == 1 and (timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR) >= "09:00.00" and timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR) <= "09:05.00"):
        music.play_melody("C C5 C C5 C C5 C C5 ", 250)
basic.forever(on_forever3)
