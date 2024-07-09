#!/usr/bin/env python3

from pathlib import PosixPath
from PIL import Image
from scipy.spatial import KDTree
from itertools import combinations
import numpy as np
import argparse

# Gruvbox Dark color palette
PALETTE = [
    "#282828", # bg
    "#CC241D", # red
    "#98971A", # green
    "#D79921", # yellow
    "#458588", # blue
    "#B16286", # purple
    "#689D6A", # aqua
    "#A89984", # gray

    "#928374", # gray
    "#FB4934", # red
    "#B8BB26", # green
    "#FABD2F", # yellow
    "#83A598", # blue
    "#D3869B", # purple
    "#8EC07C", # aqua
    "#EBDBB2", # fg

    "#1D2021", # bg0_h
    "#282828", # bg0
    "#3C3836", # bg1
    "#504945", # bg2
    "#665C54", # bg3
    "#7C6F64", # bg4
    "#928374", # gray
    "#D65D0E", # orange

    "#32302F", # bg0_s
    "#A89984", # fg4
    "#BDAE93", # fg3
    "#D5C4A1", # fg2
    "#EBDBB2", # fg1
    "#FBF1C7", # fg0
    "#FE8019", # orange
]


def color_hex2dec(hexstr: str) -> tuple:
    """
    Convert a hexadecimal color string to a tuple of decimal RGB values.

    Args:
        hexstr (str): Hexadecimal color string (e.g., "#FF5733").

    Returns:
        tuple: Decimal RGB values as a tuple (r, g, b).
    """

    r = int(hexstr[1:3], 16)
    g = int(hexstr[3:5], 16)
    b = int(hexstr[5:], 16)

    return (r, g, b)


def color_dec2hex(hexval: tuple, prefix: bool = True) -> str:
    """
    Convert a tuple of decimal RGB values to a hexadecimal color string.

    Args:
        hexval (tuple): Decimal RGB values as a tuple (r, g, b).
        prefix (bool, optional): Whether to include the "#" prefix. Defaults to True.

    Returns:
        str: Hexadecimal color string (e.g., "#FF5733").
    """
    
    color = "#" if prefix else ""
    for value in hexval:
        x = hex(value)
        x = x[2:]
        x = x.upper()
        x = x.rjust(2, '0')

        color += x

    return color


def luminance(color: tuple) -> float:
    """
    Calculate the luminance of a color.

    Args:
        color (tuple): Decimal RGB values as a tuple (r, g, b).

    Returns:
        float: Luminance value.
    """

    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def interpolate_palette(color1: tuple, color2: tuple, num_colors: int = 20) -> tuple:
    """
    Interpolate between two colors to create a palette.

    Args:
        color1 (tuple): Decimal RGB values of the first color.
        color2 (tuple): Decimal RGB values of the second color.
        num_colors (int, optional): Number of colors to generate. Defaults to 20.

    Returns:
        tuple: Interpolated palette as a tuple of tuples.
    """

    # Change to Numpy RGB format (0 to 1 range)
    color1 = np.array(color1) / 255.0
    color2 = np.array(color2) / 255.0

    # Create a palette with interpolated colors
    palette = np.linspace(color1, color2, num_colors)

    # Convert back to 0-255 range and tuple of tuples
    palette = tuple(tuple(int(c * 255) for c in color) for color in palette)

    return palette


def extend_palette(palette: list, darkest_color: str = None, brightest_color: str = None, use_brightest: bool = False, interpolate: bool = False) -> set:
    """
    Extend a color palette by interpolating between colors and/or using the brightest colors.

    Args:
        palette (list): List of hexadecimal color strings.
        darkest_color (str, optional): Hexadecimal color string of the darkest color. Defaults to None.
        brightest_color (str, optional): Hexadecimal color string of the brightest color. Defaults to None.
        use_brightest (bool, optional): Whether to use the brightest colors while extending. Defaults to False.
        interpolate (bool, optional): Whether to interpolate between colors. Defaults to False.

    Returns:
        set: Extended palette as a set of tuples of decimal RGB values.
    """

    print("Extending colors...")

    palette = map(color_hex2dec, palette)
    palette = list(palette)
    new_palette = set(palette)

    if interpolate:
        for color1, color2 in combinations(palette, 2):
            interpolated_palette = interpolate_palette(color1, color2)
            new_palette.update(interpolated_palette)

    if brightest_color is None:
        brightest_color = max(palette, key=luminance)
    else:
        brightest_color = color_hex2dec(brightest_color)

    if darkest_color is None:
        darkest_color = min(palette, key=luminance)
    else:
        darkest_color = color_hex2dec(darkest_color)

    for color in palette:
        r, g, b = color
        dr, dg, db = darkest_color

        max_color_value = max(color)
        darkest_color_value = min(darkest_color)
        color_diff = max_color_value - darkest_color_value

        for _ in range(color_diff):
            r = r - 1 if r > dr else dr
            g = g - 1 if g > dg else dg
            b = b - 1 if b > db else db

            new_color = (r, g, b)
            new_palette.add(new_color)
        
        if use_brightest and brightest_color:
            r, g, b = color
            lr, lg, lb = brightest_color

            min_color_value = min(color)
            brightest_color_value = max(brightest_color)
            color_diff = max_color_value - min_color_value

            for _ in range(color_diff):
                r = r + 1 if r < lr else lr
                g = g + 1 if g < lg else lg
                b = b + 1 if b < lb else lb

                new_color = (r, g, b)
                new_palette.add(new_color)

    
    print(f"Extended to {len(new_palette)} colors")
    return new_palette


def read_gpl(file_path: PosixPath) -> list:
    """
    Read a GIMP Palette (.gpl) file and extract the colors.

    Args:
        file_path (PosixPath): Path to the .gpl file.

    Returns:
        list: List of tuples containing decimal RGB values.
    """

    colors = []

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()

                if not line or line.startswith('GIMP Palette'):
                    continue
                # Split the line into components: R G B Name
                components = line.split()

                if len(components) < 3:
                    continue

                try:
                    # Extract RGB values
                    r = int(components[0])
                    g = int(components[1])
                    b = int(components[2])
                    # Validate RGB values
                    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                        colors.append((r, g, b))

                except ValueError:
                    continue

    except FileNotFoundError:
        print(f"Could not read the GIMP Palette file: '{file_path}'")
        return
    
    except Exception as e:
        print(f"An unknown error happened while reading a .gpl file: {e}")
        return

    return colors


def save_as_gpl(palette: list, out_path: str):
    """
    Save a color palette as a GIMP Palette (.gpl) file.

    Args:
        palette (list): List of tuples containing decimal RGB values.
        out_path (str): Path to the output .gpl file.
    """

    gpl = "GIMP Palette\nName: Gruvbox Extended\nColumns: 1\n#"

    for color in palette:
        r, g, b = color
        color = color_dec2hex(color, False)

        gpl += f"\n{r} {g} {b} color_{color}"
    
    print("Saving file...")
    file_path = PosixPath(out_path)
    file_path = file_path.expanduser()
    file_path = file_path.resolve()
    
    stem = file_path.stem
    file_path = file_path.with_name(f"{stem}.gpl")
    
    try:            
        with open(file_path, 'w') as f:
            f.write(gpl)

    except:
        print(f"Failed to save to the file '{file_path}'")
        return
    
    print(f"File saved to '{file_path}'")


def save_as_image(palette: list, in_path: str, out_path: str = None, use_floyd: bool = False):
    """
    Convert an image to a specified color palette and save the result.

    Args:
        palette (list): List of tuples containing decimal RGB values.
        in_path (str): Path to the input image file.
        out_path (str, optional): Path to the output image file. Defaults to None.
        use_floyd (bool, optional): Whether to use Floyd-Steinberg dithering. Defaults to False.
    """

    palette = list(palette)

    in_path = PosixPath(in_path)
    in_path = in_path.expanduser()
    in_path = in_path.resolve()

    if not out_path:
        out_path = in_path
    
    else:
        out_path = PosixPath(out_path)
        out_path = out_path.expanduser()
        out_path = out_path.resolve()

    new_image = None

    try:
        with Image.open(in_path) as image:
            new_image = image.copy()

        print("Converting image... (this might take a couple of minutes)")
        new_image.convert('RGB')
        image_data = np.array(new_image).astype(np.float64)
        palette_array = np.array(palette)
        kd_tree = KDTree(palette_array)

        def find_closest_color(pixel):
            _, index = kd_tree.query(pixel[:3])
            return palette_array[index]
        
        def floyd_steinberg_dither(image_data):
            height, width, _ = image_data.shape
            for y in range(height):
                for x in range(width):
                    # Get the original pixel
                    original_pixel = image_data[y, x]

                    # Find the closest color in the palette
                    new_pixel = find_closest_color(original_pixel)

                    # Compute the quantization error
                    error = original_pixel - new_pixel

                    # Update the current pixel to the new pixel value
                    image_data[y, x] = new_pixel

                    # Propagate the error to the neighboring pixels
                    if x + 1 < width:
                        image_data[y, x + 1] += error * 7 / 16
                    if y + 1 < height:
                        if x - 1 >= 0:
                            image_data[y + 1, x - 1] += error * 3 / 16
                        image_data[y + 1, x] += error * 5 / 16
                        if x + 1 < width:
                            image_data[y + 1, x + 1] += error * 1 / 16

            return image_data
        
        if use_floyd:
            new_image = floyd_steinberg_dither(image_data)
            new_image = np.clip(new_image, 0, 255)

        else:
            new_image = np.apply_along_axis(find_closest_color, 2, image_data)

        new_image = np.uint8(new_image)
        new_image = Image.fromarray(new_image)

        print("Image converted")

        if not out_path.parent.exists():
            out_path.parent.mkdir(parents=True, exist_ok=True)
            print(f'Directory {out_path.parent} created')
        
        if not out_path.exists():
            out_path.touch()
            print(f"File {out_path} created")

        print("Saving image...")
        new_image.save(out_path)
        print(f"Image saved to {out_path}")

    except FileNotFoundError:
        print(f"Input file {in_path} not found")

    except Exception as e:
        print(f"An unknown error happened while saving the image: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert image to Gruvbox palette')

    message = 'Input image file path'
    parser.add_argument('-f', '--file-path', type=str, required=True, help=message)

    message = 'Output image file path'
    parser.add_argument('-o', '--out-path', type=str, help=message)
    
    message = 'Use brightest colors while extending colors'
    parser.add_argument('-l', '--light', action='store_true', help=message)
    
    message = 'Create .gpl file'
    parser.add_argument('--gpl', action='store_true', help=message)
    
    message = 'Use Floyd-Steinberg dithering'
    parser.add_argument('-d', '--dither', action='store_true', help=message)
    
    message = 'Interpolate between palette colors'
    parser.add_argument('-i', '--interpolate', action='store_true', help=message)
    
    message = 'A .gpl file path used as a base palette'
    parser.add_argument('-p', '--palette-path', type=str, help=message)

    args = parser.parse_args()

    # ---

    if args.palette_path:
        og_palette = PosixPath(args.palette_path)
        og_palette = read_gpl(og_palette)
    
    else:
        og_palette = PALETTE

    file_path = PosixPath(args.file_path)

    palette = extend_palette(og_palette, use_brightest=args.light, interpolate=args.interpolate)

    if args.out_path:
        out_path = PosixPath(args.out_path)
    
    else:
        stem = file_path.stem
        suffix = file_path.suffix
        out_path = file_path.with_name(f"{stem}_gruvbox{suffix}")

    if args.gpl:
        save_as_gpl(palette, out_path)

    save_as_image(palette, file_path, out_path, use_floyd=args.dither)