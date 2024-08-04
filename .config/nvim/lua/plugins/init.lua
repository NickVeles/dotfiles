return {
    {
        "ellisonleao/gruvbox.nvim",
        lazy = false,
        config = function()
            local gruvbox = require('gruvbox')
            gruvbox.setup({
                transparent_mode = true,
            })
            vim.cmd('colorscheme gruvbox')
        end,
    },
    {
        "numToStr/Comment.nvim",
        lazy = false,
    },
    -- {
    --     'gorbit99/codewindow.nvim',
    --     lazy = false,
    --     config = function()
    --         local codewindow = require('codewindow')
    --         codewindow.setup({
    --             minimap_width = 16,
    --         })
    --         codewindow.apply_default_keybinds()
    --     end,
    -- },
}