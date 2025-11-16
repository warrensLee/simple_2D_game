using Raylib_cs;
using GameProject.Model;
using GameProject.Controller;
using GameProject.View;

class Program
{
    static void Main(string[] args)
    {
        // make game window and target FPS
        Raylib.InitWindow(1280,720, "--Game Name Here--");
        Raylib.SetTargetFPS(60);

        var state = new GameState();
        var controller = new GameController(state);
        var renderer = new Renderer(state);

        // now add player to game
        // commented till implemented: state.Entities.Add(new Player{ X = 100, Y = 100});

        while (!Raylib.WindowShouldClose())
        {
            float deltaTime = Raylib.GetFrameTime();

            controller.HandleInput();

            foreach (var e in state.Entities)
            {
                e.Update(deltaTime, state);
            }

            renderer.Draw();
        }

        Raylib.CloseWindow();
    }
}