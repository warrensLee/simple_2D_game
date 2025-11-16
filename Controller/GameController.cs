using Raylib_cs;
using simple_2D_game.Model;
using simple_2D_game.View;

class GameController
{
    public static void UpdateController()
    {
        // enum: https://github.com/raysan5/raylib/blob/master/src/raylib.h#L576

        if (IsKeyDown(KEY_W))                                   // UP               W
        {
            // tell model something
        }
        if (IsKeyDown(KEY_S))                                   // DOWN             S
        {
            // tell model something
        }
        if (IsKeyDown(KEY_A))                                   // LEFT             A
        {
            // tell model something
        }
        if (IsKeyDown(KEY_D))                                   // RIGHT            D
        {
            // tell model something
        }
        if (IsMouseButtonDown(MOUSE_BUTTON_LEFT))               // LEFT CLICK       
        {
            // tell model something
        }
        if (IsMouseButtonDown(MOUSE_BUTTON_RIGHT))              // RIGHT CLICK
        {
            // tell model something
        }
    }
}
