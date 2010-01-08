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

namespace PrimerJuego
{
    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public class Game1 : Microsoft.Xna.Framework.Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        // Zona de atributos
        // variables colores
        byte rojo;
        byte verde;
        byte azul;
        // variable subeColor 
        bool subeColor = true;
        int ciclo = 1; // ciclo de color: rojo, verde, azul
        byte intensidad = 0;

        public Game1()
        {
            // m�todo constructor
            

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
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
                this.Exit();

            // TODO: Add your update logic here
            if (subeColor == true)
            {  // no es necesario poner esta llave si s�lo hay una
               //l�nea
                intensidad++;
            }
            else
                intensidad--;
            if (intensidad == 255)
                subeColor = false;
            if (intensidad == 0)
            {
                subeColor = true;
                ciclo++;
                if (ciclo == 4)
                    ciclo = 1;
            }
            if (ciclo == 1)
            {
                rojo = intensidad;
                verde = 0;
                azul = 0;
            }
            if (ciclo == 2)
            {
                rojo = 0;
                verde = intensidad;
                azul = 0;
            }
            if (ciclo == 3)
            {
                rojo = 0;
                verde = 0;
                azul = intensidad;
            }

            //verde++;
            //azul++;
            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            Color fondo;    // tipo y nombre de la variable
            fondo = new Color(rojo, verde, azul);  // inicializaci�n del color

            GraphicsDevice.Clear(fondo);

            // TODO: Add your drawing code here

            base.Draw(gameTime);
        }
    }
}
