Descend into madness

Overall things to think about:
    - implementation of mesh (probably triangles)
    - how to make detailed picture into terminal format 
Engine to do:
    1. Transformation (absolute -> relative ex camera)
    2. Depth scalling
    3. Projection
    4. Picture scalling and fixing 

    5. Read up about gimbal lock
    6. Make matlab model of rotatiton transformation to check understanding


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