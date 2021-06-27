let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/scripts/cryptobot
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
edit main.js
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 1resize ' . ((&columns * 93 + 94) / 188)
exe '2resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 2resize ' . ((&columns * 93 + 94) / 188)
exe '3resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 3resize ' . ((&columns * 94 + 94) / 188)
exe '4resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 4resize ' . ((&columns * 94 + 94) / 188)
argglobal
setlocal fdm=expr
setlocal fde=GetPotionFold(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
3
normal! zo
7
normal! zo
let s:l = 7 - ((6 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
7
normal! 0
wincmd w
argglobal
if bufexists("index.html") | buffer index.html | else | edit index.html | endif
setlocal fdm=expr
setlocal fde=GetPotionFold(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
17
normal! zo
let s:l = 11 - ((10 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
11
normal! 018|
wincmd w
argglobal
if bufexists("crypto.py") | buffer crypto.py | else | edit crypto.py | endif
setlocal fdm=expr
setlocal fde=GetPotionFold(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
1
normal! zo
12
normal! zo
let s:l = 3 - ((2 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
3
normal! 03|
wincmd w
argglobal
if bufexists("chart.js") | buffer chart.js | else | edit chart.js | endif
setlocal fdm=expr
setlocal fde=GetPotionFold(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 042|
wincmd w
3wincmd w
exe '1resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 1resize ' . ((&columns * 93 + 94) / 188)
exe '2resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 2resize ' . ((&columns * 93 + 94) / 188)
exe '3resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 3resize ' . ((&columns * 94 + 94) / 188)
exe '4resize ' . ((&lines * 22 + 23) / 47)
exe 'vert 4resize ' . ((&columns * 94 + 94) / 188)
tabnext 1
badd +2 crypto_ws.py
badd +2 index.html
badd +0 main.js
badd +46 ~/scripts/englishteachingappbackup/templates/base.html
badd +0 chart.js
badd +193 ~/.vimrc
badd +0 crypto.py
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
