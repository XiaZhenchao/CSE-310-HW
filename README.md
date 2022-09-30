# CSE-310-HW
**Any external libraries used. 
Part1:
      import socket 
Part2:
      import socket
      import sys
      from unicodedata import name
      import os.path
Tools:
      MAC OS Monterey 
      Chrome Browser
      Python 3.8.5
      VScode python ide

Picture Order in PDF 1.Part 1 success 
                     2.Part 1 fail 
                     3.Part2 Success visit http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html  
                     4.Part2 Success visit http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html  
                     5.Part2 Success visit http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html  
                     6.Part2 Success visit http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html  
                     7.Part2 Success load cache to display the result in browser

Instructions on how to run your programs: 
Part1:
                    1.Open webserver.py and run 
                    2.Terminal will print localhostname, portNumber,and server is starting... 
                    3.Open Chrome Browser and enter the url(localhost:portNumber/helloworld.html), example: localhost:3002/helloworld.html 
                    4.It will display the result like picture 1 in pdf 
                    5.Change the wrong address, it will return 404 error page like picture 2 in the pdf

Part2:
                    1.Open proxyserver.py and run
                    2.Terminal will print port number,and server is starting... 
                    3.Open Chrome Browser and enter the url(localhost:portnumber/website.html), example: localhost:5059/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html or http://localhost:5058/http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
                    4.It will print target url and hostname in the terminal 
                    5.If there is no file which has same name as the url it will display the result from the server and save in the caches, it will print   
                      "SaveInCache"
                    6.Then the folder will get a new html as cache page 
                    7.If it is not a valid website, then the error page will come out.
