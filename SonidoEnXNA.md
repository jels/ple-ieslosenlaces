# Introducción #


  * http://msdn.microsoft.com/en-us/library/dd282355.aspx
  * http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.audio.soundeffect.aspx
  * http://msdn.microsoft.com/en-us/library/dd940203.aspx  Sonido en repetición

```
public SoundEffectInstance Play (
         float volume,
         float pitch,
         float pan,
         bool loop
)
```

```
SoundEffectInstance instance = soundEffect.CreateInstance();
instance.IsLooped = true;
instance.Play();
```