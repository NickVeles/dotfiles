return {
    defaults = { lazy = true },
    install = { colorscheme = { "gruvbox" } },
    spec = {
        { import = "plugins" },
    },
  
    ui = {
        icons = {
            ft = "",
            lazy = "󰂠 ",
            loaded = "",
            not_loaded = "",
        },
    },
}