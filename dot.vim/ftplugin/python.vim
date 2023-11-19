
" Only outside python projects
if empty(ale#python#FindProjectRootIni(str2nr(expand('<abuf>'))))
	" E127,E128: hanging instead of visual indent
	" FI58: hint to maybe use "annotations" future...
	let b:ale_python_flake8_options = '--ignore E127,E128,FI58 --min-version 3.10 --no-accept-encodings'
endif

