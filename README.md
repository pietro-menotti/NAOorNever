# NAOorNever
Team name: NAO OR NEVER

Members: Pietro Menotti, Lorenzo Moscardini

Description: this project focuses on building a dance coreography for NAO virtual robot given constraints on the total time of the coreography and on the mandatory moves that need to be executed.

In order to make the virtual robot dance, follow these steps:
- Use a Windows environment
- Make sure that both Python 2 and Python 3 are installed
- Required libraries: `random`, `sys`, `os`, `time`, `winsound`, `threading`
- Make sure that Git is installed
- From Git CMD, download the repository with `git clone https://github.com/pietro-menotti/NAOorNever`
- From the `bin` folder of Choreographe's installation launch `naoqi-bin.exe` 
- Open Choreographe and connect to virtual robot
- Open Git CMD in the project folder
- Make the script executable:
  ```bash
  chmod +x ./start.sh
- Launch the script:
  ```bash
  ./start.sh <nao_ip> <nao_port>
