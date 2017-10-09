TESTS_ENVIRONMENT = BATS_NO_SUMMARY=1

TESTS                   = tutorial_4
check_PROGRAMS          = tutorial_4
tutorial_4_SOURCES      = tutorial_4.c \
                          tutorial_region.c \
                          Imbalancer.cpp
tutorial_4_CPPFLAGS     = -I$(GEOPM_INC)
tutorial_4_LDFLAGS     = -L$(GEOPM_LIB) -lgeopm
TESTS                  += test_module
TESTS                  += rm_execution

