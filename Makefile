virtual_env = venv
src = src
project = lambda_project

install: virtual
build: clean_package build_package_tmp copy_python zip remove_tmp

virtual:
	 @echo "--> Setup and activate virtualenv"
	 if test ! -d "$(virtual_env)"; then \
	   sudo apt-get install -y python3-pip; \
	   sudo pip3 install virtualenv; \
	   virtualenv $(virtual_env); \
	 fi
	 @echo ""	

build_package_tmp:
	mkdir -p ./package/tmp/lib
	cp -a ./$(src)/. ./package/tmp/

copy_python:
	if test -d $(virtual_env)/lib; then \
	  cp -a $(virtual_env)/lib/python3.4/site-packages/. ./package/tmp/; \
	fi

zip:
	cd ./package/tmp && zip -r ../$(project).zip .

clean_package:
	rm -rf ./package/*

remove_tmp:
	rm -rf ./package/tmp/

