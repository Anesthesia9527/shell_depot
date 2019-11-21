
#rm wavmeta_md5.log -f

OLDIFS="$IFS"   
IFS=$'\n\$'     
name_arry=(`cat /opt/tools/rec_md5/2818_quan.txt`)
IFS="$OLDIFS"

name_size=${#name_arry[*]}

for((x=1301; x<name_size; x++))
do
        name=${name_arry[x]}

	OLDIFS="$IFS"
	IFS=$'\n\$'
	book_arry=(`ls -d "/opt/ky100_deploy/ky100/wavMeta/$name"`)
	IFS="$OLDIFS"

	book_size=${#book_arry[*]}
	
	for((m=0; m<book_size; m++))
	do
		book=${book_arry[m]}
		echo $book
	
		OLDIFS="$IFS"
		IFS=$'\n\$'
		lesson_arry=(`ls -d "$book"/*/`)
		IFS="$OLDIFS"
		lesson_size=${#lesson_arry[*]}
		
		for((n=0; n<lesson_size; n++))
		do
			lesson=${lesson_arry[n]}
			echo $lesson
			
			OLDIFS="$IFS"
			IFS=$'\n\$'
			metaz_arry=(`ls -S "${lesson}"/*.wav.meta-modcz`)
			IFS="$OLDIFS"
			metaz_size=${#metaz_arry[*]}
			md5strlesson=""
			for((p=0; p<metaz_size; p++))
			do
				metaz=${metaz_arry[p]}		
				#echo $metaz
	
				md5str=`md5sum "$metaz" | awk '{print $1}'`
				md5strlesson=${md5strlesson}$md5str			
			done
			echo $lesson@@$md5strlesson >> wavmeta.log
		done	
		break
	done
done
