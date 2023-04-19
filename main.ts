input.onButtonPressed(Button.B, function () {
    basic.showString(timeanddate.time(timeanddate.TimeFormat.HMMAMPM))
})
timeanddate.setTime(8, 59, 55, timeanddate.MornNight.AM)
pins.setAudioPin(AnalogPin.P1)
music.setVolume(255)
radio.setGroup(218)
loops.everyInterval(1000, function () {
    timeanddate.advanceBy(1, timeanddate.TimeUnit.Seconds)
})
basic.forever(function () {
    while (pins.digitalReadPin(DigitalPin.P2) == 1 && (timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr) >= "09:00.00" && timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr) <= "09:05.00")) {
        music.playMelody("C C5 C C5 C C5 C C5 ", 250)
    }
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P2) == 0 && (timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr) >= "09:00.00" && timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr) <= "09:05.00")) {
        basic.showIcon(IconNames.Yes)
        music.stopAllSounds()
    }
    if (pins.digitalReadPin(DigitalPin.P2) == 1 && timeanddate.time(timeanddate.TimeFormat.HMMSSAMPM) == "09:05.00") {
        radio.sendString("meds weren't taken")
        basic.showIcon(IconNames.No)
    }
    if (timeanddate.time(timeanddate.TimeFormat.HMMSSAMPM) == "09:05.30") {
        basic.clearScreen()
    }
})
basic.forever(function () {
    if (timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr) == "09:00.00") {
        radio.sendString("take your meds")
    }
})
