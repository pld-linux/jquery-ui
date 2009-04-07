#!/bin/sh
PROG=${0##*/}
dir=$RPM_BUILD_ROOT/usr/share/jquery/ui
langfile=$1
tmp=$(mktemp) || exit 1
rc=0

find $dir -type d -name i18n > $tmp
echo '%defattr(644,root,root,755)' > $langfile

while read dir; do
	echo "%dir ${dir#$RPM_BUILD_ROOT}" >> $langfile

	+ ./find-lang.sh jquery-ui.lang
	+ lang=ui.datepicker-ar.js
	+ lang=ui.datepicker-ar
	+ dir=/usr/share/jquery/ui/i18n/ui.datepicker-ar.js
	+ echo ERROR: Need mapping for ui.datepicker-ar!
	+ >&2

set -x
	for f in $dir/??*.js; do
		lang=${f##*/ui.datepicker-}
		lang=${lang%.*}
		dir=${f#$RPM_BUILD_ROOT}
		case "$lang" in
		en-au)
			lang=en_AU
		;;
		en-ca)
			lang=en_CA
		;;
		en-uk)
			lang=en_UK
		;;
		fr-ca)
			lang=fr_CA
		;;
		pt-BR)
			lang=pt_BR
		;;
		sr-latn)
			lang=sr@Latin
		;;
		zh-CN)
			lang=zh_CN
		;;
		zh-TW)
			lang=zh_TW
		;;
		*-*)
			echo >&2 "ERROR: Need mapping for $lang!"
			exit 1
		;;
		esac
		echo "%lang($lang) ${dir#$RPM_BUILD_ROOT}" >> $langfile
	done
done < $tmp

if [ "$(egrep -v '(^%defattr|^$)' $langfile | wc -l)" -le 0 ]; then
	echo >&2 "$PROG: Error: international files not found!"
	rc=1
fi

rm -f $tmp
exit $rc
