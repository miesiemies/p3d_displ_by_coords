# p3d_displ_by_coords
Extract displacements by coordinates for PLAXIS 3D's Python interface

# Description
A small Python script was written to obtain deformation results using the Remote scripting features in the PLAXIS 3D AE Output program. The results are retrieved using Output’s getsingleresult command for a set of coordinates written in a text file. The retrieved results are stored in a separate text file.

This Python script was written for PLAXIS 3D AE in combination with Python 3.4.x

# Instructions

1. Make sure PLAXIS 3D Output is running with a VIP licence;
1. Write a text file with points' coordinates to retrieve the data for;
1. Launch the Remote server on PLAXIS 3D Output on port 10001 (look for outputport variable);
1. Run the Python script to retrieve the deformations;
1. Point to the correct text file for the points' coordinates;
1. The results are then stored in a text file with this content per line: phasename  pointname  ux  uy  uz  
1. This text file is ready to copy & paste to Microsoft Excel or any other spreadsheet program

# Original Developer
Filippo Forlani, 
