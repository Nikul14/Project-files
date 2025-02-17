import matplotlib.pyplot as plt
 
import matplotlib.pyplot as plt

# Data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]  # First line
y2 = [3, 6, 9, 12, 15]  # Second line
y3 = [4, 8, 12, 16, 20]  # Third line

# Plot multiple lines with different styles
plt.plot(x, y1, color='r', marker='o', linestyle='-', label="Line 1")
plt.plot(x, y2, color='b', marker='s', linestyle='--', label="Line 2")
plt.plot(x, y3, color='g', marker='^', linestyle='-.', label="Line 3")

# Add labels, title, and legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines in One Plot")
plt.legend()  # Shows the labels in a legend

# # Show plot
# plt.show()

# # Bar graph
x=[2,3,4,6,7]
y=[2,5,6,67,3]
plt.bar(x,y,color='r')
plt.show()

import numpy as np
# x=np.array(['a','b','c','d'])
# y=np.array([1,2,3,4])
# plt.barh(x,y)
# plt.show()
x=np.array(['a','b','c','d'])
y=np.array([1,2,3,4])
plt.barh(x,y,color='r' ,height=0.8)
plt.show()


# Histogram (plt.hist())
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 1000 random values (normal distribution)

plt.hist(data, bins=30, color='blue', edgecolor='black')  # Histogram with 30 bins
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image

# # Provide the correct image path (Ensure the image exists at this location)
# Fname = r"c:\Users\KGE\Downloads\c6cb9eb5-9694-4265-8652-132dcebcf707.jpg" # Use 'r' to handle backslashes correctly

# # Open the image and convert to grayscale
# img = Image.open(Fname) 
# img_array = np.array(img)

# # Display the image
# plt.imshow(img_array)  # Correct grayscale colormap
# plt.axis('off')  # Hide axes for better visualization
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname= r"c:\Users\KGE\Downloads\c6cb9eb5-9694-4265-8652-132dcebcf707.jpg"
img= Image.open(fname)
img_array=np.array(img)
plt.imshow(img_array)
plt.axis('off')
plt.show()
 



