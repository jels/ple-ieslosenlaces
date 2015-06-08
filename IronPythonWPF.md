# Qué es WPF #
  * http://en.wikipedia.org/wiki/Windows_Presentation_Foundation
  * http://msdn.microsoft.com/es-es/library/ms754130.aspx
  * www.cs.brynmawr.edu/cs246/ironpython-wpf.pdf
Windows Forms, construida sobre User32 era la librería usada hasta ahora para construir interfaces.
WPF es una nueva librería de .NET para interfaces . Está construida sobre DirectX. Es más moderna y flexible. Permite más efectos (transparencias, gráficos vectoriales, 3D, animación ...) Las interfaces se pueden crear también con un dialectode XML llamado eXtensible Application Markup Language: XAML. Los diseñadores pueden crear los interfaces con herramientas como Expression Blend (o Lunar Eclipse en Mono).

## Ensamblados de WPF ##
```
PresentationFramework.dll
PresentationCore.dll
WindowsBase.dll
milcore.dll
WindowsCodecs.dll
```
## Namespaces de WPF ##
```
System.Windows
System.Windows.Controls
System.Windows.Documents
System.Windows.Media
System.Windows.Shapes
System.Windows.Markup
```
## Controles ##
http://msdn.microsoft.com/es-es/library/system.windows.controls.aspx
## Ejemplos ##
  * Cómo enlazar a un origen de datos ADO.NET: http://msdn.microsoft.com/es-es/library/ms752057.aspx
# WPF con IronPython #