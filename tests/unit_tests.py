import os

# Change too root directory
# Dengan assumsi bahwa os.getcwd() akan menghasilkan /root/app/tests
print("[test][debug] Menganti working directory.")
os.chdir(os.join.path(os.getwd(),".."))

from lib.validator.factory import ValidatorFactory

if __name__ == "__main__":
	print("[test][debug] Testing EmailValidator...")
	validator = import 
