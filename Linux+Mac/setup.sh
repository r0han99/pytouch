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
    
    echo -e "${GREEN}Moving .tar to PATH ${NC}"
    
    echo ""
    
    mv pytouch.tar /usr/local/bin
    
    echo -e "${GREEN}Extracting Content ..${NC}"
    
    echo ""
    
    tar -xvf /usr/local/bin/pytouch.tar
    
    echo -e "${GREEN}Setting up Pytouch utility as a Command..${NC}"
    
    echo ""
    
    echo -e "${GREEN}Command Setting Complete${NC}"
    
    echo ""
    
    echo -e "${GREEN}You are Good to Go ..${NC}"
    
 
    echo ""
    
    echo -e  "${CYAN}do ${GREEN}pytouch --help ${CYAN} for the MANUAL${NC}"
    
    echo ""
    
    echo -e "I'll do it for you .. :) "
    
    echo ""
    
    echo ""
    
    echo ""
     
    pytouch --help
    
    
else
    echo -e "${RED}Pytouch utility 'pytouch.tar.bz2' file doesn't Exist in the relative(current) Path${NC}"
fi