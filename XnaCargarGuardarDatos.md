Ejemplo sacados de http://msdn.microsoft.com/en-us/library/bb199073.aspx y http://www.ikisoftware.com/2009/02/26/xna-game-studio-como-guardar-y-cargar-saves-en-el-xbox360/

# Abrir archivos #

```
private static void DoOpen(StorageDevice device)
{
    // Open a storage container.
    StorageContainer container =
        device.OpenContainer("StorageDemo");

    // Add the container path to our file name.
    string filename = Path.Combine(container.Path, "demobinary.sav");

    FileStream file = File.Open(filename, FileMode.Open);
    file.Close();

    // Dispose the container.
    container.Dispose();
}
```

# Preparar clase para guardar #
```
[Serializable]
public struct SaveGameData
{
    public string PlayerName;
    public Vector2 AvatarPosition;
    public int Level;
    public int Score;
}

```

# Guardar datos #
```
private static void DoSaveGame(StorageDevice device)
{
    // Create the data to save.
    SaveGameData data = new SaveGameData();
    data.PlayerName = "Hiro";
    data.AvatarPosition = new Vector2(360, 360);
    data.Level = 11;
    data.Score = 4200;

    // Open a storage container.
    StorageContainer container =
        device.OpenContainer("StorageDemo");

    // Get the path of the save game.
    string filename = Path.Combine(container.Path, "savegame.sav");

    // Open the file, creating it if necessary.
    FileStream stream = File.Open(filename, FileMode.Create);
    

    // Convert the object to XML data and put it in the stream.
    XmlSerializer serializer = new XmlSerializer(typeof(SaveGameData));
    serializer.Serialize(stream, data);

    // Close the file.
    stream.Close();

    // Dispose the container, to commit changes.
    container.Dispose();
}

```

# Cargar datos #
```
private static void DoLoadGame(StorageDevice device)
{
// Cambiar MiJuego por el nombre de tu juego.
StorageContainer container =
device.OpenContainer(”MiJuego”);

// Get the path of the save game.
string filename = Path.Combine(container.Path, “SaveMiJuego.sav”);

// Check to see whether the save exists.
if (!File.Exists(filename))
{
return;
}

// Open the file.
FileStream stream = File.Open(filename, FileMode.OpenOrCreate,
FileAccess.Read);

// Read the data from the file.
XmlSerializer serializer = new XmlSerializer(typeof(Jugador));
Control.jugador = (Jugador)serializer.Deserialize(stream);

// Close the file.
stream.Close();

// Dispose the container.
container.Dispose();
}
```