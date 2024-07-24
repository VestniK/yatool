JAVA_LIBRARY()

DISABLE(OPENSOURCE_EXPORT)


IF(JDK_VERSION == "")
    JDK_VERSION(11)
ENDIF()

INCLUDE(${ARCADIA_ROOT}/contrib/java/org/junit/junit-bom/5.5.2/ya.dependency_management.inc)

PEERDIR(contrib/java/org/junit/jupiter/junit-jupiter-api)

JAVA_SRCS(SRCDIR src/main/java **/*)

END()
