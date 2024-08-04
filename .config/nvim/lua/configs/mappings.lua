local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

-- Override p with "+p
map('n', 'p', '"+p', opts)
map('v', 'p', '"+p', opts)

-- Override y with "+y
map('n', 'y', '"+y', opts)
map('v', 'y', '"+y', opts)

-- Override d with "_d
map('n', 'd', '"_d', opts)
map('v', 'd', '"_d', opts)

-- Scroll up
map('n', '<C-u>', '<C-u>zz', opts)
map('n', '<C-d>', '<C-d>zz', opts)

-- Swap lines
map('n', '<A-j>', 'ddp', opts)
map('v', '<A-j>', 'ddp', opts)

map('n', '<A-k>', 'ddkkp', opts)
map('v', '<A-k>', 'ddkkp', opts)

-- Comment
map('n', '<leader>/', 'gcc', opts)
map('v', '<leader>/', 'gc', opts)

-- Bind ; to :
map("n", ";", ":", { desc = "CMD enter command mode" })