import matplotlib.pyplot as plt
from randomwalks import RandomWalks  # Fix the typo in the import

def run_visual():
    repeat = True
    
    while repeat:
        # Make a random walk
        rw = RandomWalks()
        rw.fill_walk()

        # Plot the points in the walk.
        #############################
        plt.style.use('classic')
        fig, ax = plt.subplots()
        point_numbers = range(rw.points)
        ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
                   edgecolors='none', s=1)

        # Emphasize the first and the last points.
        ax.scatter(0,0, c= 'green', s=100,edgecolors='none')
        ax.scatter(rw.x_values[-1],rw.y_values[-1],c= 'red', s= 100)

        # Remove the axis
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Save the image and display
        plt.savefig("img.png", bbox_inches='tight') #saves the image as img.png
        plt.show() # display thr plot

        restart = input("Do you want to run the analysis again? (y/n): ").lower()

        if restart == "n":
            print("Exiting visualization.")
            repeat = False
        elif restart == "y":
            print("Restarting visualization...")
        else:
            print("Invalid input. Exiting visualization.")
            repeat = False

# Call the run_visual() function to execute the visualization
if __name__ == "__main__":
    run_visual()
