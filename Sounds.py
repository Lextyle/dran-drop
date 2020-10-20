from pygame import mixer
mixer.pre_init(44100, -16, 2, 4096)
mixer.init()
drag_sound = mixer.Sound(r"sounds\drag_sound.wav")
drop_sound = mixer.Sound(r"sounds\drop_sound.wav")
explosion_sound = mixer.Sound(r"sounds\explosion_sound.wav")
button_pressed_sound = mixer.Sound(r"sounds\button_pressed.wav")