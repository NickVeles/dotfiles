# dotfiles
A repository containing my linux dotfiles (WIP)

### Config:
- 🎨 `hyprland` - wayland compositor
- 🐚 `zsh` with `powerlevel10k` - shell + theme
- 💻 `alacritty` - termianl
- 🔍 `rofi-wayland` - dmenu
- 🖱️ `Bibata-Modern-Ice` - cursor-theme + hyprcursor
- 📂 `Orchis-Orange-Dark` - gtk-theme (5px)
- 🙂 `Tela-black-dark` - icon-theme
- 🕥 `aylurs-gtk-shell` - status Bar + widgets
- 🗃️ `thunar` - file manager

---

### Other important apps:
- `ufw` - firewall
- `lxappearance` - GTK theme editor (highly recommended)
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
- `Tela-circle-black-dark` - icons for dmenu
- `bluez` - bluetooth
- `bluez-utils` - bluetooth
- `blueman` - bluetooth GUI
- `btop` - task manager
- `rofi-calc-git` - calc plugin for rofi
- `rofi-emoji-git` - emoji plugin for rofi
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

---

### Fonts I use
- `ttf-jetbrains-mono`
- `ttf-jetbrains-mono-nerd`
- `otf-opendyslexic-nerd` [link](https://opendyslexic.org/)
- `ttf-font-awesome`
- `noto-fonts-emoji`

---

### Things To Do
- Unpack the `Tela-black-dark.tar.gz` file (modified icons).
- Delete the `assets` folder.
- Enable services: `ufw`, `cups.service`.
- Enable `Experimental = true` in `/etc/bluetooth/main.conf`
- Place `sugar-candy` folder in `/usr/share/sddm/themes/`.
- Place `sddm.conf` file in `/etc/`.
- Use `btop` theme: `gruvbox_dark_v2` with background disabled.
- Add my [Firefox theme](https://color.firefox.com/?theme=XQAAAAJEAgAAAAAAAABBKYhm849SCicxcUEYWXcGHf3p79EhVPXpIZrHAQWRl-Xj7UBmqXiG5wsXaL1ei0ksRAZcdZKRsFsq0aumeRoYoFBgVqqVSrjrXjE9g6WCrDK3H57ewuq5UH2Vw__5oBNYn6Nht9OYQoY77X8xVKBamAkH1_pGP1tH9eonM18oEUlsavVANpmyMt0uPgdrLvmwcYLdDvlfraS7IP8I9XeqodbvSjmFHuWlM3mec8JTBLrc823vzrqxfgMs1s9RfWSg3eE4Q0ADIvqshDOXUHYRVr3fC7TZonEoADBBEvOqc1gzFmbWjo-fMQu3IKPXp_2NelOdIJcuxVNVhkeEiZ2d_s23iQ2f_7Aj2AA).
- Add the [PWA Extension](https://unhook.app/) to Firefox in order to use PWAs:
  - Create Firefox PWAs for Google's [Gmail](https://raw.githubusercontent.com/vinceliuice/Tela-circle-icon-theme/master/src/scalable/apps/gmail.svg), [Keep](https://raw.githubusercontent.com/NickVeles/dotfiles/main/assets/keep.svg), and [Calendar](https://raw.githubusercontent.com/vinceliuice/Tela-circle-icon-theme/master/src/scalable/apps/google-calendar.svg) (links to icons).
  - Create Discord PWA ([icon](https://raw.githubusercontent.com/vinceliuice/Tela-circle-icon-theme/master/src/scalable/apps/discord.svg)):
    - rename `discord.desktop.bak` to `discord.desktop` if you want to use the standard discord app);
    - enable Firefox > Settings > Force links into a new window;
    - enable Firefox > Settings > Focus the existing window;
    - disable Firefox > Open links in tabs instead of new windows;
    - enable Discord > User Settings > Notifications > Enable Desktop Notifications.

---

### Acknowledgements
This repo uses direct or modified files that bypass their intended downloads. Here's the credit to their authors:
- [Tela Icon Theme](https://github.com/vinceliuice/Tela-icon-theme) by Vince.
- [Tela Circle Icon Theme](https://github.com/vinceliuice/Tela-circle-icon-theme) by Vince.
- [Sugar Candy SDDM Theme](https://github.com/Kangie/sddm-sugar-candy) by Matt Jolly.

