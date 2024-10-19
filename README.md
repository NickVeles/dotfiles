# dotfiles
A repository containing my linux dotfiles (WIP)


## Config
- 🖥️ **OS**: Arch Linux
- 🐚 **Shell**: zsh
- 🎨 **DE**: Hyprland
- 🖱️ **Cursor**: Bibata-Modern-Gruvbox-Light
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
4. Do all things in **Things To Do** section.

### Deps
```
yay -S hyprland hyprcursor hyprlock hypridle hyprpicker kitty zsh oh-my-zsh powerlevel10k thunar thunar-archive-plugin thunar-volman thunar-vcs-plugin thunar-media-tags-plugin gvfs tumbler ffmpegthumbnailer libgsf raw-thumbnailer file-roller ufw timeshift lxsession-gtk3 bluez bluez-utils blueman pipewire-pulse pavucontrol pamixer cups gutenprint ghostscript hplip foomatic-db-gutenprint-ppds aylurs-gtk-shell nwg-look dconf-editor gruvbox-plus-icon-theme-git papirus-icon-theme qt5-graphicaleffects qt5-quickcontrols2 qt5-svg vlc gthumb swappy pinta gnome-bluetooth-3.0 btop piper wtype brightnessctl grimblast-git cliphist rofi-wayland rofi-calc-git rofi-emoji-git firefox-pwa jq socat python-scipy tree neovim ripgrep yazi zen-browser-avx2-bin
```

<details>
  <summary><h3>Description</h3></summary>

  This software is required by the config.
  
  #### Window Management
  - `hyprland` - window manager
    - `hyprcursor` - cursor for Hyprland
    - `hyprlock` - lock screen for Hyprland
    - `hypridle` - idle state manager for Hyprland
    - `hyprpicker` - color picker for Hyprland
  
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
    - `cliphist` - clipboard plugin for rofi
  
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
- Unpack the `.local/share/icons/Bibata-Gruvbox-Cursors.tar.gz` file.
- Place `sugar-candy` folder in `/usr/share/sddm/themes/`.
- Place `sddm.conf` file in `/etc/`.
- Use `btop` theme: `gruvbox_dark_v2` with background disabled.
- Add my [Firefox theme](https://addons.mozilla.org/en-US/firefox/addon/gruvbox-dark-theme-shapes/).
- Add the [PWA Extension](https://unhook.app/) to Firefox in order to use PWAs:
  - Create Discord PWA:
    - rename `discord.desktop.bak` to `discord.desktop` if you want to use the standard discord app;
    - enable Firefox > Settings > Force links into a new window;
    - enable Firefox > Settings > Focus the existing window;
    - disable Firefox > Open links in tabs instead of new windows;
    - enable Discord > User Settings > Notifications > Enable Desktop Notifications.
- Install the [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme).
- Install [vim-plug](https://github.com/junegunn/vim-plug).
  - Use `sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'`

Some day I'll (surely) create an install script that does all these things. For now, it's all manual.


## FAQ

### 1. How to change the GTK theme?
First of all, it's **not recommended**, as I use the gruvbox theme everywhere, including widgets and other stuff not affected by the GTK theme. But if you insist:

1. Open the `.config/hypr/hyprland.conf` file.
2. Find the line with `env = GTK_THEME,Current-Theme`, where `Current-Theme` is the placeholder for your current theme.
3. Change `Current-Theme` to the name of your desired theme.
    - e.g. `env = GTK_THEME,Arc-Dark`
4. Save the file and either reboot your computer or exit to SDDM.

### 2. Where can I find your cursors?
Here's the direct **download**: [Bibata-Gruvbox-Cursors.tar.gz](https://github.com/NickVeles/dotfiles/raw/main/.local/share/icons/Bibata-Gruvbox-Cursors.tar.gz). I used the *bibata.live* tool to create them.

### 3. Where can I find your wallpapers?
Here's the direct **download**: [Wallpapers.tar.gz](https://github.com/NickVeles/dotfiles/raw/main/Pictures/Wallpapers/Wallpapers.tar.gz). Here are the links to the original images/wallpapers: [Mars Wallpaper](https://www.pixel4k.com/planet-mars-4k-8k-2212.html), [Earth Image](https://assets.science.nasa.gov/content/dam/science/esd/eo/content-feature/nightlights/images/media/BlackMarble_2016_Americas_composite.png), [Abstract Shapes](https://www.reddit.com/r/wallpapers/comments/10d98fw/gruvbox_abstract_shapes_7680x4320/) by u/lqlarry.


## Acknowledgements
This repo uses direct or modified files that bypass their intended downloads. Here's the credit to their authors:
- [Sugar Candy SDDM Theme](https://github.com/Kangie/sddm-sugar-candy) by [Matt Jolly](https://github.com/Kangie/).
- Custom gruvbox cursors were created with [bibata.live](https://www.bibata.live/studio) by [Abdulkaiz Khatri](https://github.com/ful1e5).

