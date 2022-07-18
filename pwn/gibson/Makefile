OUT_DIR=gibson_s390x

# Don't actually rebuild - risk of messing up the md5sum and offsets for players
# binary: mainframe.c
# 	s390x-linux-gnu-gcc -fno-stack-protector -no-pie -o bin/mainframe $<

dist: 
	mkdir -p ./$(OUT_DIR)/docs
	mkdir -p ./$(OUT_DIR)/xinetd
	mkdir -p ./$(OUT_DIR)/bin
	mkdir -p ./$(OUT_DIR)/flags
	mkdir -p ./$(OUT_DIR)/wrapper_scripts
	cp ./docs/tips.md ./$(OUT_DIR)/docs/tips.md
	cp ./bin/mainframe ./$(OUT_DIR)/bin/mainframe
	cp ./bin/libc.so.6 ./$(OUT_DIR)/bin/libc.so.6
	cp ./flags/fake_flag ./$(OUT_DIR)/flags/flag
	cp ./Dockerfile ./$(OUT_DIR)/Dockerfile
	cp ./docker-compose.yml ./$(OUT_DIR)/docker-compose.yml
	cp ./xinetd/infrastructure.xinetd ./$(OUT_DIR)/xinetd/
	cp ./xinetd/competitor.xinetd ./$(OUT_DIR)/xinetd
	cp ./wrapper_scripts/infrastructure_wrapper.sh ./$(OUT_DIR)/wrapper_scripts/
	cp ./wrapper_scripts/competitor_wrapper.sh ./$(OUT_DIR)/wrapper_scripts/
	tree -a ./$(OUT_DIR)
	tar -cf $(OUT_DIR).tar ./$(OUT_DIR)
	rm -r $(OUT_DIR)

clean:
	# rm -f bin/mainframe
	rm -f gibson_s390x.tar
