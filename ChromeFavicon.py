from PIL import Image

# Set the path to the input image file
input_file = "icons/ori.png"

# Define the favicon sizes and corresponding file names
favicon_sizes = {
    16: "icons/icon16.png",
    19: "icons/icon19.png",
    48: "icons/icon48.png",
    128: "icons/icon128.png"
}

# Open the input image file
image = Image.open(input_file)

# Generate and save the favicon icons for each size
for size, output_file in favicon_sizes.items():
    favicon = image.resize((size, size), resample=Image.BILINEAR)
    favicon.save(output_file, format="PNG")

print("Favicon icons generated successfully!")
