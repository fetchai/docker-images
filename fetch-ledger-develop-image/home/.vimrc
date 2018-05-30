syntax on

"Information on the following setting can be found with
":help set
set tabstop=4
set expandtab
set autoindent 
set shiftwidth=4  "this is the level of autoindent, adjust to taste
set ruler
set number
set backspace=indent,eol,start
set visualbell
set mouse=a
set hlsearch
set clipboard=unnamed

" Session options: disable storing global options and folds in to the session
" file:
set ssop-=options
set ssop-=folds

" Uncomment below to make screen not flash on error
" set vb t_vb=""

"Enable mosue support"
"set mouse=a"

filetype plugin indent on
syntax on

autocmd Filetype xml setlocal ts=2 sw=2 sts=0 expandtab
autocmd Filetype html setlocal ts=2 sw=2 sts=0 expandtab
autocmd Filetype ruby setlocal ts=2 sw=2 sts=0 expandtab

autocmd Filetype java setlocal ts=4 sw=4 sts=0 expandtab
autocmd Filetype javascript setlocal ts=4 sw=4 sts=0 expandtab
autocmd Filetype coffeescript setlocal ts=4 sw=4 sts=0 expandtab
autocmd Filetype jade setlocal ts=4 sw=4 sts=0 expandtab

nmap <F3> i<C-R>=strftime("%FT%T%z")<CR><Esc>
imap <F3> <C-R>=strftime("%FT%T%z")<CR>

