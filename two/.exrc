if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <D-BS> 
imap <M-BS> 
imap <M-Down> }
inoremap <D-Down> <C-End>
imap <M-Up> {
inoremap <D-Up> <C-Home>
noremap! <M-Right> <C-Right>
noremap! <D-Right> <End>
noremap! <M-Left> <C-Left>
noremap! <D-Left> <Home>
map! <D-v> *
nmap v :call Screen_Vars()
nmap  vip
vmap  "ry :call Send_to_Screen(@r)
map  
snoremap <silent> 	 i<Right>=TriggerSnippet()
nnoremap <NL> w
nnoremap  W
map  
snoremap ' b<BS>'
vmap [% [%m'gv``
nnoremap \gc :GitCommit
nnoremap \gA :GitAdd <cfile>
nnoremap \ga :GitAdd
nnoremap \gl :GitLog
nnoremap \gs :GitStatus
nnoremap \gD :GitDiff --cached
nnoremap \gd :GitDiff
vmap ]% ]%m'gv``
vmap a% [%v]%
nmap gx <Plug>NetrwBrowseX
map <M-Down> }
noremap <D-Down> <C-End>
map <M-Up> {
noremap <D-Up> <C-Home>
noremap <M-Right> <C-Right>
noremap <D-Right> <End>
noremap <M-Left> <C-Left>
noremap <D-Left> <Home>
snoremap <Left> bi
snoremap <Right> a
snoremap <BS> b<BS>
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
xmap <BS> "-d
vmap <D-x> "*d
vmap <D-c> "*y
vmap <D-v> "-d"*P
nmap <D-v> "*P
inoremap <silent> 	 =TriggerSnippet()
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=2
set backupdir=~/.vim-tmp
set directory=~/.vim-tmp
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set fillchars=fold:\ 
set fuoptions=maxvert,maxhorz
set guifont=Anonymous:h9.00
set guioptions=a
set guitablabel=%M%t
set helplang=en
set hidden
set ignorecase
set incsearch
set laststatus=2
set mouse=a
set printexpr=system('open\ -a\ Preview\ '.v:fname_in)\ +\ v:shell_error
set ruler
set rulerformat=%15(%c%V\ %p%%%)
set scrolloff=3
set shiftwidth=2
set showbreak=>
set showmatch
set smartcase
set smartindent
set smarttab
set tabstop=2
set termencoding=utf-8
set title
set wildmenu
set wildmode=list:longest
set window=23
" vim: set ft=vim :
