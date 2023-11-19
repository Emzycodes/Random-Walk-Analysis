import matplotlib.pyplot as plt
from randomwalks import RandomWalks  # Fix the typo in the import

def run_visual():
    repeat = True
    
    while repeat:
        # Make a random walk
        rw = RandomWalks()
        rw.fill_walk()

        # Plot the points in the walk.
        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.scatter(rw.x_values, rw.y_values, s=15)
        plt.savefig("img.png", bbox_inches='tight')
        plt.show()

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
