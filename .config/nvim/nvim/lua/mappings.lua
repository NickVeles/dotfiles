require "nvchad.mappings"

local map = vim.keymap.set

-- Override <C-p> with "+p
map('n', '<C-p>', '"+p')
map('v', '<C-p>', '"+p')

-- Override <C-y> with "+y
map('n', '<C-y>', '"+y')
map('v', '<C-y>', '"+y')

-- Override d with "_d
map('n', 'd', '"_d')
map('v', 'd', '"_d')

-- Override <C-u> with <C-r>
map('n', '<C-u>', '<C-r>')

-- Swap lines
map('n', '<A-j>', 'ddp')
map('v', '<A-j>', 'ddp')
map('n', '<A-k>', 'ddkkp')
map('v', '<A-k>', 'ddkkp')

-- Open Ranger
map('n', '<leader>rr', ':Ranger<CR>')

-- Built-in remaps

map("n", ";", ":", { desc = "CMD enter command mode" })

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")
