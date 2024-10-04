import argparse
from PIL import Image

def change_sprite_spacing(sprite_sheet_path, output_path, orig_w, orig_h, cols, new_w, new_h, rows):
    # Load the original sprite sheet
    sprite_sheet = Image.open(sprite_sheet_path)

    # Calculate the size of the new image with the updated spacing
    new_grid_width = new_w * cols
    new_grid_height = new_h * rows

    # Create a new blank image with the desired size
    new_image = Image.new("RGBA", (new_grid_width, new_grid_height), (0, 0, 0, 0))  # Transparent background

    # Loop through the original grid and paste each sprite into the new image
    for row in range(rows):
        for col in range(cols):
            # Calculate the sprite's position in the original sheet
            original_x = col * orig_w
            original_y = row * orig_h

            # Extract the sprite from the original sheet
            sprite = sprite_sheet.crop((original_x, original_y, original_x + orig_w, original_y + orig_h))

            # Calculate the new position in the new image (adjusting for spacing but keeping sprite size the same)
            new_x = col * new_w
            new_y = row * new_h

            # Paste the sprite into the new image at the same size (no resizing)
            new_image.paste(sprite, (new_x, new_y))

    # Save the new image
    new_image.save(output_path)

if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Change sprite sheet spacing without resizing sprites.")
    
    # Add required positional arguments for input and output file paths
    parser.add_argument("input", help="Path to the original sprite sheet")
    parser.add_argument("output", help="Path to save the new sprite sheet")
    
    # Add optional arguments for sprite dimensions and grid configuration with sensible defaults
    parser.add_argument("--ow", type=int, default=160, help="Original sprite width (default: 160)")
    parser.add_argument("--oh", type=int, default=228, help="Original sprite height (default: 228)")
    parser.add_argument("--cols", type=int, default=4, help="Sprites per row (default: 4)")
    parser.add_argument("--nw", type=int, default=240, help="New sprite rectangle width (default: 240)")
    parser.add_argument("--nh", type=int, default=480, help="New sprite rectangle height (default: 480)")
    parser.add_argument("--rows", type=int, default=4, help="Number of rows (default: 4)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the resize function with the provided arguments
    change_sprite_spacing(
        args.input,
        args.output,
        args.ow,
        args.oh,
        args.cols,
        args.nw,
        args.nh,
        args.rows
    )
