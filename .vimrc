" Bật highlight cú pháp cho một loại file (như .py, .cpp, .xml)
syntax enable
" Sử dụng clipboard hệ thống thay buffer của vim
set clipboard=unnamedplus
autocmd BufEnter * :set scroll=10 "set croll line 
syntax on

set encoding=UTF-8
set mouse=a "enable mouse trong context của neovim 

set incsearch 
set hlsearch  "hightlight text khi search 

set tabstop=4 "space mỗi lần tab
set softtabstop=0
set shiftwidth=4
set number
set backspace=indent,eol,start  " more powerful backspacing

"=============" install plugin
" Gọi đầu tiên
call plug#begin('~/.vim/plugged')

"theme gruvbox
Plug 'morhetz/gruvbox'
" Kết thúc việc cài plugin
call plug#end()

"============" setting for plugin
"for gruvbox
set background=dark
highlight Normal ctermbg=None
colorscheme gruvbox
let g:airline_theme='gruvbox'
set termguicolors
