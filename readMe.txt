Descend into madness

Overall things to think about:
    - implementation of mesh (probably triangles)
    - how to make detailed picture into terminal format 
Engine to do:
I chapter:
    1. Transformation (absolute -> relative ex camera)
    2. Depth scalling
    3. Projection
    4. Picture scalling and fixing 

    5. Read up about gimbal lock
    6. Make matlab model of rotatiton transformation to check understanding

II chapter:
    - implement more methods to cooperate better between classes
    - creater lib(?) file so importing classes is easier
    - incorporate use of shapes 
    - fix image blinking in terminal!!!!
    - more methods to change objects render (frame size etc)
    - cs_transfomr method look into???


Progess day 1:
    - found translation for moving CS by vector 
    - looking for rotation deriviation

Progess day 2:
    - implemented transformation method 

Progress day 3:
    - reading about how to render object 
    Source: https://www.scratchapixel.com/index.php?redirect

Proggess day 4:
    - worked on class structure
    - started rasterization methods

Day 5 + 6:
    - something is off with rotation
    Found out that the rotations I look for are theta and psi (gotta look into that though).
    While testing on triangle points A(300, 0, 0), B(-300, 0, 0), C(0, 300, 0) after transformation by psi(10) got weird z cordinate of point C_z = -52

Day ???:
    - First render of spinning donut!!!


Day ??? + few months:
    To do:
        - Add widget menu to animation
        - Add animation to styles
        - Add comments to all files:
            - GUI 
            - Menu
            - styles
            - main
            - camera
            - Renderer
            - shapes
            - window
        - Reupload nice graphics instead of check off and on