# About "PcbSetupUser"  



## A. Overview  

+ "PcbSetupUser.py" is a macro program that runs on the PC design software Pcbnew of KiCADv4, and adds the user setting of the specified reference file to the board file on which the macro is running.


## B. File contents 

+ "PcbSetupUser.py" ... Software to copy the user settings of the board file for KiCAD


## C. Confirmation environment 

+ KiCAD Ver 4.07 on Windows7-64bit / Ubuntu14.04LTS-64bit


## D. Usage 

1. Copy the user-defined reference board file to the same folder as the board file you want to add ,and change its file name to "Default.kicad_pcb".
2. Immediately after creating a new board file, there is no setting information, so please load the netlist beforehand, and save it.
3. Start Pcbnew, in case, select and execute Python console.
4. In the console, execute "pwd" and copy this software "PcbSetupUser.py" to the folder that is outputed (normally "C: \ Program Files \ KiCad").
5. In the console, enter "execfile (" PcbSetupUser.py ")" and execute it.
