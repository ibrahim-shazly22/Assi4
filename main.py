import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, output_path, watermark_text):
    # Open the image
    img = Image.open(image_path)

    # Add watermark
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 36)  # Change the font and size as needed
    draw.text((10, 10), watermark_text, fill="white", font=font)

    # Save the watermarked image
    img.save(output_path)


def select_image():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def add_watermark_to_image():
    image_path = entry.get()
    if not image_path:
        return

    output_path = "watermarked_image.jpg"  # Output file path
    watermark_text = "Your Watermark Text"  # Watermark text

    add_watermark(image_path, output_path, watermark_text)
    tk.messagebox.showinfo("Success", "Watermark added successfully!")


# Create the main window
root = tk.Tk()
root.title("Image Watermarking App")

# Add widgets
tk.Label(root, text="Select Image:").pack()
entry = tk.Entry(root, width=50)
entry.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Button(root, text="Add Watermark", command=add_watermark_to_image).pack()

# Start the main event loop
root.mainloop()