local map = vim.keymap.set

-- Override p with "+p
map({ 'n', 'v' }, 'p', '"+p')

-- Override y with "+y
map({ 'n', 'v' }, 'y', '"+y')

-- Override d with "_d
map({ 'n', 'v' }, 'd', '"_d')

-- Scroll up
map('n', '<C-u>', '<C-u>zz')
map('n', '<C-d>', '<C-d>zz')

-- Swap lines
map({ 'n', 'v' }, '<A-j>', 'ddp')
map({ 'n', 'v' }, '<A-k>', 'ddkkp')

-- Bind ; to :
map("n", ";", ":", { desc = "CMD enter command mode" })
