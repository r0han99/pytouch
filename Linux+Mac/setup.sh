#!/bin/bash 

GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m' 
NC='\033[0m' 

if [ -f ./pytouch.tar.bz2 ]
then 
    echo ""
    
    echo -e "${GREEN}Initiating ..${NC}"
    
    echo ""
    
    echo -e "${GREEN}Authenticating bzip2 ..${NC}"
    
    echo ""
    
    bunzip2 ./pytouch.tar.bz2
    
    echo -e "${GREEN}Cracked !${NC}"
    
    echo ""
    
    echo -e "${GREEN}Extracting Content ..${NC}"
    
    echo ""
    
    tar -xvf ./pytouch.tar
    
    echo ""
    
    echo -e "${GREEN}Handiling permissions ..${NC}"
    
    echo -e "${GREEN}Required to be ${RED}Root .. ${NC}"
    
    echo -e "Enter password if prompted for. ${RED}[Enter correctly]${NC}"
    
    echo ""
    
    sudo chmod 777 pytouch pytouch.py help.py
    
    echo -e "${GREEN}Moving .tar to PATH ${NC}"
    
    echo ""
    
    sudo mv pytouch pytouch.py help.py /usr/local/bin/
    
    
    echo -e "${GREEN}Setting up Pytouch utility as a Command..${NC}"
    
    echo ""
    
    echo -e "${GREEN}Command Setting Complete${NC}"
    
    echo ""
    
    echo -e "${GREEN}Executing the Command, for initial log setup..${NC}"
    
 
    echo ""
    
    pytouch        
    
    echo ""
    
    echo "You are good to go, do pytouch --help for MANUAL PAGE. "
    
    echo ""
      
    
    
else
    echo -e "${RED}Pytouch utility 'pytouch.tar.bz2' file doesn't Exist in the relative(current) Path${NC}"
fi