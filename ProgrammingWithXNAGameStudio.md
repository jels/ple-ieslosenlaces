# Conexión XBox #
http://creators.xna.com/en-US/education/gettingstarted/bgintro/Chapter5

[XNAGamepad](XNAGamepad.md)

# C# for pythoners #
Todas las sentencias terminadas con `;`

Bloques: `  {} `

Comentarios: ` // `

# Condicionales #
```
if (condición)
{
    bloque
{
```

# Estructura general de un videojuego #

```
Inicializar controladores gráficos, de entrada y de sonido
Cargar recursos
Iniciar bucle del juego. En cada paso:
    Recoger input de usuario
    Hacer cálculos necesarios (IA, movimientos, colisiones, etc)
    Dibujar el nuevo estado de la pantalla, generar sonidos y feedback del controlador
Finalizar gráficos, input y sonido
Liberar recursos
```

# Proyecto con XNA #
XNA oculta parte de la dificultad de crear el videojuego
## Métodos creados en Game1.cs y Program.cs ##
```
Game1() --> inicialización general
Initialize() --> Inicialización del juego
LoadContent() --> Carga recursos gráficos
Run() --> Inicia el bucle del juego
  En cada paso:
    Update()  
    Draw()
UnloadContent()
```