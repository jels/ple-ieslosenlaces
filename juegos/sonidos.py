# -*- coding: cp1252 -*-
"""
Para reproducir sonidos con winsound
(sólo en windows)
"""

import winsound

# Sonido de salir ..
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# Error
winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

# Sonido en .wav
winsound.PlaySound('doh.wav' ,winsound.SND_FILENAME)

