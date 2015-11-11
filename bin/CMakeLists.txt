#
configure_file(PlotHist.py PlotHist.py)
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/PlotHist.py DESTINATION bin)
