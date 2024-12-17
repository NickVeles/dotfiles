# dotfiles
A repository containing my linux dotfiles (WIP)


## Config
- 🖥️ **OS**: Arch Linux
- 🐚 **Shell**: zsh
- 🎨 **DE**: Hyprland
- 🖱️ **Cursor**: Bibata-Modern-Light
- 🖼️ **Theme**: Gruvbox-Dark
- 📁 **Icons**: Gruvbox-Plus-Dark
- ⬛ **Terminal**: kitty
- 🕥 **Widgets**: AGS
- 🗃️ **File Manager**: Thunar


## Install

⚠ This is very WIP. Run at your own risk.

1. Install all the dependencies.
2. Run `git clone https://github.com/NickVeles/dotfiles/` .
3. Extract the cloned folder to your home directory.
4. Do all the things in the **"Things you have to do manually"** section.

### Deps
```
yay -S hyprland-git hyprcursor-git hyprlock-git hypridle-git hyprpicker-git kitty zsh oh-my-zsh powerlevel10k thunar thunar-archive-plugin thunar-volman thunar-vcs-plugin thunar-media-tags-plugin gvfs tumbler ffmpegthumbnailer libgsf raw-thumbnailer file-roller ufw timeshift lxsession-gtk3 bluez bluez-utils blueman pipewire-pulse pavucontrol pamixer cups gutenprint ghostscript hplip foomatic-db-gutenprint-ppds aylurs-gtk-shell nwg-look dconf-editor gruvbox-plus-icon-theme-git papirus-icon-theme qt5-graphicaleffects qt5-quickcontrols2 qt5-svg vlc gthumb swappy pinta gnome-bluetooth-3.0 btop piper wtype brightnessctl grimblast-git rofi-wayland rofi-calc-git rofi-emoji-git firefox-pwa jq socat python-scipy tree neovim ripgrep yazi zen-browser-avx2-bin
```

<details>
  <summary><h3>Description</h3></summary>

  This software is required by the config.
  
  #### Window Management
  - `hyprland-git` - window manager
    - `hyprcursor-git` - cursor for Hyprland
    - `hyprlock-git` - lock screen for Hyprland
    - `hypridle-git` - idle state manager for Hyprland
    - `hyprpicker-git` - color picker for Hyprland
  
  #### Terminal & Shell
  - `kitty` - terminal
  - `zsh` - shell
    - `oh-my-zsh` - zsh tool
    - `powerlevel10k` - zsh theme
  - `tree` - directory tree
  
  #### File Management
  - `thunar` - file explorer
    - `thunar-archive-plugin` - archive plugin for Thunar
    - `thunar-volman` - removable devices control plugin for Thunar
    - `thunar-vcs-plugin` - GIT actions plugin for Thunar
    - `thunar-media-tags-plugin` - detailed information about media files for Thunar
    - `gvfs` - sidebar addon for Thunar
    - `tumbler` - thumbnail generator for Thunar
      - `ffmpegthumbnailer` - video addon for Tumbler
      - `libgsf` - open document extension addon for Tumbler
      - `raw-thumbnailer` - raw file addon for Tumbler
  - `file-roller` - archive tool
  - `yazi` - terminal file explorer
  - `neovim` - in-terminal text editor
    - `ripgrep` - telescope plugin dependency
  
  #### System Tools & Utilities
  - `ufw` - firewall
  - `timeshift` - system backup manager
  - `lxsession-gtk3` - authentication agent for polkit
  
  #### Networking & Bluetooth
  - `bluez` - bluetooth
  - `bluez-utils` - bluetooth
  - `blueman` - bluetooth GUI
  
  #### Audio Management
  - `pipewire-pulse` - for pavucontrol
  - `pavucontrol` - sound control
  - `pamixer` - terminal sound control
  
  #### Printing
  - `cups` - printing system
  - `gutenprint` - printing tool
  - `ghostscript` - printing dep
  - `hplip` - HP printer drivers (optional)
  - `foomatic-db-gutenprint-ppds` - drivers for printing
  
  #### GUI Customization & Themes
  - `gnome-bluetooth-3.0` - AGS dependency
  - `aylurs-gtk-shell` - widgets + bar / status bar and widgets (WIP)
  - `nwg-look` - gtk theme editor
  - `dconf-editor` - theme editor
  - `gruvbox-plus-icon-theme-git` - main icons
  - `papirus-icon-theme` - backup icons
  - `qt5-graphicaleffects` - sddm theme dep
  - `qt5-quickcontrols2` - sddm theme dep
  - `qt5-svg` - sddm theme dep
  
  #### Media & Graphics
  - `vlc` - media player
  - `gthumb` - image viewer/editor
  - `swappy` - draw on screenshots
  - `pinta` - paint-like image editor
  
  #### System Enhancements
  - `btop` - task manager
  - `piper` - mouse control / mouse config tool
  - `wtype` - keyboard simulator
  - `brightnessctl` - brightness control
  
  #### Screenshotting
  - `grimblast-git` - screenshotting
  
  #### Launcher
  - `rofi-wayland` - launcher
    - `rofi-calc-git` - calc plugin for rofi
    - `rofi-emoji-git` - emoji plugin for rofi
  
  #### Web
  - `zen-browser-avx2-bin` - optimized firefox-based browser
  - `firefox-pwa` - progressive web apps (used with the [PWA Addon](https://addons.mozilla.org/en-US/firefox/addon/pwas-for-firefox/))
  
  #### Miscellaneous
  - `jq` - jquery
  - `socat` - reading sockets
  - `python-scipy` - gruvboxize requirement
</details>

### Optional Deps
```
yay -S gnome-text-editor visual-studio-code-bin baobab xorg-xhost gparted inkscape gimp fastfetch
```

<details>
  <summary><h3>Description</h3></summary>
  
  This software is not required anywhere in the config.

  - `gnome-text-editor` - simple text editor
  - `visual-studio-code-bin` - main code editor
  - `baobab` - disk visualization
  - `xorg-xhost` - server access control (needed for gparted)
  - `gparted` - disk management
  - `inkscape` - SVG editor
  - `gimp` - raster graphics editor
  - `fastfetch` - system information tool
</details>

## Fonts

```
yay -S ttf-jetbrains-mono ttf-jetbrains-mono-nerd otf-opendyslexic-nerd ttf-font-awesome noto-fonts noto-fonts-emoji noto-fonts-extra noto-fonts-cjk
```

<details>
  <summary><h3>Description</h3></summary>
  
  - `ttf-jetbrains-mono` - UI font
  - `ttf-jetbrains-mono-nerd` - UI font
  - `otf-opendyslexic-nerd` - [link](https://opendyslexic.org/)
  - `ttf-font-awesome`
  - `noto-fonts` - Main font for everything
  - `noto-fonts-emoji` - Emoji font
  - `noto-fonts-extra` - Additional formatting options for main font
  - `noto-fonts-cjk` - chinese/japanese/korean
</details>


## Things you have to do manually
- Check `.config/hypr/nvidia.conf` for important information (if using nvidia gpu)
- Enable services: `ufw`, `cups.service`.
- Enable `Experimental = true` in `/etc/bluetooth/main.conf`.
- Place `sugar-candy` folder in `/usr/share/sddm/themes/`.
- Place `sddm.conf` file in `/etc/`.

Some day I'll (surely) create an install script that does all these things. For now, it's all manual.


## FAQ

### How can I change the system theme?
1. Changing the GTK theme:
    - Open the `.config/hypr/hyprland.conf` file
    - Find the line `env = GTK_THEME,placeholder`, where `placeholder` is the currently set theme
    - Replace `placeholder` with your desired theme
    - Reboot or exit to SDDM
2. Changing the terminal theme:
    - Run `kitty +kitten themes`
    - Select the theme you want

### How can I change the wallpaper?

### Where can I find your cursors?
Here's the direct **download**: [Bibata-Gruvbox-Cursors.tar.gz](https://github.com/NickVeles/dotfiles/raw/main/.local/share/icons/Bibata-Gruvbox-Cursors.tar.gz). I used the *bibata.live* tool to create them.

### Where can I find your wallpapers?
Here's the direct **download**: [Wallpapers.tar.gz](https://github.com/NickVeles/dotfiles/raw/main/Pictures/Wallpapers/Wallpapers.tar.gz). Here are the links to the original images/wallpapers: [Mars Wallpaper](https://www.pixel4k.com/planet-mars-4k-8k-2212.html), [Earth Image](https://assets.science.nasa.gov/content/dam/science/esd/eo/content-feature/nightlights/images/media/BlackMarble_2016_Americas_composite.png).


## Acknowledgements
This repo uses direct or modified files that bypass their intended downloads. Here's the credit to their authors:
- [Sugar Candy SDDM Theme](https://github.com/Kangie/sddm-sugar-candy) by [Matt Jolly](https://github.com/Kangie/).
