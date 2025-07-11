# Generated by devtools/yamaker from nixpkgs 24.05.

LIBRARY()

VERSION(1.34.0)

ORIGINAL_SOURCE(https://github.com/chriskohlhoff/asio/archive/asio-1-34-0.tar.gz)

LICENSE(
    BSL-1.0 AND
    Public-Domain
)

LICENSE_TEXTS(.yandex_meta/licenses.list.txt)

PEERDIR(
    contrib/libs/openssl
)

ADDINCL(
    GLOBAL contrib/libs/asio/include
)

NO_COMPILER_WARNINGS()

NO_UTIL()

CFLAGS(
    GLOBAL -DASIO_STANDALONE
    GLOBAL -DASIO_SEPARATE_COMPILATION
)

IF (MSVC)
    CFLAGS(
        GLOBAL -DASIO_HAS_STD_COROUTINE
        GLOBAL -DASIO_HAS_CO_AWAIT
        GLOBAL -DASIO_HAS_DEDUCED_EXECUTE_MEMBER_TRAIT
        GLOBAL -DASIO_HAS_DEDUCED_EQUALITY_COMPARABLE_TRAIT
        GLOBAL -DASIO_HAS_DEDUCED_QUERY_MEMBER_TRAIT
        GLOBAL -DASIO_HAS_DEDUCED_QUERY_STATIC_CONSTEXPR_MEMBER_TRAIT
    )
ENDIF()

SRCS(
    src/asio.cpp
    src/asio_ssl.cpp
)

END()

RECURSE(
    src/examples/cpp11/allocation
    src/examples/cpp11/buffers
    src/examples/cpp11/chat/chat_client
    src/examples/cpp11/chat/chat_server
    src/examples/cpp11/chat/posix_chat_client
    src/examples/cpp11/deferred/deferred_1
    src/examples/cpp11/deferred/deferred_2
    src/examples/cpp11/echo/async_tcp_echo_server
    src/examples/cpp11/echo/async_udp_echo_server
    src/examples/cpp11/echo/blocking_tcp_echo_client
    src/examples/cpp11/echo/blocking_tcp_echo_server
    src/examples/cpp11/echo/blocking_udp_echo_client
    src/examples/cpp11/echo/blocking_udp_echo_server
    src/examples/cpp11/executors/actor
    src/examples/cpp11/executors/bank_account_1
    src/examples/cpp11/executors/bank_account_2
    src/examples/cpp11/executors/fork_join
    src/examples/cpp11/files/async_file_copy
    src/examples/cpp11/files/blocking_file_copy
    src/examples/cpp11/futures
    src/examples/cpp11/handler_tracking
    src/examples/cpp11/http/client/async_client
    src/examples/cpp11/http/client/sync_client
    src/examples/cpp11/http/server
    src/examples/cpp11/http/server2
    src/examples/cpp11/http/server3
    src/examples/cpp11/http/server4
    src/examples/cpp11/icmp
    src/examples/cpp11/invocation
    src/examples/cpp11/iostreams/daytime_client
    src/examples/cpp11/iostreams/daytime_server
    src/examples/cpp11/iostreams/http_client
    src/examples/cpp11/local/connect_pair
    src/examples/cpp11/local/iostream_client
    src/examples/cpp11/local/stream_client
    src/examples/cpp11/local/stream_server
    src/examples/cpp11/multicast/receiver
    src/examples/cpp11/multicast/sender
    src/examples/cpp11/nonblocking
    src/examples/cpp11/operations/composed_1
    src/examples/cpp11/operations/composed_2
    src/examples/cpp11/operations/composed_3
    src/examples/cpp11/operations/composed_4
    src/examples/cpp11/operations/composed_5
    src/examples/cpp11/operations/composed_6
    src/examples/cpp11/operations/composed_7
    src/examples/cpp11/operations/composed_8
    src/examples/cpp11/parallel_group/ranged_wait_for_all
    src/examples/cpp11/parallel_group/wait_for_all
    src/examples/cpp11/parallel_group/wait_for_one
    src/examples/cpp11/parallel_group/wait_for_one_error
    src/examples/cpp11/parallel_group/wait_for_one_success
    src/examples/cpp11/porthopper/client
    src/examples/cpp11/porthopper/server
    src/examples/cpp11/services
    src/examples/cpp11/socks4
    src/examples/cpp11/ssl/client
    src/examples/cpp11/ssl/server
    src/examples/cpp11/timeouts/async_tcp_client
    src/examples/cpp11/timeouts/blocking_tcp_client
    src/examples/cpp11/timeouts/blocking_token_tcp_client
    src/examples/cpp11/timeouts/blocking_udp_client
    src/examples/cpp11/timeouts/server
    src/examples/cpp11/timers
    src/examples/cpp11/tutorial/daytime1
    src/examples/cpp11/tutorial/daytime2
    src/examples/cpp11/tutorial/daytime3
    src/examples/cpp11/tutorial/daytime4
    src/examples/cpp11/tutorial/daytime5
    src/examples/cpp11/tutorial/daytime6
    src/examples/cpp11/tutorial/daytime7
    src/examples/cpp11/tutorial/timer1
    src/examples/cpp11/tutorial/timer2
    src/examples/cpp11/tutorial/timer3
    src/examples/cpp11/tutorial/timer4
    src/examples/cpp11/tutorial/timer5
    src/examples/cpp14/deferred/deferred_1
    src/examples/cpp14/deferred/deferred_2
    src/examples/cpp14/deferred/deferred_3
    src/examples/cpp14/deferred/deferred_4
    src/examples/cpp14/deferred/deferred_5
    src/examples/cpp14/deferred/deferred_6
    src/examples/cpp14/deferred/deferred_7
    src/examples/cpp14/echo/async_tcp_echo_server
    src/examples/cpp14/echo/async_udp_echo_server
    src/examples/cpp14/echo/blocking_tcp_echo_client
    src/examples/cpp14/echo/blocking_tcp_echo_server
    src/examples/cpp14/echo/blocking_udp_echo_client
    src/examples/cpp14/echo/blocking_udp_echo_server
    src/examples/cpp14/executors/actor
    src/examples/cpp14/executors/async_1
    src/examples/cpp14/executors/async_2
    src/examples/cpp14/executors/bank_account_1
    src/examples/cpp14/executors/bank_account_2
    src/examples/cpp14/executors/fork_join
    src/examples/cpp14/iostreams
    src/examples/cpp14/operations/c_callback_wrapper
    src/examples/cpp14/operations/callback_wrapper
    src/examples/cpp14/operations/composed_1
    src/examples/cpp14/operations/composed_2
    src/examples/cpp14/operations/composed_3
    src/examples/cpp14/operations/composed_4
    src/examples/cpp14/operations/composed_5
    src/examples/cpp14/operations/composed_6
    src/examples/cpp14/operations/composed_7
    src/examples/cpp14/operations/composed_8
    src/examples/cpp14/parallel_group/parallel_sort
    src/examples/cpp14/parallel_group/ranged_wait_for_all
    src/examples/cpp14/parallel_group/wait_for_all
    src/examples/cpp14/parallel_group/wait_for_one
    src/examples/cpp14/parallel_group/wait_for_one_error
    src/examples/cpp14/parallel_group/wait_for_one_success
)

IF (OS_LINUX OR OS_DARWIN)
    RECURSE(
        src/examples/cpp11/executors/pipeline
        src/examples/cpp11/executors/priority_scheduler
        src/examples/cpp11/fork/daemon
        src/examples/cpp11/fork/process_per_connection
        src/examples/cpp11/local/fd_passing_stream_client
        src/examples/cpp11/local/fd_passing_stream_server
        src/examples/cpp11/type_erasure
        src/examples/cpp14/executors/pipeline
        src/examples/cpp14/executors/priority_scheduler
    )
ENDIF()
