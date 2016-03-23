#
configure_file(plothist plothist)
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/plothist DESTINATION bin)
