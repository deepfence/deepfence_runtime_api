This folder contains some sample scripts.

1. start-vulnerability-scan.sh This script is used to scan images from the command line. It takes the type of scan as the input. ./start-vulnerability-scan.sh --help gives details about all the necessary switches

2. run-struts.sh This script starts a sample struts container that contains the Equifax exploit. This starts to listen at port 8080

3. run-exploit.sh This script runs the attack that was done on the Equifax container. It takes as a parameter the IP address of machine that has the struts container that was started using the script run-struts.sh

4. test_api.py A python script to exercise some sample features of the deepfence API subsystem
