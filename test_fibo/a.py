import os,sys
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#sys.path.append("../fibo")
absFilePath = os.path.abspath(__file__)
print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)
parentDir = os.path.dirname(fileDir)
print(parentDir)


newPath = os.path.join(parentDir, 'fibo')   # Get the directory for StringFunctions
print(newPath)
sys.path.append(newPath)

import fibo2
a=fibo2.fib(5)