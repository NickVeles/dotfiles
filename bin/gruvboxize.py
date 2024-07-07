from pathlib import PosixPath
from PIL import Image
from scipy.spatial import KDTree
import numpy as np

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


def color_hex2dec(hexstr: str):

    r = int(hexstr[1:3], 16)
    g = int(hexstr[3:5], 16)
    b = int(hexstr[5:], 16)

    return (r, g, b)


def color_dec2hex(hexval: tuple, prefix: bool = True):
    
    color = "#" if prefix else ""
    for value in hexval:
        x = hex(value)
        x = x[2:]
        x = x.upper()
        x = x.rjust(2, '0')

        color += x

    return color


def luminance(color: tuple):
    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def extend_palette(palette: list, darkest_color: str = None, brightest_color: str = None, use_brightest: bool = False):

    print("Extending colors...")

    palette = map(color_hex2dec, palette)
    palette = list(palette)
    new_palette = set(palette)

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


def save_as_gpl(palette: list, out_path: str):
    gpl = "GIMP Palette\nName: Gruvbox Extended\nColumns: 1\n#"

    palette = extend_palette(PALETTE)

    for color in palette:
        r, g, b = color
        color = color_dec2hex(color, False)

        gpl += f"\n{r} {g} {b} color_{color}"
    
    print("Saving file...")
    file_path = PosixPath(out_path)
    file_path = file_path.expanduser()
    file_path = file_path.resolve()
    
    with open(file_path, 'w') as f:
        f.write(gpl)
    
    print(f"File saved to '{file_path}'")


def save_as_image(palette: list, in_path: str, out_path: str = None, use_floyd: bool = False):

    palette = extend_palette(palette, use_brightest=True)
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
        print(f"Input file {in_path} not found.")


if __name__ == "__main__":
    
    # TODO: Make this an executable with flags:
    # -f --file   - in_path
    # -o --out    - out_path
    # -l --light  - use brightness
    #    --gpl    - create .gpl file
    # -d --dither - use floyd-steinberg dither

    # TODO: Add docstrings

    in_path = "~/Pictures/Wallpapers/earth_4k.png"
    out_path = "~/Pictures/Wallpapers/earth_4k_gruvbox.png"
    save_as_image(PALETTE, in_path, out_path)