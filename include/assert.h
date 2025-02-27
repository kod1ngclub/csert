#ifndef CSERT_ASSERT_H
#define CSERT_ASSERT_H

#include <stdbool.h>

void csert_assert(
    const bool condition,
    const char* const expression,

    const char* const component,
    const char* const filename,
    const char* const funcname,
    const int line
);

void csert_assertm(
    const char* const message,
    const bool condition,
    const char* const expression,

    const char* const component,
    const char* const filename,
    const char* const funcname,
    const int line
);

#endif // CSERT_ASSERT_H
