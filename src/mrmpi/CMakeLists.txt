#SET(CMAKE_C_COMPILER /export/openmpi/bin/mpicc)
#SET(CMAKE_CXX_COMPILER /export/openmpi/bin/mpicxx)

#SET(CCFLAGS "-g -Wall -O -I../mrmpi")
#SET(CMAKE_CXX_FLAGS "-g -Wall ")
#SET(LINK "/export/openmpi/bin/mpicxx /export/mrmpi/lib")
#SET(LINKFLAGS "-g -O -L../mrmpi")
#SET(USRLIB "-lmrmpi")
#SET(SYSLIB "-lpthread")
#SET(LIB "/export/mrmpi/libmrmpi.a")
#SET(DEPFLAGS "-M")
#SET(ARCHIVE "ar")
#SET(ARFLAGS "-rc")

add_library (mrmpi mapreduce.cpp mapreduce.cpp cmapreduce.cpp keyvalue.cpp keymultivalue.cpp spool.cpp irregular.cpp hash.cpp memory.cpp error.cpp) 

#set(CMAKE_BUILD_TYPE Release)

#SET(CMAKE_BUILD_TYPE distribtion)
#SET(CMAKE_CXX_FLAGS_DISTRIBUTION "-O3")
#SET(CMAKE_C_FLAGS_DISTRIBUTION "-O3")

SET(CMAKE_BUILD_TYPE Debug)
SET(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
SET(CMAKE_C_FLAGS_DEBUG -g "-O0")
