# dotfiles
A repository containing my linux dotfiles (WIP)


## Config:
- 🎨 `hyprland` - wayland compositor
- 🐚 `zsh` with `powerlevel10k` - shell + theme
- 💻 `alacritty` - termianl
- 🔍 `rofi-wayland` - dmenu
- 🖱️ `Bibata-Modern-Ice` - cursor-theme + hyprcursor
- 📂 `Orchis-Orange-Dark` - gtk-theme (5px)
- 🙂 `Papirus-Dark` - icon-theme
- 🕥 `aylurs-gtk-shell` - status Bar + widgets
- 🗃️ `thunar` - file manager


## Other important apps:
- `ufw` - firewall
- `nwg-look` - gtk theme editor
- `gnome-text-editor` - simple text editor
- `hyprcursor` - cursor for Hyprland
- `hyprlock` - lock screen for Hyprland
- `hypridle` - idle state manager for Hyprland
- `hyprpicker` - color picker for Hyprland
- `oh-my-zsh` - zsh tool
- `timeshift` - system backup manager
- `dconf-editor` - theme editor
- `pipewire-pulse` - for pavucontrol
- `pavucontrol` - sound control
- `pamixer` - terminal sound control
- `piper` - mouse control
- `grimblast-git` - screenshotting
- `inkscape` - SVG editor
- `jq` - jquery
- `socat` - reading sockets
- `alacritty-themes` - terminal theme
- `vlc` - media player
- `ranger` - backup file manager
- `dragon-drop` - addon for ranger
- `papirus-icon-theme` - icons for dmenu
- `bluez` - bluetooth
- `bluez-utils` - bluetooth
- `blueman` - bluetooth GUI
- `btop` - task manager
- `rofi-calc-git` - calc plugin for rofi
- `rofi-emoji-git` - emoji plugin for rofi
- `cliphist` - clipboard plugin for rofi
- `wtype` - keyboard simulator
- `qt5-graphicaleffects` - sddm theme
- `qt5-quickcontrols2` - sddm theme
- `qt5-svg` - sddm theme
- `baobab` - disk visualization
- `gparted` - disk management
- `lxsession-gtk3` - authentication agent for polkit
- `xorg-xhost` - server access control (needed for gparted)
- `cups` - printing system
- `gutenprint` - printing tool
- `ghostscript` - printing requirement
- `hplip` - HP printer drivers (optional)
- `foomatic-db-gutenprint-ppds` - drivers for printing
- `firefox-pwa` - progressive web apps (used with the [PWA Addon](https://addons.mozilla.org/en-US/firefox/addon/pwas-for-firefox/))
- `file-roller` - archive tool
- `thunar-archive-plugin` - archive plugin for Thunar
- `thunar-volman` - removable devices control plugin for Thunar
- `thunar-vcs-plugin` - GIT actions plugin for Thunar
- `thunar-media-tags-plugin` - detailed information about media files for Thunar
- `gvfs` - sidebar addon for Thunar
- `tumbler` - thumbnail generator for Thunar
- `ffmpegthumbnailer` - video addon for Tumbler
- `libgsf` - open document extension addon for Tumbler
- `raw-thumbnailer` - raw file addon for Tumbler
- `gthumb` - image viewer/editor
- `swappy` - draw on screenshots
- `pinta` - paint-like image editor
- `aylurs-gtk-shell` - status bar and widgets (WIP)
- `gnome-bluetooth-3.0` - AGS dependency
- `brightnessctl` - brightness control
- `neovim` - in-terminal text editor
- `visual-studio-code-bin` - main code editor


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
- Run `papirus-folders -C black`.
- Place `sugar-candy` folder in `/usr/share/sddm/themes/`.
- Place `sddm.conf` file in `/etc/`.
- Use `btop` theme: `gruvbox_dark_v2` with background disabled.
- Add my [Firefox theme](https://color.firefox.com/?theme=XQAAAAJEAgAAAAAAAABBKYhm849SCicxcUEYWXcGHf3p79EhVPXpIZrHAQWRl-Xj7UBmqXiG5wsXaL1ei0ksRAZcdZKRsFsq0aumeRoYoFBgVqqVSrjrXjE9g6WCrDK3H57ewuq5UH2Vw__5oBNYn6Nht9OYQoY77X8xVKBamAkH1_pGP1tH9eonM18oEUlsavVANpmyMt0uPgdrLvmwcYLdDvlfraS7IP8I9XeqodbvSjmFHuWlM3mec8JTBLrc823vzrqxfgMs1s9RfWSg3eE4Q0ADIvqshDOXUHYRVr3fC7TZonEoADBBEvOqc1gzFmbWjo-fMQu3IKPXp_2NelOdIJcuxVNVhkeEiZ2d_s23iQ2f_7Aj2AA).
- Add the [PWA Extension](https://unhook.app/) to Firefox in order to use PWAs:
  - Create Firefox PWAs for Google Gmail, Keep, and Calendar.
  - Create Discord PWA:
    - rename `discord.desktop.bak` to `discord.desktop` if you want to use the standard discord app;
    - enable Firefox > Settings > Force links into a new window;
    - enable Firefox > Settings > Focus the existing window;
    - disable Firefox > Open links in tabs instead of new windows;
    - enable Discord > User Settings > Notifications > Enable Desktop Notifications.

Some day I'll surely create an install script that does all these things. For now, it's all manual.


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

