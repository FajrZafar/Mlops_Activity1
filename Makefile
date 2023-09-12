install:
	pip install -r requirements.txt

test:
	pytest test_main.py


# when you run "make install" on the terminal it'll run the command under the install scope
# you can also add it to the yaml file

# Makefile is used to run complex terminal commands by using keywords instead of typing the entire sequence again and again
