# # To improve
# # * dependency items are declared at different places
# #   - This file two places DEP_DANSE_PKGS, CPACK_DEBIAN_PACKAGE_DEPENDS
# #   - File rpm.spec.in
# # * rpm and deb releases are treated differently:
# #   - rpm: source rpm
# #   - deb: binary deb
# # * upload-<> should also upload to github release site

# cmake_minimum_required (VERSION 2.6)
# project (histogram)

set(VERSION "0.3.9")
set(AUTHOR "Jiao Lin")
set(AUTHOR_EMAILE "jiao.lin@gmail.com")
set(VENDOR "DANSE")
set(SUMMARY "histogram")
set(LICENSE "BSD")
set(RPM_APP_GROUP "Development/Tools")
set(GITHUB_URL "https://github.com/neutrons/histogram-dev") # this repo
set (HOMEPAGE ${GITHUB_URL})

# # this is released with danse.ins packages
# set(DEP_DANSE_PKGS "danse.ins")

# # package repository at packagecloud
# set (PKGCLOUD_USERNAME "danse")
# set (PKGCLOUD_REPO "ins")
# # debian
# # set(DOCKER_PKGING_DEB_DIST_NAME "ubuntu")
# # set(DOCKER_PKGING_DEB_DIST_VERSION "12.04")
# # dependencies
# set (DOCKER_PKGING_DEPS_DEB "python-numpy danse.ins journal pyre")
# set (DOCKER_PKGING_DEPS_RPM "numpy danse.ins journal pyre")
# set (DOCKER_PKGING_TEST_SRPM ". /opt/danse/bin/setup-danse.sh && python -c 'import histogram as p; print p'")
# set (DOCKER_PKGING_TEST_RPM ${DOCKER_PKGING_TEST_SRPM})
# set (DOCKER_PKGING_TEST_DEB ${DOCKER_PKGING_TEST_SRPM})
# set (CONDA_PKGING_BUILD_DEPS "python numpy journal")
# set (CONDA_PKGING_RUN_DEPS "python numpy danse.ins journal pyre h5py")

# # variables
# set (PYBINDING_NAME "${PROJECT_NAME}module")
# set (LIB_NAME "${PROJECT_NAME}")
# set (PKG_NAME "${PROJECT_NAME}")

# # get cmake_utils
# IF(EXISTS "cmake_utils/")
#   execute_process(
#     COMMAND git pull
#     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/cmake_utils
#     )
# ELSE(EXISTS "cmake_utils/")
#   execute_process(
#     COMMAND git clone https://github.com/danse-inelastic/cmake_utils
#     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
#     )
# ENDIF(EXISTS "cmake_utils/")
# set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)

# # lib64
# include(System)

# # ABI
# add_definitions(-D_GLIBCXX_USE_CXX11_ABI=0)

# #list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

# # needs python
# find_package ( PythonLibs REQUIRED )
# find_package ( PythonInterp REQUIRED )
# # python installation path
# set(INSTALL_PY_PATH "${INSTALL_LIB_DIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages")

# #
# enable_testing()

# subdirs
add_subdirectory(lib)
# add_subdirectory(pyext)
add_subdirectory(src)
add_subdirectory(bin)
# add_subdirectory(etc)
add_subdirectory(tests)

# # packaging
# # CPACK
# set(CPACK_PACKAGE_VERSION ${VERSION})
# # set(CPACK_GENERATOR  "RPM")
# set(CPACK_GENERATOR  "DEB")
# set(CPACK_PACKAGE_NAME ${PKG_NAME})
# set(CPACK_PACKAGE_SUMMARY ${SUMMARY})
# set(CPACK_PACKAGE_LICENSE ${LICENSE})
# set(CPACK_PACKAGE_RELEASE 0)
# set(CPACK_PACKAGE_APP_GROUP ${RPM_APP_GROUP})
# set(CPACK_PACKAGE_CONTACT ${AUTHOR})
# set(CPACK_PACKAGE_VENDOR ${VENDOR})
# set(CPACK_PACKAGING_INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
# set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_PACKAGE_RELEASE}.${CMAKE_SYSTEM_PROCESSOR}")
# set(CPACK_RPM_PACKAGE_REQUIRES "cmake")
# set(CPACK_DEBIAN_PACKAGE_DEPENDS "python, danse.ins")
# include(CPack)

# # source tar ball
# add_custom_command(
#   OUTPUT ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
#   COMMAND git archive --format=tar --prefix=${PKG_NAME}-${CPACK_PACKAGE_VERSION}/ HEAD | gzip -c > ${CMAKE_CURRENT_BINARY_DIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
#   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#   )
# add_custom_target(
#   src_tgz
#   DEPENDS ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
#   )

# # CPack does not have a rule for source rpm
# # the following is a way to do that
# #
# set(RPM_BUILD_DIR rpm_build)
# # rpm spec file
# configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/rpm.spec.in
#   ${CMAKE_CURRENT_BINARY_DIR}/${RPM_BUILD_DIR}/SPECS/${PKG_NAME}.spec )
# # rules to build src rpm
# set(SRC_RPM ${PKG_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_PACKAGE_RELEASE}.src.rpm)
# add_custom_command(
#   OUTPUT ${SRC_RPM}
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/BUILD
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/BUILDROOT
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/RPMS
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SOURCES
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SPECS
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SRPMS
#   COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/tmp
#   COMMAND ${CMAKE_COMMAND} -E copy ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz ${RPM_BUILD_DIR}/SOURCES
#   COMMAND rpmbuild -bs --define=\"_topdir ${RPM_BUILD_DIR}\" --buildroot=${RPM_BUILD_DIR}/tmp  ${RPM_BUILD_DIR}/SPECS/${PKG_NAME}.spec
#   COMMAND ${CMAKE_COMMAND} -E copy ${RPM_BUILD_DIR}/SRPMS/${SRC_RPM} ${SRC_RPM}
#   WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
#   DEPENDS src_tgz
#   )
# add_custom_target(
#   srpm
#   DEPENDS ${SRC_RPM}
#   )

# # folders for build and test packaging artifacts
# # deb/rpm
# include(docker)
# # conda
# include(conda)


cmake_minimum_required(VERSION 3.4)
project(histogram)
find_package(PythonExtensions REQUIRED)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the source file(s)
add_library(Array_1D MODULE src/Array_1D.cpp)

# Link any necessary libraries (if any)
# target_link_libraries(my_module PRIVATE some_library)


python_extension_module(Array_1D)
install(TARGETS Array_1D LIBRARY DESTINATION Array_1D)