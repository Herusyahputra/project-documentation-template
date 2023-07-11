#### create the share object for python
g++ -c -fPIC moildev.cpp -o moildev.o
g++ -shared moildev.o -o moildev.so

g++ -shared -Wl,-soname,moildev.so -o moildev.so  moildev.o -lopencv_core -lopencv_highgui -lopencv_imgproc

#### or use
g++ -fPIC -shared moildev.cpp -o moildev.so
