using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using Microsoft.Xna.Framework.Net;
using Microsoft.Xna.Framework.Storage;

namespace EntradaUsuario
{
    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public class Game1 : Microsoft.Xna.Framework.Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;

        // atributos globales
        byte rojo = 0;
        byte verde = 0;
        byte azul = 0;

        // estado de gamepad
        GamePadState pad1;
        KeyboardState teclas;

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {
            // TODO: Add your initialization logic here

            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);

            // TODO: use this.Content to load your game content here
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
            // TODO: Unload any non ContentManager content here
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            // Allows the game to exit
            GamePad.SetVibration(PlayerIndex.One, 0, 0);
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed ||
                teclas.IsKeyDown(Keys.Escape))
                this.Exit();

            // TODO: Add your update logic here
            // leer estado de controlador 
            pad1 = GamePad.GetState(PlayerIndex.One);
            teclas = Keyboard.GetState();
            // comprobación de estado
            if (pad1.Buttons.B == ButtonState.Pressed ||
                pad1.DPad.Right == ButtonState.Pressed ||
                teclas.IsKeyDown(Keys.R))
                rojo++;
            if (pad1.Buttons.A == ButtonState.Pressed ||
                pad1.DPad.Down == ButtonState.Pressed ||
                teclas.IsKeyDown(Keys.V))
                verde++;
            if (pad1.Buttons.X == ButtonState.Pressed ||
                pad1.DPad.Left == ButtonState.Pressed ||
                teclas.IsKeyDown(Keys.A))
            {
                azul++;
           
            }
            if (pad1.Buttons.Y == ButtonState.Pressed ||
                pad1.DPad.Up == ButtonState.Pressed ||
                teclas.IsKeyDown(Keys.N))  //naranja ?
            {
                rojo++;
                verde++;
            }
            if ((pad1.Buttons.LeftShoulder == ButtonState.Pressed &&
                pad1.Buttons.RightShoulder == ButtonState.Pressed) ||
                (teclas.IsKeyDown(Keys.LeftShift) &&
                teclas.IsKeyDown(Keys.RightShift) )
                )
            {
                rojo = 0;
                verde = 0;
                azul = 0;
            }
            if (rojo > 220 || verde > 220 || azul > 220)
                GamePad.SetVibration(PlayerIndex.One, 0, 1);
            else
                GamePad.SetVibration(PlayerIndex.One, 0, 0);

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            // atributo color
            Color color = new Color(rojo, verde, azul);

            GraphicsDevice.Clear(color);

            // TODO: Add your drawing code here

            base.Draw(gameTime);
        }
    }
}
