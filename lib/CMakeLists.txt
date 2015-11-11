# ------------- Modify these -------------
set ( SRC_FILES 
  Array_1D.cc
  events2Ix.cc
  events2Ixy.cc
  Event2Quantity.cc
  NdArray.cc
  NdArraySlice.cc
  )

set ( INC_FILES
  Array_1D.h
  Array_1D.icc
  AxisMapper.h
  Event2Quantity.h
  GridData_1D.h
  GridData_2D.h
  GridData_4D.h
  EvenlySpacedAxisMapper.h
  EvenlySpacedGridData_1D.h
  EvenlySpacedGridData_2D.h
  EvenlySpacedGridData_4D.h
  Exception.h
  Histogrammer.h
  NdArray.h
  NdArray.icc
  NdArraySlice.h
  NdArraySlice.icc
  OutOfBound.h
  events2histogram.h
  events2EvenlySpacedIx.h
  events2EvenlySpacedIxy.h
  events2EvenlySpacedIxxxx.h
  events2Ix.h
  events2Ixy.h
  events2Ixxxx.h
  _macros.h
  )

set ( EXPORT_HEADERS ${INC_FILES} )
# ----------------------------------------

# -D
add_definitions(-DUSE_DANSE_NAMESPACE )

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )
# assume journal is already deployed at the same deployment prefix
# where we are going to deploy histogram
include_directories( ${DEPLOYMENT_PREFIX}/include )

# export headers from this project
foreach (header ${EXPORT_HEADERS})
  configure_file(
    "${header}"
    "${CMAKE_CURRENT_BINARY_DIR}/include/${PROJECT_NAME}/${header}"
    )
endforeach (header)

# create empty portinfo (pyre-config thing)
execute_process(
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/lib/include/portinfo
)

# -I and -L
include_directories(${CMAKE_BINARY_DIR}/lib/include)
# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} ${INC_FILES} )

# install headers
install (
  DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME})
# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )
