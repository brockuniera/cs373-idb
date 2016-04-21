FILES :=                              \
    .gitignore                        \
    .travis.yml                       \
    makefile                          \
    apiary.apib                       \
    IDB3.log                          \
    models.html                        \
    app/models.py                         \
    app/tests.py                          \
    UML.pdf
	
check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__
	
test: app/tests.py
	coverage3 run    --branch app/tests.py >  tests.tmp 2>&1
	coverage3 report -m --omit=/lusr/lib/python3.4/dist-packages/*,/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/* >> tests.tmp
	cat tests.tmp
	
IDB1.log:
	git log > IDB1.log

IDB2.log:
	git log > IDB2.log

IDB3.log:
	git log > IDB3.log
	
models.html: models.py
	pydoc -w models

