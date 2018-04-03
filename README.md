# Project3 #
## Planetary modeling using differential equations ##
This repository holds all parts to the third project for PHY 480 at MSU spring-2018

The repository is split into three folders. Pictures holds all pictures in the report as well as some extra pictures that were created.

The report is in the Report folder as well as the zip of the latex file.

All programs are in the Programs folder. They are all coded in python3 requiring numpy and matplolib. There are the following programs:
1. Findingescapevelocity.py
    - Finds the escape velocity of earth.
2. Run_RealPlanets_VV.py
    - Runs the solar system will all planets in it. Uses the VV method. Also displays the paths and shows the conserved quantities after.
3. Run_SunEarthJupiter_Euler.py
    - Uses Euler's method to simulate the Sun-Earth-Jupiter system. Also displays the paths and shows the conserved quantities after.
4. Run_SunEarthJupiter_VV.py
    - Uses the Velocity Verlet (VV) method to simulate the Sun-Earth-Jupiter system. Also displays the paths and shows the conserved quantities after.
5. Showing Stability.py
    - Takes the conserved quantities from the Euler and VV and compares them over either short or long term
6. SunEarthJupiter_timing_euler.py
    - Times the Euler and VV methods
7. SunEarthJupiter_timing_hardcode.py
    - Times the difference between hard coding and OOP
