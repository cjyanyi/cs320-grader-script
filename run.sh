#!bin/sh
for file in ./*
do
    if test -f $file
    then
        echo $file 是文件
    fi
    if test -d $file
    then
        echo $file 是目录
        cd ./$file/assignments/week3/
        cabal new-test > ./test_result_grader.txt
        cd ../../..
    fi
done