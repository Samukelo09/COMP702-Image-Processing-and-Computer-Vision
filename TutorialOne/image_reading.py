import cv2
import tkinter as tk
from tkinter import filedialog

# Function to open an image file
def open_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff")]
    )

    if file_path:  # If a file was selected
        image = cv2.imread(file_path)  # Load the image
        if image is None:
            print("Error: Unable to open the image.")
            return

        cv2.imshow("Opened Image", image)  # Display the image
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Create a simple GUI window
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

# Run the image opener
open_image()
