# ---------------------------------------------------------------------------
# leanstore
# ---------------------------------------------------------------------------

include(ExternalProject)
find_package(Git REQUIRED)

# Get jni-bind
ExternalProject_Add(
        jnibind_src
        PREFIX "vendor/jnibind"
        GIT_REPOSITORY "https://github.com/google/jni-bind.git"
        GIT_TAG b95b2ff5e0a85fd019dbf6e996b469865689145d
        TIMEOUT 10
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
        UPDATE_COMMAND ""
)

# Prepare jni-bind
ExternalProject_Get_Property(jnibind_src source_dir)
set(JNIBIND_INCLUDE_DIR ${source_dir})
file(MAKE_DIRECTORY ${JNIBIND_INCLUDE_DIR})
add_library(jnibind INTERFACE)
set_property(TARGET jnibind APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES ${JNIBIND_INCLUDE_DIR})

# Dependencies
add_dependencies(jnibind jnibind_src)
