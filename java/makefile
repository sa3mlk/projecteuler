JAVAC=javac

SOURCES=$(wildcard *.java)
CLASSES=$(SOURCES:.java=.class)

all: $(CLASSES)

clean:
	@rm -f *.class

%.class: %.java
	$(JAVAC) $<

