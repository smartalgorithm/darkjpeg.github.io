
BUILD  = build
SOURCE = source

all: clean script dark style

script:
	iced -I window -cp -j -- \
	$(SOURCE)/backend.coffee $(SOURCE)/frontend.coffee | \
	uglifyjs -c -p1 -m -o $(BUILD)/script.js - 2> /dev/null

dark:
	uglifyjs -c -p1 -m -o $(BUILD)/dark.js \
	$(SOURCE)/worker.js $(SOURCE)/sha3.js $(SOURCE)/aes256.js \
	$(SOURCE)/jpeg-encoder.js $(SOURCE)/jpeg-decoder.js 2> /dev/null

style:
	lessc -O2 --yui-compress $(SOURCE)/style.less > $(BUILD)/style.css

clean:
	rm -f $(BUILD)/*
