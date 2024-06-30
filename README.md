# dotfiles
A repository containing my linux dotfiles (WIP)


## Config:
- 🖥️ OS: Arch Linux
- 🐚 Shell: zsh
- 🎨 DE: Hyprland
- 🖱️ Cursor: Bibata-Modern-Gruvbox-Light
- 🖼️ Theme: Gruvbox-Dark
- 📁 Icons: Gruvbox-Plus-Dark
- ⬛ Terminal: alacritty
- 🕥 Widgets: AGS
- 🗃️ File Manager: Thunar


## Dependencies:

<details>
  <summary><h3>Dependency Description</h3></summary>

  These apps are required by the config
  
#### Window Management
- `hyprland` - window manager
- `hyprcursor` - cursor for Hyprland
- `hyprlock` - lock screen for Hyprland
- `hypridle` - idle state manager for Hyprland
- `hyprpicker` - color picker for Hyprland

#### Terminal & Shell
- `alacritty` - terminal
  - `alacritty-themes` - terminal theme
- `zsh` - shell
  - `oh-my-zsh` - zsh tool
  - `powerlevel10k` - zsh theme

#### Text Editors & IDEs
- `gnome-text-editor` - simple text editor
- `neovim` - in-terminal text editor
- `visual-studio-code-bin` - main code editor

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
- `ranger` - backup file manager
  - `dragon-drop` - addon for ranger
- `file-roller` - archive tool

#### System Tools & Utilities
- `ufw` - firewall
- `timeshift` - system backup manager
- `lxsession-gtk3` - authentication agent for polkit
- `xorg-xhost` - server access control (needed for gparted)
- `baobab` - disk visualization
- `gparted` - disk management

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
- `ghostscript` - printing requirement
- `hplip` - HP printer drivers (optional)
- `foomatic-db-gutenprint-ppds` - drivers for printing

#### GUI Customization & Themes
- `aylurs-gtk-shell` - widgets + bar / status bar and widgets (WIP)
- `nwg-look` - gtk theme editor
- `dconf-editor` - theme editor
- `gruvbox-plus-icon-theme-git` - main icons
- `papirus-icon-theme` - backup icons
- `qt5-graphicaleffects` - sddm theme
- `qt5-quickcontrols2` - sddm theme
- `qt5-svg` - sddm theme

#### Media & Graphics
- `vlc` - media player
- `inkscape` - SVG editor
- `gthumb` - image viewer/editor
- `swappy` - draw on screenshots
- `pinta` - paint-like image editor

#### Bluetooth
- `gnome-bluetooth-3.0` - AGS dependency

#### System Enhancements
- `btop` - task manager
- `piper` - mouse control / mouse config tool
- `wtype` - keyboard simulator
- `brightnessctl` - brightness control

#### Screenshotting & Clipboarding
- `grimblast-git` - screenshotting
- `cliphist` - clipboard plugin for rofi
- `dragon-drop` - addon for ranger

#### Rofi Plugins
- `rofi-calc-git` - calc plugin for rofi
- `rofi-emoji-git` - emoji plugin for rofi

#### Web
- `firefox-pwa` - progressive web apps (used with the [PWA Addon](https://addons.mozilla.org/en-US/firefox/addon/pwas-for-firefox/))

#### Miscellaneous
- `jq` - jquery
- `socat` - reading sockets
</details>

<details>
  <summary><h3>Optional</h3></summary>
  
  These apps are not required anywhere in the config.

  - WIP
</details>

## Fonts I use
- `ttf-jetbrains-mono`
- `ttf-jetbrains-mono-nerd`
- `otf-opendyslexic-nerd` [link](https://opendyslexic.org/)
- `ttf-font-awesome`
- `noto-fonts`
- `noto-fonts-emoji`


## Things To Do
- Check `.config/hypr/nvidia.conf` for important information (if using nvidia gpu)
- Enable services: `ufw`, `cups.service`.
- Enable `Experimental = true` in `/etc/bluetooth/main.conf`.
- Unpack the `.local/share/icons/Bibata-Gruvbox-Cursors.tar.gz` file.
- Place `sugar-candy` folder in `/usr/share/sddm/themes/`.
- Place `sddm.conf` file in `/etc/`.
- Use `btop` theme: `gruvbox_dark_v2` with background disabled.
- Add my [Firefox theme]() WIP!.
- Add the [PWA Extension](https://unhook.app/) to Firefox in order to use PWAs:
  - Create Firefox PWAs for Google Gmail, Keep, and Calendar.
  - Create Discord PWA:
    - rename `discord.desktop.bak` to `discord.desktop` if you want to use the standard discord app;
    - enable Firefox > Settings > Force links into a new window;
    - enable Firefox > Settings > Focus the existing window;
    - disable Firefox > Open links in tabs instead of new windows;
    - enable Discord > User Settings > Notifications > Enable Desktop Notifications.
- Install the [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme).

Some day I'll (surely) create an install script that does all these things. For now, it's all manual.


## FAQ

### How to change the GTK theme?
1. Open the `.config/hypr/hyprland.conf` file.
2. Find the line with `env = GTK_THEME,Current-Theme`, where `Current-Theme` is the placeholder for your current theme.
3. Change `Current-Theme` to the name of your desired theme.
    - e.g. `env = GTK_THEME,Arc-Dark`
4. Save the file and either reboot your computer or exit to SDDM.


## Acknowledgements
This repo uses direct or modified files that bypass their intended downloads. Here's the credit to their authors:
- [Sugar Candy SDDM Theme](https://github.com/Kangie/sddm-sugar-candy) by [Matt Jolly](https://github.com/Kangie/).
- Custom gruvbox cursors were created with [bibata.live](https://www.bibata.live/studio) by [Abdulkaiz Khatri](https://github.com/ful1e5).

