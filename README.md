
# 3 Phases Energy Sensor
## _Demo Data Visualization_



### Features

1) Choose to visualize each parameter at each fase (L1, L2, L3). 
2) Visualize multiple fases simultaneously.
3) Switch between fases and parameters instantly, by easily checking the boxes.
4) Eliminate extreme outliners for easier visualization (on the bottom right checkbox).
5) Bottom left table with actualized min, max, average and median information about the data currently showed.

### Instalation and how to run

Required libraries
- PyQt5
- Pandas
- Matplitlib

Run main.py file

### Code explanation

- main.py runs the app
- mainwindow.py
    -Backend: Contains the main window labels and check boxes functions
    -Interacts with the database
- graphs.py
    -Deals with the plot of the graph and how it shows.
-funcionts.py
    -Module with some assistant functions
-mainwindow.py
    -Frontend design

Observations:

I think I could have coded mainwindow.py in a more elegant way, in the end I prioritized functionality and just went for it. If I would code it again I would definitely do it differently.

Somehow when I open a graph and then close it, the instance does not close completely in matplotlib. After some time using the app, it shows a warning: "more than 20 figures have been opened". Still works fine, but definitely something that would need a fix to optimice the app.

### Future additions

- Select and filter days
- Select and filter times

Since the database is only of one hour, I decided to leave this out since it would be overkill. But it is something that could be added for larger databases.

### Conclusion

I had fun programming this app, I am greatful for the task. The functionality is as I wanted it to be. The code can be written smoother and better. Practice makes perfect.

Thank you for your time!
